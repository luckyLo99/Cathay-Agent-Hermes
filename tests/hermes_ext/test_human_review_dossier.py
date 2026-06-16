import json
from pathlib import Path

from hermes_ext.human_review.dossier import (
    ColdStartValidationPlanBuilder,
    HumanReviewDossierBuilder,
)
from hermes_ext.human_review.evidence_loader import HumanReviewEvidenceLoader


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(root: Path, relative: str, payload: dict) -> None:
    _write(root, relative, json.dumps(payload))


def _write_phase12_evidence(root: Path) -> None:
    _write_json(root, "reports/phase12/merge_readiness_report.json", {"ok": True})
    _write_json(
        root,
        "reports/phase12/final_documentation_pack.json",
        {"summary": "does not approve native integration"},
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


def test_dossier_contains_required_sections(tmp_path):
    _write_phase12_evidence(tmp_path)
    evidence = HumanReviewEvidenceLoader(tmp_path).load()

    dossier = HumanReviewDossierBuilder().build(evidence)

    assert dossier.phase == 13
    assert "executive_summary" in dossier.sections
    assert "native integration" in dossier.sections["executive_summary"]
    assert "risk_register" in dossier.sections
    assert dossier.source_evidence


def test_cold_start_plan_contains_forbidden_actions():
    plan = ColdStartValidationPlanBuilder().build()

    assert plan.phase == 13
    assert any("Do not call real providers" in item for item in plan.forbidden_actions)
    assert any("pytest" in item for item in plan.steps)
    assert plan.plan_hash