from __future__ import annotations

from pathlib import Path

from hermes_ext.adapter_scan.contracts import AdapterIntegrationPosture, AdapterScanConfig
from hermes_ext.adapter_scan.scanner import AdapterScanEngine


def test_adapter_scan_engine_runs_read_only(tmp_path: Path) -> None:
    (tmp_path / "cli.py").write_text("def main():\n    pass\n", encoding="utf-8")
    (tmp_path / "providers").mkdir()
    (tmp_path / "providers" / "__init__.py").write_text(
        "class ProviderRegistry:\n    pass\n",
        encoding="utf-8",
    )
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "ignored.py").write_text("x = 1\n", encoding="utf-8")

    report = AdapterScanEngine(AdapterScanConfig(project_root=tmp_path)).run()

    assert report.summary.files_scanned == 2
    assert report.summary.candidates_found >= 1
    assert any(candidate.relative_path == "cli.py" for candidate in report.candidates)
    assert any(candidate.posture == AdapterIntegrationPosture.FORBIDDEN for candidate in report.candidates)


def test_adapter_scan_engine_records_parse_errors(tmp_path: Path) -> None:
    (tmp_path / "broken.py").write_text("def broken(:\n", encoding="utf-8")

    report = AdapterScanEngine(AdapterScanConfig(project_root=tmp_path)).run()

    assert report.summary.parse_errors == 1