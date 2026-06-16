import json
from pathlib import Path

from hermes_ext.human_review.evidence_loader import HumanReviewEvidenceLoader


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(root: Path, relative: str, payload: dict) -> None:
    _write(root, relative, json.dumps(payload))


def _write_phase12_evidence(root: Path) -> None:
    _write_json(
        root,
        "reports/phase12/merge_readiness_report.json",
        {"ok": True, "passed": 8, "warned": 0, "failed": 0},
    )
    _write_json(
        root,
        "reports/phase12/final_documentation_pack.json",
        {"summary": "does not approve native integration"},
    )
    _write_json(
        root,
        "reports/phase12/final_stabilization_bundle.json",
        {"bundle_hash": "abc"},
    )
    _write(
        root,
        "reports/phase12/phase12_test_result.md",
        "总通过 | 254\n失败 | 0\n禁止 import Hermes core",
    )
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
    _write(
        root,
        "reports/phase12/rollback_index.md",
        "git reset --hard phase11-shadow-assembly-manifest",
    )


def test_loader_loads_all_required_phase12_evidence(tmp_path):
    _write_phase12_evidence(tmp_path)

    evidence = HumanReviewEvidenceLoader(tmp_path).load()

    assert evidence.missing_required_names == ()
    assert evidence.invalid_required_names == ()
    assert evidence.document("phase12_merge_readiness_report").json_data["ok"] is True


def test_loader_reports_missing_files(tmp_path):
    evidence = HumanReviewEvidenceLoader(tmp_path).load()

    assert "phase12_merge_readiness_report" in evidence.missing_required_names
    assert "phase12_rollback_index" in evidence.missing_required_names


def test_loader_reports_invalid_json(tmp_path):
    _write_phase12_evidence(tmp_path)
    _write(tmp_path, "reports/phase12/merge_readiness_report.json", "{bad json")

    evidence = HumanReviewEvidenceLoader(tmp_path).load()

    assert "phase12_merge_readiness_report" in evidence.invalid_required_names