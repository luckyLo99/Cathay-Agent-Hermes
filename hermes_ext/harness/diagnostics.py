from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.harness.contracts import ExtensionFlagName, FeatureFlagSet


class DiagnosticCheck(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    name: str
    ok: bool
    detail: str
    severity: str = "info"


class ExtensionDiagnosticReport(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    ok: bool
    checks: list[DiagnosticCheck] = Field(default_factory=list)

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")


class ExtensionDiagnostics:
    """
    Read-only diagnostics for hermes_ext.

    Does not read .env or API keys.
    """

    REQUIRED_MODULES = [
        "hermes_ext.runtime",
        "hermes_ext.schema",
        "hermes_ext.hooks",
        "hermes_ext.security",
        "hermes_ext.cathay",
        "hermes_ext.memoryx",
        "hermes_ext.orchestration",
        "hermes_ext.harness",
    ]

    FORBIDDEN_IMPORTS = [
        "run_agent",
        "cli",
        "hermes_state",
        "tools.memory_tool",
        "agent.memory_provider",
        "agent.memory_manager",
        "memoryx",
        "cathay_agent",
        "langgraph",
        "opentelemetry",
    ]

    def __init__(self, *, project_root: Path, flags: FeatureFlagSet) -> None:
        self.project_root = project_root
        self.flags = flags

    def run(self) -> ExtensionDiagnosticReport:
        checks = [
            self._check_python_version(),
            self._check_required_modules(),
            self._check_flags_safe_defaults(),
            self._check_state_dir_policy(),
            self._check_no_forbidden_module_loaded(),
        ]

        return ExtensionDiagnosticReport(
            ok=all(check.ok for check in checks),
            checks=checks,
        )

    def _check_python_version(self) -> DiagnosticCheck:
        version = sys.version_info
        ok = (version.major, version.minor) >= (3, 11) and not (
            version.major == 3 and version.minor >= 14
        )
        return DiagnosticCheck(
            name="python_version",
            ok=ok,
            detail=f"Python {version.major}.{version.minor}.{version.micro}",
            severity="error" if not ok else "info",
        )

    def _check_required_modules(self) -> DiagnosticCheck:
        missing: list[str] = []

        for module in self.REQUIRED_MODULES:
            try:
                importlib.import_module(module)
            except Exception as exc:
                missing.append(f"{module}: {exc}")

        if missing:
            return DiagnosticCheck(
                name="required_modules",
                ok=False,
                detail="missing modules: " + "; ".join(missing),
                severity="error",
            )

        return DiagnosticCheck(
            name="required_modules",
            ok=True,
            detail="all hermes_ext modules importable",
        )

    def _check_flags_safe_defaults(self) -> DiagnosticCheck:
        if self.flags.values[ExtensionFlagName.KILL_SWITCH].enabled:
            return DiagnosticCheck(
                name="feature_flags",
                ok=True,
                detail="kill switch enabled; extension capabilities disabled",
            )

        enabled_flags = [
            name.value
            for name in ExtensionFlagName
            if self.flags.is_enabled(name)
        ]

        if enabled_flags:
            return DiagnosticCheck(
                name="feature_flags",
                ok=True,
                detail="enabled effective flags: " + ", ".join(enabled_flags),
                severity="warning",
            )

        return DiagnosticCheck(
            name="feature_flags",
            ok=True,
            detail="all extension capabilities effectively disabled by default",
        )

    def _check_state_dir_policy(self) -> DiagnosticCheck:
        if not self.project_root.exists():
            return DiagnosticCheck(
                name="project_root",
                ok=False,
                detail=f"project root does not exist: {self.project_root}",
                severity="error",
            )

        return DiagnosticCheck(
            name="project_root",
            ok=True,
            detail=f"project root exists: {self.project_root}",
        )

    def _check_no_forbidden_module_loaded(self) -> DiagnosticCheck:
        loaded = []
        for module in self.FORBIDDEN_IMPORTS:
            if module in sys.modules:
                loaded.append(module)

        if loaded:
            return DiagnosticCheck(
                name="forbidden_modules",
                ok=False,
                detail="forbidden modules already loaded: " + ", ".join(loaded),
                severity="error",
            )

        return DiagnosticCheck(
            name="forbidden_modules",
            ok=True,
            detail="no forbidden runtime modules loaded by diagnostics",
        )