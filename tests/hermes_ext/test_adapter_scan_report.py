from __future__ import annotations

from pathlib import Path

from hermes_ext.adapter_scan.contracts import AdapterScanConfig
from hermes_ext.adapter_scan.report import AdapterScanReporter
from hermes_ext.adapter_scan.scanner import AdapterScanEngine


def test_adapter_scan_reporter_renders_markdown_and_json(tmp_path: Path) -> None:
    (tmp_path / "cli.py").write_text("def main():\n    pass\n", encoding="utf-8")

    report = AdapterScanEngine(AdapterScanConfig(project_root=tmp_path)).run()
    renderer = AdapterScanReporter()

    markdown = renderer.render_markdown(report)
    json_text = renderer.render_json(report)

    assert "# Hermes Adapter Scan Report" in markdown
    assert "Extension Point Candidates" in markdown
    assert '"summary"' in json_text