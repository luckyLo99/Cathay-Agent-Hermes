from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.runtime.mock_provider import MockProviderAdapter
from hermes_ext.runtime.request_envelope import LLMRequestEnvelope, PromptSegment
from hermes_ext.schema.portable_schema import PortableSchemaValidator


class CheckStatus(str, Enum):
    PASS = "pass"
    WARN = "warn"
    FAIL = "fail"


class DoctorCheck(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    name: str
    status: CheckStatus
    detail: str
    severity: str = "info"


class DoctorReport(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    ok: bool
    checks: list[DoctorCheck] = Field(default_factory=list)

    def to_exit_code(self) -> int:
        return 0 if self.ok else 1


class AgentDoctor:
    """
    Offline doctor for Phase 1 extension layer.

    This doctor intentionally avoids:
    - real model calls
    - .env reads
    - API key checks
    - Hermes state mutation
    """

    def __init__(self, project_root: Path | None = None) -> None:
        self.project_root = project_root or Path.cwd()

    def run_all(self) -> DoctorReport:
        checks = [
            self.check_python_version(),
            self.check_extension_layout(),
            self.check_no_api_key_required(),
            self.check_mock_provider(),
            self.check_portable_schema(),
            self.check_git_status(),
        ]
        ok = all(check.status != CheckStatus.FAIL for check in checks)
        return DoctorReport(ok=ok, checks=checks)

    def check_python_version(self) -> DoctorCheck:
        version = sys.version_info
        if (version.major, version.minor) < (3, 11):
            return DoctorCheck(
                name="python_version",
                status=CheckStatus.FAIL,
                severity="error",
                detail=f"Python >=3.11 required, got {version.major}.{version.minor}.{version.micro}",
            )

        if version.major == 3 and version.minor >= 14:
            return DoctorCheck(
                name="python_version",
                status=CheckStatus.FAIL,
                severity="error",
                detail=f"Python <3.14 required, got {version.major}.{version.minor}.{version.micro}",
            )

        return DoctorCheck(
            name="python_version",
            status=CheckStatus.PASS,
            detail=f"Python {version.major}.{version.minor}.{version.micro}",
        )

    def check_extension_layout(self) -> DoctorCheck:
        required = [
            self.project_root / "hermes_ext" / "__init__.py",
            self.project_root / "hermes_ext" / "runtime" / "request_envelope.py",
            self.project_root / "hermes_ext" / "runtime" / "mock_provider.py",
            self.project_root / "hermes_ext" / "runtime" / "agent_doctor.py",
            self.project_root / "hermes_ext" / "schema" / "portable_schema.py",
        ]
        missing = [str(path) for path in required if not path.exists()]
        if missing:
            return DoctorCheck(
                name="extension_layout",
                status=CheckStatus.FAIL,
                severity="error",
                detail="Missing files: " + ", ".join(missing),
            )

        return DoctorCheck(
            name="extension_layout",
            status=CheckStatus.PASS,
            detail="hermes_ext layout is present",
        )

    def check_no_api_key_required(self) -> DoctorCheck:
        provider_env_names = [
            "OPENAI_API_KEY",
            "ANTHROPIC_API_KEY",
            "OPENROUTER_API_KEY",
            "MISTRAL_API_KEY",
            "GEMINI_API_KEY",
        ]
        present = [name for name in provider_env_names if os.environ.get(name)]
        if present:
            return DoctorCheck(
                name="api_key_independence",
                status=CheckStatus.WARN,
                severity="warning",
                detail="Provider API key env vars are present, but Phase 1 did not read or require them",
            )

        return DoctorCheck(
            name="api_key_independence",
            status=CheckStatus.PASS,
            detail="No provider API key required",
        )

    def check_mock_provider(self) -> DoctorCheck:
        try:
            envelope = LLMRequestEnvelope(
                messages=[
                    PromptSegment.from_message(
                        "user",
                        "hello mock runtime",
                        segment_type="conversation",
                    )
                ]
            )
            response = MockProviderAdapter().generate(envelope)
        except Exception as exc:
            return DoctorCheck(
                name="mock_provider",
                status=CheckStatus.FAIL,
                severity="error",
                detail=f"Mock provider failed: {exc}",
            )

        if not response.content.startswith("MOCK_ECHO:"):
            return DoctorCheck(
                name="mock_provider",
                status=CheckStatus.FAIL,
                severity="error",
                detail=f"Unexpected mock content: {response.content}",
            )

        return DoctorCheck(
            name="mock_provider",
            status=CheckStatus.PASS,
            detail="Mock provider generated deterministic offline response",
        )

    def check_portable_schema(self) -> DoctorCheck:
        result = PortableSchemaValidator.validate(
            "command",
            {"argv": ["python", "--version"], "timeout_seconds": 30},
        )
        if not result.ok:
            return DoctorCheck(
                name="portable_schema",
                status=CheckStatus.FAIL,
                severity="error",
                detail=f"PortableSchema validation failed: {result.error}",
            )

        return DoctorCheck(
            name="portable_schema",
            status=CheckStatus.PASS,
            detail="PortableSchema validates known command payload",
        )

    def check_git_status(self) -> DoctorCheck:
        try:
            result = subprocess.run(
                ["git", "status", "--short"],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                check=False,
                timeout=10,
            )
        except Exception as exc:
            return DoctorCheck(
                name="git_status",
                status=CheckStatus.WARN,
                severity="warning",
                detail=f"Could not inspect git status: {exc}",
            )

        if result.returncode != 0:
            return DoctorCheck(
                name="git_status",
                status=CheckStatus.WARN,
                severity="warning",
                detail=result.stderr.strip() or "git status failed",
            )

        output = result.stdout.strip()
        if output:
            return DoctorCheck(
                name="git_status",
                status=CheckStatus.WARN,
                severity="warning",
                detail="Working tree has changes, expected during Phase 1 before commit",
            )

        return DoctorCheck(
            name="git_status",
            status=CheckStatus.PASS,
            detail="Working tree clean",
        )


def report_to_text(report: DoctorReport) -> str:
    lines = []
    for check in report.checks:
        marker = {
            CheckStatus.PASS: "✓",
            CheckStatus.WARN: "⚠",
            CheckStatus.FAIL: "✗",
        }[check.status]
        lines.append(f"{marker} {check.name}: {check.detail}")
    lines.append("")
    lines.append(f"overall: {'PASS' if report.ok else 'FAIL'}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Hermes extension Phase 1 offline doctor")
    parser.add_argument("--json", action="store_true", help="emit JSON report")
    parser.add_argument("--project-root", default=".", help="project root path")
    args = parser.parse_args(argv)

    report = AgentDoctor(Path(args.project_root).resolve()).run_all()

    if args.json:
        print(json.dumps(report.model_dump(mode="json"), ensure_ascii=False, indent=2))
    else:
        print(report_to_text(report))

    return report.to_exit_code()


if __name__ == "__main__":
    raise SystemExit(main())