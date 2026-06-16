from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.adapter_scan.cli import main


def test_adapter_scan_cli_writes_markdown(tmp_path: Path) -> None:
    (tmp_path / "cli.py").write_text("def main():\n    pass\n", encoding="utf-8")
    output = tmp_path / "report.md"

    exit_code = main(
        [
            "--project-root",
            str(tmp_path),
            "--format",
            "markdown",
            "--output",
            str(output),
        ]
    )

    assert exit_code == 0
    assert output.exists()
    assert "# Hermes Adapter Scan Report" in output.read_text(encoding="utf-8")


def test_adapter_scan_cli_writes_json(tmp_path: Path) -> None:
    (tmp_path / "cli.py").write_text("def main():\n    pass\n", encoding="utf-8")
    output = tmp_path / "report.json"

    exit_code = main(
        [
            "--project-root",
            str(tmp_path),
            "--format",
            "json",
            "--output",
            str(output),
        ]
    )

    data = json.loads(output.read_text(encoding="utf-8"))

    assert exit_code == 0
    assert "summary" in data
    assert data["summary"]["files_scanned"] == 1


def test_adapter_scan_cli_returns_nonzero_on_parse_error(tmp_path: Path) -> None:
    (tmp_path / "broken.py").write_text("def broken(:\n", encoding="utf-8")

    exit_code = main(["--project-root", str(tmp_path)])

    assert exit_code == 1