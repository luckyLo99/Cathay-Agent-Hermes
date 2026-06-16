from __future__ import annotations

import re

from pydantic import BaseModel, ConfigDict, Field, field_validator

from hermes_ext.security.decisions import SecurityDecision


class CommandGuardConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    deny_shell_metacharacters: bool = True
    denied_exact: set[str] = Field(
        default_factory=lambda: {
            "shutdown",
            "reboot",
            "halt",
            "poweroff",
            "mkfs",
        }
    )
    denied_tokens: set[str] = Field(
        default_factory=lambda: {
            "format",
            "diskpart",
            "reg",
            "bcdedit",
            "cipher",
        }
    )
    ask_tokens: set[str] = Field(
        default_factory=lambda: {
            "pip",
            "npm",
            "pnpm",
            "yarn",
            "uv",
            "git",
            "docker",
            "curl",
            "wget",
        }
    )
    dangerous_patterns: list[str] = Field(
        default_factory=lambda: [
            r"rm\s+-rf\s+/",
            r"del\s+/s\s+/q\s+[a-zA-Z]:\\",
            r"Remove-Item\s+.*-Recurse\s+.*-Force",
            r":\(\)\s*\{\s*:\|:\s*&\s*\};:",
        ]
    )

    @field_validator("dangerous_patterns")
    @classmethod
    def compile_patterns(cls, value: list[str]) -> list[str]:
        for pattern in value:
            re.compile(pattern, flags=re.IGNORECASE)
        return value


class CommandGuard:
    def __init__(self, config: CommandGuardConfig | None = None) -> None:
        self.config = config or CommandGuardConfig()

    def evaluate_argv(self, argv: list[str]) -> SecurityDecision:
        if not argv:
            return SecurityDecision.deny("Command argv is empty", rule_id="command.empty")

        normalized = []
        for item in argv:
            if "\x00" in item:
                return SecurityDecision.deny("Command contains null byte", rule_id="command.null_byte")
            item = item.strip()
            if not item:
                return SecurityDecision.deny("Command contains empty token", rule_id="command.empty_token")
            normalized.append(item)

        command_text = " ".join(normalized)
        executable = normalized[0].lower()

        for pattern in self.config.dangerous_patterns:
            if re.search(pattern, command_text, flags=re.IGNORECASE):
                return SecurityDecision.deny(
                    f"Command matches dangerous pattern: {pattern}",
                    rule_id="command.dangerous_pattern",
                    metadata={"pattern": pattern},
                )

        if executable in {item.lower() for item in self.config.denied_exact}:
            return SecurityDecision.deny(
                f"Executable is denied: {normalized[0]}",
                rule_id="command.executable_denied",
                metadata={"executable": normalized[0]},
            )

        lowered_tokens = {item.lower() for item in normalized}
        denied_hits = lowered_tokens.intersection({item.lower() for item in self.config.denied_tokens})
        if denied_hits:
            return SecurityDecision.deny(
                f"Command token denied: {sorted(denied_hits)[0]}",
                rule_id="command.token_denied",
                metadata={"token": sorted(denied_hits)[0]},
            )

        if self.config.deny_shell_metacharacters:
            shell_meta = {"&&", "||", "|", ";", "`", "$(", ">", ">>", "<"}
            hits = lowered_tokens.intersection(shell_meta)
            if hits:
                return SecurityDecision.ask(
                    f"Shell metacharacter requires approval: {sorted(hits)[0]}",
                    rule_id="command.shell_meta_requires_approval",
                    metadata={"token": sorted(hits)[0]},
                )

        ask_hits = lowered_tokens.intersection({item.lower() for item in self.config.ask_tokens})
        if ask_hits:
            return SecurityDecision.ask(
                f"Command token requires approval: {sorted(ask_hits)[0]}",
                rule_id="command.token_requires_approval",
                metadata={"token": sorted(ask_hits)[0]},
            )

        return SecurityDecision.allow(
            "Command shape allowed",
            rule_id="command.allow",
            metadata={"executable": normalized[0]},
        )