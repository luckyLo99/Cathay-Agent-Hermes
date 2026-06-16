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
from hermes_ext.integration_spec.report import IntegrationSpecReporter
from hermes_ext.integration_spec.spec_builder import build_spec_from_report_dict


def test_integration_spec_reporter_renders_markdown_and_json(tmp_path: Path) -> None:
    report = AdapterScanReport(
        project_root=str(tmp_path),
        summary=AdapterScanSummary(candidates_found=1),
        candidates=[
            ExtensionPointCandidate(
                relative_path="cli.py",
                surface=AdapterSurfaceKind.CLI,
                posture=AdapterIntegrationPosture.FORBIDDEN,
                risk=RiskLevel.CRITICAL,
                reason="lifeline",
                future_adapter_hint="do not patch",
            ).stable_id()
        ],
    )
    spec = build_spec_from_report_dict(tmp_path, report.model_dump(mode="json"))

    markdown = IntegrationSpecReporter().render_markdown(spec)
    json_text = IntegrationSpecReporter().render_json(spec)
    parsed = json.loads(json_text)

    assert "# Zero-touch Hermes Integration Spec" in markdown
    assert "Non-negotiable Rule" in markdown
    assert parsed["spec_hash"]