from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.finalization.contracts import FinalizationConfig
from hermes_ext.finalization.evidence_loader import FinalizationEvidenceLoader


def test_evidence_loader_loads_json_and_markdown(tmp_path: Path) -> None:
    (tmp_path / "reports" / "phase11").mkdir(parents=True)
    (tmp_path / "reports" / "phase11" / "shadow_assembly_manifest.json").write_text(
        json.dumps({"manifest_hash": "x", "summary": {"invariants_failed": 0}}),
        encoding="utf-8",
    )
    (tmp_path / "reports" / "phase11" / "release_gate_report.json").write_text(
        json.dumps({"ok": True, "blocking_failures": [], "warnings": []}),
        encoding="utf-8",
    )
    (tmp_path / "reports" / "phase11" / "phase11_test_result.md").write_text(
        "总通过 | 241\n失败 | 0\n",
        encoding="utf-8",
    )
    (tmp_path / "reports" / "phase11" / "phase11_exit_checklist.md").write_text(
        "回滚\n",
        encoding="utf-8",
    )
    (tmp_path / "reports" / "phase11" / "phase11_execution_log.md").write_text(
        "log\n",
        encoding="utf-8",
    )
    (tmp_path / "reports" / "phase10").mkdir(parents=True)
    (tmp_path / "reports" / "phase10" / "golden_trace_replay_report.json").write_text(
        json.dumps({"ok": True}),
        encoding="utf-8",
    )
    (tmp_path / "reports" / "phase9").mkdir(parents=True)
    (tmp_path / "reports" / "phase9" / "native_boundary_contract_report.json").write_text(
        json.dumps({"ok": True}),
        encoding="utf-8",
    )

    evidence = FinalizationEvidenceLoader(
        FinalizationConfig(project_root=tmp_path, output_dir=tmp_path / "out")
    ).load()

    assert len(evidence) == 7
    assert all(item.exists for item in evidence)
    assert any(item.json_payload for item in evidence)


def test_evidence_loader_records_missing_files(tmp_path: Path) -> None:
    evidence = FinalizationEvidenceLoader(
        FinalizationConfig(project_root=tmp_path, output_dir=tmp_path / "out")
    ).load()

    assert len(evidence) == 7
    assert any(not item.exists for item in evidence)