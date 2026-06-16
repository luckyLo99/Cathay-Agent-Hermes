from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.golden_trace.cli import main


def test_golden_trace_cli_writes_markdown(tmp_path: Path) -> None:
    output = tmp_path / "golden.md"

    exit_code = main(
        [
            "--project-root",
            ".",
            "--state-dir",
            str(tmp_path / "state"),
            "--repeat",
            "1",
            "--native-boundary-limit",
            "5",
            "--format",
            "markdown",
            "--output",
            str(output),
        ]
    )

    assert exit_code == 0
    assert output.exists()
    assert "Golden Trace Replay Report" in output.read_text(encoding="utf-8")


def test_golden_trace_cli_writes_json(tmp_path: Path) -> None:
    output = tmp_path / "golden.json"

    exit_code = main(
        [
            "--project-root",
            ".",
            "--state-dir",
            str(tmp_path / "state"),
            "--repeat",
            "1",
            "--native-boundary-limit",
            "5",
            "--format",
            "json",
            "--output",
            str(output),
        ]
    )

    data = json.loads(output.read_text(encoding="utf-8"))

    assert exit_code == 0
    assert data["ok"] is True
    assert data["case_count"] >= 5