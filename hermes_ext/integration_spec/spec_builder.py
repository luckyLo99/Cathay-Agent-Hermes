from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from hermes_ext.adapter_scan.contracts import AdapterScanReport, ExtensionPointCandidate
from hermes_ext.integration_spec.contracts import (
    IntegrationConstraint,
    IntegrationSpecConfig,
    RiskLevel,
    ZeroTouchIntegrationSpec,
    candidate_from_dict,
)
from hermes_ext.integration_spec.matrix_builder import IntegrationMatrixBuilder


class IntegrationSpecBuilder:
    """
    Builds a zero-touch integration spec from Phase 7 adapter scan JSON.

    It consumes scan output only. It does not scan Hermes again and does not patch.
    """

    def __init__(self, config: IntegrationSpecConfig) -> None:
        self.config = config
        self.matrix_builder = IntegrationMatrixBuilder()

    def build_from_scan_json(self) -> ZeroTouchIntegrationSpec:
        data = self._read_json(self.config.phase7_scan_json)
        scan_report = AdapterScanReport.model_validate(data, strict=False)
        candidates = self._load_candidates(scan_report)

        matrix = self.matrix_builder.build(candidates)

        warnings: list[str] = []
        if matrix.count_by_mode(mode=self._integration_mode_forbidden()) > 0:
            warnings.append("Spec contains forbidden entries; these are blocked and design-only.")
        if len(matrix.entries) > self.config.max_entries:
            warnings.append("Spec entries exceeded max_entries and were truncated.")

        spec = ZeroTouchIntegrationSpec(
            project_root=str(self.config.project_root),
            source_scan_report_id=scan_report.report_id,
            matrix=matrix,
            global_constraints=self._global_constraints(),
            warnings=warnings,
        ).with_hash()

        return spec

    def _load_candidates(self, scan_report: AdapterScanReport) -> list[ExtensionPointCandidate]:
        candidates = scan_report.candidates[: self.config.max_entries]
        if not self.config.allow_forbidden_entries:
            candidates = [
                candidate
                for candidate in candidates
                if candidate.posture.value != "forbidden"
            ]
        return candidates

    def _read_json(self, path: Path) -> dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Phase 7 scan JSON not found: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Phase 7 scan JSON must be an object")
        return data

    def _global_constraints(self) -> list[IntegrationConstraint]:
        return [
            IntegrationConstraint(
                rule_id="global.no_hermes_core_patch",
                description="Phase 8 must not modify Hermes core files.",
                severity=RiskLevel.CRITICAL,
            ),
            IntegrationConstraint(
                rule_id="global.no_patch_generation",
                description="Phase 8 must not generate source patches.",
                severity=RiskLevel.CRITICAL,
            ),
            IntegrationConstraint(
                rule_id="global.feature_flag_first",
                description="Future runnable integration must be gated by HERMES_EXT_* feature flags.",
                severity=RiskLevel.HIGH,
            ),
            IntegrationConstraint(
                rule_id="global.kill_switch_required",
                description="Any future integration must honor HERMES_EXT_KILL_SWITCH.",
                severity=RiskLevel.CRITICAL,
            ),
            IntegrationConstraint(
                rule_id="global.shadow_before_native",
                description="Shadow harness validation must precede any native Hermes integration.",
                severity=RiskLevel.CRITICAL,
            ),
        ]

    @staticmethod
    def _integration_mode_forbidden():
        from hermes_ext.integration_spec.contracts import IntegrationMode

        return IntegrationMode.FORBIDDEN


def build_spec_from_report_dict(
    project_root: Path,
    report_dict: dict[str, Any],
) -> ZeroTouchIntegrationSpec:
    """
    Convenience function for tests and in-memory use.
    """
    scan_report = AdapterScanReport.model_validate(report_dict, strict=False)
    candidates = [candidate_from_dict(item.model_dump(mode="json")) for item in scan_report.candidates]
    matrix = IntegrationMatrixBuilder().build(candidates)
    return ZeroTouchIntegrationSpec(
        project_root=str(project_root.resolve()),
        source_scan_report_id=scan_report.report_id,
        matrix=matrix,
        global_constraints=[
            IntegrationConstraint(
                rule_id="global.no_hermes_core_patch",
                description="Phase 8 must not modify Hermes core files.",
                severity=RiskLevel.CRITICAL,
            )
        ],
    ).with_hash()