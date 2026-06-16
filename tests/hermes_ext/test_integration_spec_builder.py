from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterScanReport,
    AdapterScanSummary,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
)
from hermes_ext.integration_spec.contracts import IntegrationMode, IntegrationSpecConfig
from hermes_ext.integration_spec.spec_builder import IntegrationSpecBuilder


def make_scan_json(tmp_path: Path) -> Path:
    report = AdapterScanReport(
        project_root=str(tmp_path),
        summary=AdapterScanSummary(candidates_found=2),
        candidates=[
            ExtensionPointCandidate(
                candidate_id="cli",
                relative_path="cli.py",
                surface=AdapterSurfaceKind.CLI,
                posture=AdapterIntegrationPosture.FORBIDDEN,
                risk=RiskLevel.CRITICAL,
                reason="lifeline",
                future_adapter_hint="do not patch",
            ).stable_id(),
            ExtensionPointCandidate(
                candidate_id="tool",
                relative_path="agent/tool_executor.py",
                surface=AdapterSurfaceKind.TOOL_REGISTRY,
                posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
                risk=RiskLevel.HIGH,
                reason="tool",
                future_adapter_hint="flag",
            ).stable_id(),
        ],
    )
    path = tmp_path / "scan.json"
    path.write_text(json.dumps(report.model_dump(mode="json")), encoding="utf-8")
    return path


def test_spec_builder_builds_from_scan_json(tmp_path: Path) -> None:
    scan_json = make_scan_json(tmp_path)
    spec = IntegrationSpecBuilder(
        IntegrationSpecConfig(project_root=tmp_path, phase7_scan_json=scan_json)
    ).build_from_scan_json()

    assert spec.spec_hash
    assert len(spec.matrix.entries) == 2
    assert spec.matrix.count_by_mode(IntegrationMode.FORBIDDEN) == 1
    assert spec.matrix.count_by_mode(IntegrationMode.FEATURE_FLAG_SHADOW) == 1


def test_spec_builder_can_exclude_forbidden(tmp_path: Path) -> None:
    scan_json = make_scan_json(tmp_path)
    spec = IntegrationSpecBuilder(
        IntegrationSpecConfig(
            project_root=tmp_path,
            phase7_scan_json=scan_json,
            allow_forbidden_entries=False,
        )
    ).build_from_scan_json()

    assert len(spec.matrix.entries) == 1
    assert spec.matrix.entries[0].integration_mode == IntegrationMode.FEATURE_FLAG_SHADOW