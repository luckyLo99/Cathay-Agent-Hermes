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
from hermes_ext.integration_spec.cli import main


def write_scan_json(tmp_path: Path) -> Path:
    report = AdapterScanReport(
        project_root=str(tmp_path),
        summary=AdapterScanSummary(candidates_found=1),
        candidates=[
            ExtensionPointCandidate(
                relative_path="agent/tool_executor.py",
                surface=AdapterSurfaceKind.TOOL_REGISTRY,
                posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
                risk=RiskLevel.HIGH,
                reason="tool",
                future_adapter_hint="flag",
            ).stable_id()
        ],
    )
    path = tmp_path / "scan.json"
    path.write_text(json.dumps(report.model_dump(mode="json")), encoding="utf-8")
    return path


def test_integration_spec_cli_writes_markdown(tmp_path: Path) -> None:
    scan_json = write_scan_json(tmp_path)
    output = tmp_path / "spec.md"

    exit_code = main(
        [
            "--project-root",
            str(tmp_path),
            "--scan-json",
            str(scan_json),
            "--format",
            "markdown",
            "--output",
            str(output),
        ]
    )

    assert exit_code == 0
    assert output.exists()
    assert "Zero-touch Hermes Integration Spec" in output.read_text(encoding="utf-8")


def test_integration_spec_cli_writes_json(tmp_path: Path) -> None:
    scan_json = write_scan_json(tmp_path)
    output = tmp_path / "spec.json"

    exit_code = main(
        [
            "--project-root",
            str(tmp_path),
            "--scan-json",
            str(scan_json),
            "--format",
            "json",
            "--output",
            str(output),
        ]
    )

    data = json.loads(output.read_text(encoding="utf-8"))

    assert exit_code == 0
    assert data["phase"] == 8
    assert data["matrix"]["entries"]