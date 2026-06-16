from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.native_boundary.cli import main


def test_native_boundary_cli_writes_markdown(tmp_path: Path) -> None:
    output = tmp_path / "report.md"

    exit_code = main(
        [
            "--format",
            "markdown",
            "--output",
            str(output),
        ]
    )

    assert exit_code == 0
    assert output.exists()
    assert "No-op Native Boundary Contract Report" in output.read_text(encoding="utf-8")


def test_native_boundary_cli_writes_json(tmp_path: Path) -> None:
    output = tmp_path / "report.json"

    exit_code = main(
        [
            "--format",
            "json",
            "--output",
            str(output),
        ]
    )

    data = json.loads(output.read_text(encoding="utf-8"))

    assert exit_code == 0
    assert data["ok"] is True
    assert data["case_count"] >= 7