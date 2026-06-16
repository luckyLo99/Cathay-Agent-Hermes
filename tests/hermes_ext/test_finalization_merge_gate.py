from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.finalization.contracts import FinalizationConfig
from hermes_ext.finalization.evidence_loader import FinalizationEvidenceLoader
from hermes_ext.finalization.merge_gate import MergeReadinessGate


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
        json.dumps(
            {
                "ok": True,
                "case_count": 5,
                "stable_cases": 5,
                "unstable_cases": 0,
                "failed": 0,
                "violations": [],
            }
        ),
        encoding="utf-8",
    )

    (root / "reports" / "phase9").mkdir(parents=True)
    (root / "reports" / "phase9" / "native_boundary_contract_report.json").write_text(
        json.dumps(
            {
                "ok": True,
                "failed": 0,
                "violations": [],
                "results": [
                    {
                        "native_called": False,
                        "tool_executed": False,
                        "provider_called": False,
                        "memory_written": False,
                        "state_mutated": False,
                        "patch_generated": False,
                        "secret_read": False,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


def test_merge_readiness_gate_passes_clean_evidence(tmp_path: Path) -> None:
    create_clean_evidence(tmp_path)
    config = FinalizationConfig(project_root=tmp_path, output_dir=tmp_path / "out")
    evidence = FinalizationEvidenceLoader(config).load()

    report = MergeReadinessGate(config).evaluate(evidence)

    assert report.ok
    assert report.failed == 0
    assert report.readiness_hash


def test_merge_readiness_gate_fails_bad_release_gate(tmp_path: Path) -> None:
    create_clean_evidence(tmp_path)
    (tmp_path / "reports" / "phase11" / "release_gate_report.json").write_text(
        json.dumps({"ok": False, "blocking_failures": [{"x": 1}], "warnings": []}),
        encoding="utf-8",
    )

    config = FinalizationConfig(project_root=tmp_path, output_dir=tmp_path / "out")
    evidence = FinalizationEvidenceLoader(config).load()
    report = MergeReadinessGate(config).evaluate(evidence)

    assert not report.ok
    assert report.failed >= 1