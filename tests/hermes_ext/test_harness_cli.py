from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.harness.cli import main


def test_harness_cli_doctor_json(tmp_path: Path, capsys) -> None:
    exit_code = main(
        [
            "doctor",
            "--project-root",
            ".",
            "--state-dir",
            str(tmp_path),
            "--json",
        ]
    )

    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert exit_code == 0
    assert data["ok"] is True
    assert data["mode"] == "diagnostic"


def test_harness_cli_shadow_run_requires_flag(tmp_path: Path, capsys) -> None:
    exit_code = main(
        [
            "shadow-run",
            "--project-root",
            ".",
            "--state-dir",
            str(tmp_path),
            "--text",
            "hello",
            "--json",
        ]
    )

    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert exit_code == 1
    assert data["ok"] is False
    assert "shadow_runner flag" in data["error"]


def test_harness_cli_shadow_run_with_flags_json(tmp_path: Path, capsys) -> None:
    flags_path = tmp_path / "flags.json"
    flags_path.write_text(
        json.dumps(
            {
                "enabled": True,
                "shadow_runner": True,
                "cathay": False,
                "memoryx": False,
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(
        [
            "shadow-run",
            "--project-root",
            ".",
            "--state-dir",
            str(tmp_path / "state"),
            "--flags-json",
            str(flags_path),
            "--text",
            "Phase 6 CLI shadow run",
            "--json",
        ]
    )

    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert exit_code == 0
    assert data["ok"] is True
    assert data["shadow_result"]["status"] == "completed"