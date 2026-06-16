from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.finalization.cli import main


def create_clean_evidence(root: Path) -> None:
    (root / "reports" / "phase11").mkdir(parents=True)
    (root / "reports" / "phase11" / "release_gate_report.json").write_text(
        json.dumps({"ok": True, "blocking_failures": [], "warnings": []}),
        encoding="utf-8",
    )
    (root / "reports" / "phase11" / "shadow_assembly_manifest.json").write_text(
        json.dumps(
            {
                "manifest_hash": "a" * 64,
                "summary": {
                    "invariants_passed": 6,
                    "invariants_warned": 0,
                    "invariants_failed": 0,
                },
                "invariants": [],
            }
        ),
        encoding="utf-8",
    )
    (root / "reports" / "phase11" / "phase11_test_result.md").write_text(
        "总通过 | 241\n失败 | 0\n",
        encoding="utf-8",
    )
    (root / "reports" / "phase11" / "phase11_exit_checklist.md").write_text(
        "未修改 Hermes 生命线文件\n未修改 Hermes CLI 入口\n未修改 pyproject.toml\n未修改 lock 文件\n未安装新依赖\nrelease_gate ok=true\n回滚\n",
        encoding="utf-8",
    )
    (root / "reports" / "phase11" / "phase11_execution_log.md").write_text("log\n", encoding="utf-8")

    (root / "reports" / "phase10").mkdir(parents=True)
    (root / "reports" / "phase10" / "golden_trace_replay_report.json").write_text(
        json.dumps({"ok": True, "case_count": 5, "stable_cases": 5, "unstable_cases": 0, "failed": 0, "violations": []}),
        encoding="utf-8",
    )
    (root / "reports" / "phase9").mkdir(parents=True)
    (root / "reports" / "phase9" / "native_boundary_contract_report.json").write_text(
        json.dumps({"ok": True, "failed": 0, "violations": [], "results": []}),
        encoding="utf-8",
    )


def test_finalization_cli_writes_all_outputs(tmp_path: Path) -> None:
    create_clean_evidence(tmp_path)
    output_dir = tmp_path / "reports" / "phase12"

    exit_code = main(
        [
            "--project-root",
            str(tmp_path),
            "--output-dir",
            str(output_dir),
        ]
    )

    assert exit_code == 0
    assert (output_dir / "final_documentation_pack.md").exists()
    assert (output_dir / "final_documentation_pack.json").exists()
    assert (output_dir / "merge_readiness_report.md").exists()
    assert (output_dir / "merge_readiness_report.json").exists()
    assert (output_dir / "rollback_index.md").exists()
    assert (output_dir / "maintenance_guide.md").exists()
    assert (output_dir / "final_stabilization_bundle.json").exists()

    readiness = json.loads((output_dir / "merge_readiness_report.json").read_text(encoding="utf-8"))
    assert readiness["ok"] is True