from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, field_validator

from hermes_ext.security.decisions import SecurityDecision


class PathGuardConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    workspace_root: Path = Field(default_factory=lambda: Path.cwd())
    allow_create_under_workspace: bool = True
    deny_hidden_sensitive_files: bool = True
    denied_names: set[str] = Field(
        default_factory=lambda: {
            ".env",
            ".env.local",
            ".env.production",
            "id_rsa",
            "id_dsa",
            "id_ed25519",
            "known_hosts",
            "credentials",
            "credentials.json",
            "secrets.json",
        }
    )
    denied_parts: set[str] = Field(
        default_factory=lambda: {
            ".ssh",
            ".aws",
            ".azure",
            ".gnupg",
            ".kube",
            ".docker",
        }
    )

    @field_validator("workspace_root")
    @classmethod
    def normalize_workspace_root(cls, value: Path) -> Path:
        return value.resolve()


class PathGuard:
    def __init__(self, config: PathGuardConfig | None = None) -> None:
        self.config = config or PathGuardConfig()

    def evaluate_read(self, path_text: str) -> SecurityDecision:
        return self._evaluate(path_text, operation="read")

    def evaluate_write(self, path_text: str) -> SecurityDecision:
        return self._evaluate(path_text, operation="write")

    def _evaluate(self, path_text: str, *, operation: str) -> SecurityDecision:
        if "\x00" in path_text:
            return SecurityDecision.deny(
                "Path contains null byte",
                rule_id="path.null_byte",
            )

        path_text = path_text.strip()
        if not path_text:
            return SecurityDecision.deny(
                "Path is empty",
                rule_id="path.empty",
            )

        raw_path = Path(path_text)
        candidate = raw_path if raw_path.is_absolute() else self.config.workspace_root / raw_path

        try:
            resolved = candidate.resolve(strict=False)
        except OSError as exc:
            return SecurityDecision.deny(
                f"Path resolution failed: {exc}",
                rule_id="path.resolve_failed",
            )

        if not self._is_under_workspace(resolved):
            return SecurityDecision.deny(
                f"Path escapes workspace: {resolved}",
                rule_id="path.workspace_escape",
                metadata={"path": str(resolved)},
            )

        if self.config.deny_hidden_sensitive_files:
            sensitive = self._sensitive_reason(resolved)
            if sensitive:
                return SecurityDecision.deny(
                    sensitive,
                    rule_id="path.sensitive",
                    metadata={"path": str(resolved)},
                )

        if operation == "write":
            if not self.config.allow_create_under_workspace:
                if not resolved.exists():
                    return SecurityDecision.ask(
                        f"Path does not exist and create is disabled: {resolved}",
                        rule_id="path.create_requires_approval",
                    )

        return SecurityDecision.allow(
            f"Path {operation} allowed inside workspace",
            rule_id=f"path.{operation}.allow",
            metadata={"path": str(resolved)},
        )

    def _is_under_workspace(self, path: Path) -> bool:
        try:
            path.relative_to(self.config.workspace_root)
            return True
        except ValueError:
            return False

    def _sensitive_reason(self, path: Path) -> str | None:
        lowered_name = path.name.lower()
        lowered_parts = {part.lower() for part in path.parts}

        denied_names = {name.lower() for name in self.config.denied_names}
        denied_parts = {part.lower() for part in self.config.denied_parts}

        if lowered_name in denied_names:
            return f"Sensitive file name is denied: {path.name}"

        matched_parts = lowered_parts.intersection(denied_parts)
        if matched_parts:
            return f"Sensitive path component is denied: {sorted(matched_parts)[0]}"

        return None