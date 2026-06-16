from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.assembly.cli import main


def create_reports(root: Path) -> None:
    (root / "reports" / "phase10").mkdir(parents=True)
    (root / "reports" / "phase10" / "golden_trace_replay_report.json").write_text(
        json.dumps({"ok": True, "case_count": 1, "stable_cases": 1, "unstable_cases": 0, "failed": 0, "violations": []}),
        encoding="utf-8",
    )
    (root / "reports" / "phase9").mkdir(parents=True)
    (root / "reports" / "phase9" / "native_boundary_contract_report.json").write_text(
        json.dumps({"ok": True, "failed": 0, "violations": [], "results": []}),
        encoding="utf-8",
    )


def test_assembly_cli_writes_outputs(tmp_path: Path) -> None:
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "x.py").write_text("x = 1\n", encoding="utf-8")
    create_reports(tmp_path)

    manifest_md = tmp_path / "manifest.md"
    manifest_json = tmp_path / "manifest.json"
    gate_md = tmp_path / "gate.md"
    gate_json = tmp_path / "gate.json"

    exit_code = main(
        [
            "--project-root",
            str(tmp_path),
            "--manifest-md",
            str(manifest_md),
            "--manifest-json",
            str(manifest_json),
            "--gate-md",
            str(gate_md),
            "--gate-json",
            str(gate_json),
        ]
    )

    assert exit_code == 0
    assert manifest_md.exists()
    assert manifest_json.exists()
    assert gate_md.exists()
    assert gate_json.exists()
    assert json.loads(gate_json.read_text(encoding="utf-8"))["ok"] is True


def test_assembly_cli_can_allow_missing_phase_reports(tmp_path: Path) -> None:
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "x.py").write_text("x = 1\n", encoding="utf-8")

    exit_code = main(
        [
            "--project-root",
            str(tmp_path),
            "--manifest-md",
            str(tmp_path / "manifest.md"),
            "--manifest-json",
            str(tmp_path / "manifest.json"),
            "--gate-md",
            str(tmp_path / "gate.md"),
            "--gate-json",
            str(tmp_path / "gate.json"),
            "--allow-missing-phase-reports",
        ]
    )

    assert exit_code == 0