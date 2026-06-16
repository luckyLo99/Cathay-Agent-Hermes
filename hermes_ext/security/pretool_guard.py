from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.hooks.contracts import HookEvent
from hermes_ext.schema.portable_schema import PortableSchemaValidator
from hermes_ext.security.command_guard import CommandGuard
from hermes_ext.security.decisions import SecurityDecision, SecurityDecisionType
from hermes_ext.security.exec_policy import ExecPolicy
from hermes_ext.security.path_guard import PathGuard, PathGuardConfig
from hermes_ext.security.url_guard import URLGuard


class PreToolGuardConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    workspace_root: Path = Field(default_factory=lambda: Path.cwd())
    unknown_tool_decision: SecurityDecisionType = SecurityDecisionType.ASK


class PreToolGuard:
    """
    Phase 2 PreToolUse safety gate.

    It evaluates tool intent only. It never executes the tool.
    """

    def __init__(
        self,
        config: PreToolGuardConfig | None = None,
        *,
        path_guard: PathGuard | None = None,
        url_guard: URLGuard | None = None,
        command_guard: CommandGuard | None = None,
        exec_policy: ExecPolicy | None = None,
    ) -> None:
        self.config = config or PreToolGuardConfig()
        self.path_guard = path_guard or PathGuard(
            PathGuardConfig(workspace_root=self.config.workspace_root)
        )
        self.url_guard = url_guard or URLGuard()
        self.command_guard = command_guard or CommandGuard()
        self.exec_policy = exec_policy or ExecPolicy.default()

    def evaluate_event(self, event: HookEvent) -> SecurityDecision:
        tool_name = event.tool_name or event.payload.get("tool_name")
        if not isinstance(tool_name, str) or not tool_name.strip():
            return SecurityDecision.deny(
                "PreToolUse event is missing tool_name",
                rule_id="pretool.missing_tool_name",
            )

        return self.evaluate_tool(tool_name.strip(), event.payload)

    def evaluate_tool(self, tool_name: str, payload: dict[str, Any]) -> SecurityDecision:
        normalized_name = tool_name.lower().strip()

        if normalized_name in {"bash", "shell", "run_command", "command", "exec"}:
            return self._evaluate_command_tool(payload)

        if normalized_name in {"write", "write_file", "file_write", "edit", "replace"}:
            return self._evaluate_file_write_tool(payload)

        if normalized_name in {"read", "read_file", "file_read"}:
            return self._evaluate_file_read_tool(payload)

        if normalized_name in {"webfetch", "web_fetch", "fetch", "url_fetch", "http"}:
            return self._evaluate_url_fetch_tool(payload)

        if normalized_name in {"memory_write", "save_memory", "remember"}:
            return self._evaluate_memory_write_tool(payload)

        if self.config.unknown_tool_decision == SecurityDecisionType.DENY:
            return SecurityDecision.deny(
                f"Unknown tool denied: {tool_name}",
                rule_id="pretool.unknown_tool.deny",
            )

        if self.config.unknown_tool_decision == SecurityDecisionType.ALLOW:
            return SecurityDecision.allow(
                f"Unknown tool allowed by config: {tool_name}",
                rule_id="pretool.unknown_tool.allow",
            )

        return SecurityDecision.ask(
            f"Unknown tool requires approval: {tool_name}",
            rule_id="pretool.unknown_tool.ask",
        )

    def _evaluate_command_tool(self, payload: dict[str, Any]) -> SecurityDecision:
        argv = self._extract_argv(payload)
        schema_result = PortableSchemaValidator.validate(
            "command",
            {
                "argv": argv,
                "cwd": payload.get("cwd"),
                "timeout_seconds": payload.get("timeout_seconds", 60),
            },
        )
        if not schema_result.ok:
            return SecurityDecision.deny(
                f"Command schema rejected: {schema_result.error}",
                rule_id="pretool.command.schema",
            )

        command_decision = self.command_guard.evaluate_argv(argv)
        if command_decision.decision == SecurityDecisionType.DENY:
            return command_decision

        policy_decision = self.exec_policy.evaluate(argv)
        return self._max_decision([command_decision, policy_decision])

    def _evaluate_file_write_tool(self, payload: dict[str, Any]) -> SecurityDecision:
        path = self._extract_path(payload)
        schema_result = PortableSchemaValidator.validate(
            "file_write",
            {
                "path": path,
                "content": str(payload.get("content", "")),
                "encoding": payload.get("encoding", "utf-8"),
                "create_dirs": bool(payload.get("create_dirs", False)),
            },
        )
        if not schema_result.ok:
            return SecurityDecision.deny(
                f"File write schema rejected: {schema_result.error}",
                rule_id="pretool.file_write.schema",
            )

        return self.path_guard.evaluate_write(path)

    def _evaluate_file_read_tool(self, payload: dict[str, Any]) -> SecurityDecision:
        path = self._extract_path(payload)
        return self.path_guard.evaluate_read(path)

    def _evaluate_url_fetch_tool(self, payload: dict[str, Any]) -> SecurityDecision:
        url = str(payload.get("url", ""))
        schema_result = PortableSchemaValidator.validate(
            "url_fetch",
            {
                "url": url,
                "method": payload.get("method", "GET"),
                "headers": payload.get("headers", {}),
                "body": payload.get("body"),
                "timeout_seconds": payload.get("timeout_seconds", 30),
            },
        )
        if not schema_result.ok:
            return SecurityDecision.deny(
                f"URL fetch schema rejected: {schema_result.error}",
                rule_id="pretool.url_fetch.schema",
            )

        return self.url_guard.evaluate(url)

    def _evaluate_memory_write_tool(self, payload: dict[str, Any]) -> SecurityDecision:
        schema_result = PortableSchemaValidator.validate(
            "memory_write",
            {
                "namespace": str(payload.get("namespace", "")),
                "key": str(payload.get("key", "")),
                "value": str(payload.get("value", "")),
                "confidence": float(payload.get("confidence", 0.5)),
                "source_trace_id": payload.get("source_trace_id"),
            },
        )
        if not schema_result.ok:
            return SecurityDecision.deny(
                f"Memory write schema rejected: {schema_result.error}",
                rule_id="pretool.memory_write.schema",
            )

        return SecurityDecision.ask(
            "Memory write requires approval in Phase 2",
            rule_id="pretool.memory_write.requires_approval",
        )

    @staticmethod
    def _extract_argv(payload: dict[str, Any]) -> list[str]:
        argv = payload.get("argv")
        if isinstance(argv, list):
            return [str(item) for item in argv]

        command = payload.get("command")
        if isinstance(command, str):
            # Phase 2 deliberately does not implement shell parsing.
            # Shell strings require approval because quoting can hide intent.
            return [command]

        return []

    @staticmethod
    def _extract_path(payload: dict[str, Any]) -> str:
        for key in ("path", "file_path", "target_path"):
            value = payload.get(key)
            if isinstance(value, str):
                return value
        return ""

    @staticmethod
    def _max_decision(decisions: list[SecurityDecision]) -> SecurityDecision:
        order = {
            SecurityDecisionType.DENY: 4,
            SecurityDecisionType.ASK: 3,
            SecurityDecisionType.WARN: 2,
            SecurityDecisionType.ALLOW: 1,
        }
        return max(decisions, key=lambda item: order[item.decision])