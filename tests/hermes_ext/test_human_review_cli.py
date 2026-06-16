import json
from pathlib import Path

from hermes_ext.human_review.cli import main


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(root: Path, relative: str, payload: dict) -> None:
    _write(root, relative, json.dumps(payload))


def _write_clean_phase12_evidence(root: Path) -> None:
    _write_json(
        root,
        "reports/phase12/merge_readiness_report.json",
        {
            "ok": True,
            "passed": 8,
            "warned": 0,
            "failed": 0,
            "interpretation": "does not approve native integration rollback_index_present",
        },
    )
    _write_json(
        root,
        "reports/phase12/final_documentation_pack.json",
        {"note": "does not approve native integration"},
    )
    _write_json(root, "reports/phase12/final_stabilization_bundle.json", {})
    _write(root, "reports/phase12/phase12_test_result.md", "总通过 | 254\n失败 | 0\n禁止 import")
    _write(
        root,
        "reports/phase12/phase12_exit_checklist.md",
        "未修改 Hermes 生命线文件\n未调用真实模型\n未调用真实 provider\n未执行真实工具\n未写 Hermes native memory\n未生成 patch",
    )
    _write(
        root,
        "reports/phase12/maintenance_guide.md",
        "no-import\nkill-switch\nshadow-only\nno-op by default\nlifeline files",
    )
    _write(root, "reports/phase12/rollback_index.md", "git reset --hard tag")


def test_cli_returns_zero_for_pending_review(tmp_path):
    _write_clean_phase12_evidence(tmp_path)
    output_dir = tmp_path / "reports/phase13"

    code = main(
        [
            "--project-root",
            str(tmp_path),
            "--output-dir",
            str(output_dir),
        ]
    )

    assert code == 0
    assert (output_dir / "phase13_review_bundle.json").exists()


def test_cli_returns_nonzero_for_approve_without_ack(tmp_path):
    _write_clean_phase12_evidence(tmp_path)
    output_dir = tmp_path / "reports/phase13"

    code = main(
        [
            "--project-root",
            str(tmp_path),
            "--output-dir",
            str(output_dir),
            "--decision",
            "approve_shadow_merge",
        ]
    )

    assert code == 2
    assert (output_dir / "merge_decision_report.json").exists()


def test_cli_allows_approve_with_required_ack(tmp_path):
    _write_clean_phase12_evidence(tmp_path)
    output_dir = tmp_path / "reports/phase13"

    code = main(
        [
            "--project-root",
            str(tmp_path),
            "--output-dir",
            str(output_dir),
            "--decision",
            "approve_shadow_merge",
            "--reviewer",
            "reviewer@example.com",
            "--ack",
            "ack_shadow_only",
            "--ack",
            "ack_no_native_integration",
            "--ack",
            "ack_rollback_anchor",
            "--ack",
            "ack_human_review_complete",
        ]
    )

    assert code == 0


def test_cli_returns_nonzero_for_missing_evidence(tmp_path):
    output_dir = tmp_path / "reports/phase13"

    code = main(
        [
            "--project-root",
            str(tmp_path),
            "--output-dir",
            str(output_dir),
        ]
    )

    assert code == 2
    assert (output_dir / "merge_decision_report.json").exists()