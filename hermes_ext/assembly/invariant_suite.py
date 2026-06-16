from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any

from hermes_ext.assembly.contracts import (
    AssemblyArtifact,
    AssemblyArtifactKind,
    AssemblyInvariant,
    AssemblyInvariantSeverity,
    AssemblyInvariantStatus,
    AssemblyManifestConfig,
)
from hermes_ext.harness.contracts import ExtensionFlagName, FeatureFlagSet


class AssemblyInvariantSuite:
    """
    Release-style invariant suite for hermes_ext shadow assembly.

    It validates structure, no-import policy, feature flag defaults, and prior phase reports.
    """

    FORBIDDEN_IMPORT_PREFIXES = {
        "run_agent",
        "cli",
        "hermes_state",
        "hermes_cli",
        "gateway",
        "model_tools",
        "toolsets",
        "tools.registry",
        "tools.memory_tool",
        "agent.memory_provider",
        "agent.memory_manager",
        "agent.system_prompt",
        "providers",
        "memoryx",
        "cathay_agent",
        "dotenv",
        "openai",
        "anthropic",
        "openfeature",
        "pydantic_settings",
    }

    LIFELINE_FILES = {
        "cli.py",
        "run_agent.py",
        "hermes_cli/main.py",
        "gateway/run.py",
        "tools/registry.py",
        "model_tools.py",
        "toolsets.py",
        "agent/memory_provider.py",
        "agent/memory_manager.py",
        "tools/memory_tool.py",
        "agent/system_prompt.py",
        "agent/prompt_builder.py",
        "agent/context_compressor.py",
        "hermes_state.py",
        "providers/__init__.py",
        "providers/base.py",
        "tools/threat_patterns.py",
        "agent/redact.py",
        "cron/jobs.py",
        "cron/scheduler.py",
        "gateway/platforms/base.py",
        "gateway/session.py",
    }

    def __init__(self, config: AssemblyManifestConfig) -> None:
        self.config = config

    def run(self, artifacts: list[AssemblyArtifact]) -> list[AssemblyInvariant]:
        invariants = [
            self._invariant_artifacts_exist(artifacts),
            self._invariant_no_lifeline_artifacts(artifacts),
            self._invariant_feature_flags_default_disabled(),
            self._invariant_no_forbidden_imports(),
            self._invariant_phase10_golden_trace(),
            self._invariant_phase9_native_boundary(),
        ]

        return invariants

    def _invariant_artifacts_exist(self, artifacts: list[AssemblyArtifact]) -> AssemblyInvariant:
        missing = [item.relative_path for item in artifacts if not item.exists]
        if missing:
            return AssemblyInvariant(
                invariant_id="assembly.artifacts_exist",
                status=AssemblyInvariantStatus.WARN,
                severity=AssemblyInvariantSeverity.WARNING,
                message="Some expected artifact trees are missing.",
                evidence={"missing": missing},
            )

        return AssemblyInvariant(
            invariant_id="assembly.artifacts_exist",
            status=AssemblyInvariantStatus.PASS,
            severity=AssemblyInvariantSeverity.INFO,
            message="All collected artifact records exist.",
            evidence={"artifact_count": len(artifacts)},
        )

    def _invariant_no_lifeline_artifacts(self, artifacts: list[AssemblyArtifact]) -> AssemblyInvariant:
        source_artifacts = {
            item.relative_path
            for item in artifacts
            if item.kind == AssemblyArtifactKind.SOURCE
        }
        touched_lifelines = sorted(source_artifacts & self.LIFELINE_FILES)

        if touched_lifelines:
            return AssemblyInvariant(
                invariant_id="assembly.no_lifeline_source_artifacts",
                status=AssemblyInvariantStatus.FAIL,
                severity=AssemblyInvariantSeverity.CRITICAL,
                message="Assembly source inventory contains Hermes lifeline files.",
                evidence={"lifelines": touched_lifelines},
            )

        return AssemblyInvariant(
            invariant_id="assembly.no_lifeline_source_artifacts",
            status=AssemblyInvariantStatus.PASS,
            severity=AssemblyInvariantSeverity.CRITICAL,
            message="Assembly source inventory contains only hermes_ext sources, not Hermes lifeline files.",
            evidence={"lifeline_count": 0},
        )

    def _invariant_feature_flags_default_disabled(self) -> AssemblyInvariant:
        flags = FeatureFlagSet.default()
        enabled = [
            name.value
            for name in ExtensionFlagName
            if flags.is_enabled(name)
        ]

        if enabled:
            return AssemblyInvariant(
                invariant_id="assembly.feature_flags_default_disabled",
                status=AssemblyInvariantStatus.FAIL,
                severity=AssemblyInvariantSeverity.CRITICAL,
                message="Feature flags are not effectively disabled by default.",
                evidence={"enabled": enabled},
            )

        return AssemblyInvariant(
            invariant_id="assembly.feature_flags_default_disabled",
            status=AssemblyInvariantStatus.PASS,
            severity=AssemblyInvariantSeverity.CRITICAL,
            message="All extension feature flags are effectively disabled by default.",
            evidence={"enabled": []},
        )

    def _invariant_no_forbidden_imports(self) -> AssemblyInvariant:
        root = self.config.project_root / "hermes_ext"
        violations: list[dict[str, Any]] = []

        if not root.exists():
            return AssemblyInvariant(
                invariant_id="assembly.no_forbidden_imports",
                status=AssemblyInvariantStatus.FAIL,
                severity=AssemblyInvariantSeverity.CRITICAL,
                message="hermes_ext source tree is missing.",
                evidence={"root": str(root)},
            )

        for path in root.rglob("*.py"):
            if "__pycache__" in path.parts:
                continue
            relative = path.relative_to(self.config.project_root).as_posix()
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
            except SyntaxError as exc:
                violations.append({"path": relative, "kind": "syntax_error", "error": str(exc)})
                continue

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if self._is_forbidden(alias.name):
                            violations.append(
                                {"path": relative, "module": alias.name, "line": getattr(node, "lineno", 0)}
                            )

                if isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    if self._is_forbidden(module):
                        violations.append(
                            {"path": relative, "module": module, "line": getattr(node, "lineno", 0)}
                        )

        if violations:
            return AssemblyInvariant(
                invariant_id="assembly.no_forbidden_imports",
                status=AssemblyInvariantStatus.FAIL,
                severity=AssemblyInvariantSeverity.CRITICAL,
                message="Forbidden imports detected in hermes_ext.",
                evidence={"violations": violations[:100], "violation_count": len(violations)},
            )

        return AssemblyInvariant(
            invariant_id="assembly.no_forbidden_imports",
            status=AssemblyInvariantStatus.PASS,
            severity=AssemblyInvariantSeverity.CRITICAL,
            message="No forbidden Hermes core/model SDK imports detected in hermes_ext.",
            evidence={"violation_count": 0},
        )

    def _invariant_phase10_golden_trace(self) -> AssemblyInvariant:
        path = self.config.project_root / "reports/phase10/golden_trace_replay_report.json"

        if not path.exists():
            status = AssemblyInvariantStatus.FAIL if self.config.require_phase10_golden_trace else AssemblyInvariantStatus.WARN
            return AssemblyInvariant(
                invariant_id="assembly.phase10_golden_trace_stable",
                status=status,
                severity=AssemblyInvariantSeverity.CRITICAL if status == AssemblyInvariantStatus.FAIL else AssemblyInvariantSeverity.WARNING,
                message="Phase 10 golden trace JSON report is missing.",
                evidence={"path": path.as_posix()},
            )

        data = self._read_json(path)
        ok = bool(data.get("ok")) is True
        case_count = int(data.get("case_count", 0))
        stable_cases = int(data.get("stable_cases", -1))
        unstable_cases = int(data.get("unstable_cases", -1))
        failed = int(data.get("failed", -1))
        violations = data.get("violations", [])

        if ok and case_count == stable_cases and unstable_cases == 0 and failed == 0 and not violations:
            return AssemblyInvariant(
                invariant_id="assembly.phase10_golden_trace_stable",
                status=AssemblyInvariantStatus.PASS,
                severity=AssemblyInvariantSeverity.CRITICAL,
                message="Phase 10 golden trace replay is stable.",
                evidence={
                    "case_count": case_count,
                    "stable_cases": stable_cases,
                    "unstable_cases": unstable_cases,
                    "failed": failed,
                    "violations": len(violations),
                },
            )

        return AssemblyInvariant(
            invariant_id="assembly.phase10_golden_trace_stable",
            status=AssemblyInvariantStatus.FAIL,
            severity=AssemblyInvariantSeverity.CRITICAL,
            message="Phase 10 golden trace replay is not clean.",
            evidence={
                "ok": ok,
                "case_count": case_count,
                "stable_cases": stable_cases,
                "unstable_cases": unstable_cases,
                "failed": failed,
                "violations": violations,
            },
        )

    def _invariant_phase9_native_boundary(self) -> AssemblyInvariant:
        path = self.config.project_root / "reports/phase9/native_boundary_contract_report.json"

        if not path.exists():
            status = AssemblyInvariantStatus.FAIL if self.config.require_phase9_native_boundary else AssemblyInvariantStatus.WARN
            return AssemblyInvariant(
                invariant_id="assembly.phase9_native_boundary_no_side_effects",
                status=status,
                severity=AssemblyInvariantSeverity.CRITICAL if status == AssemblyInvariantStatus.FAIL else AssemblyInvariantSeverity.WARNING,
                message="Phase 9 native boundary JSON report is missing.",
                evidence={"path": path.as_posix()},
            )

        data = self._read_json(path)
        results = data.get("results", [])
        side_effect_fields = [
            "native_called",
            "tool_executed",
            "provider_called",
            "memory_written",
            "state_mutated",
            "patch_generated",
            "secret_read",
        ]

        side_effect_counts = {
            field: sum(1 for item in results if isinstance(item, dict) and bool(item.get(field)))
            for field in side_effect_fields
        }

        ok = bool(data.get("ok")) is True
        failed = int(data.get("failed", -1))
        violations = data.get("violations", [])
        has_side_effects = any(count > 0 for count in side_effect_counts.values())

        if ok and failed == 0 and not violations and not has_side_effects:
            return AssemblyInvariant(
                invariant_id="assembly.phase9_native_boundary_no_side_effects",
                status=AssemblyInvariantStatus.PASS,
                severity=AssemblyInvariantSeverity.CRITICAL,
                message="Phase 9 no-op native boundary report has no side effects.",
                evidence={
                    "failed": failed,
                    "violations": len(violations),
                    "side_effect_counts": side_effect_counts,
                },
            )

        return AssemblyInvariant(
            invariant_id="assembly.phase9_native_boundary_no_side_effects",
            status=AssemblyInvariantStatus.FAIL,
            severity=AssemblyInvariantSeverity.CRITICAL,
            message="Phase 9 native boundary report contains failures, violations, or side effects.",
            evidence={
                "ok": ok,
                "failed": failed,
                "violations": violations,
                "side_effect_counts": side_effect_counts,
            },
        )

    def _is_forbidden(self, module: str) -> bool:
        return any(
            module == prefix or module.startswith(prefix + ".")
            for prefix in self.FORBIDDEN_IMPORT_PREFIXES
        )

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"expected JSON object: {path}")
        return data
