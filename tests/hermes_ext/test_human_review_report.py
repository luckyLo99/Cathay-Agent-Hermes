import json
from pathlib import Path

from hermes_ext.human_review.contracts import HumanReviewDecision
from hermes_ext.human_review.decision_gate import HumanReviewDecisionGate
from hermes_ext.human_review.dossier import (
    ColdStartValidationPlanBuilder,
    HumanReviewDossierBuilder,
)
from hermes_ext.human_review.evidence_loader import HumanReviewEvidenceLoader
from hermes_ext.human_review.experiment_proposal import NativeExperimentProposalBuilder
from hermes_ext.human_review.report import HumanReviewReporter


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


def test_reporter_writes_all_phase13_outputs(tmp_path):
    _write_clean_phase12_evidence(tmp_path)
    evidence = HumanReviewEvidenceLoader(tmp_path).load()
    dossier = HumanReviewDossierBuilder().build(evidence)
    plan = ColdStartValidationPlanBuilder().build()
    proposal = NativeExperimentProposalBuilder().build()
    decision = HumanReviewDecisionGate().evaluate(
        evidence=evidence,
        native_experiment_proposal=proposal,
        decision=HumanReviewDecision.PENDING,
    )

    output_dir = tmp_path / "reports/phase13"
    bundle = HumanReviewReporter(output_dir).write_all(
        dossier=dossier,
        cold_start_plan=plan,
        native_experiment_proposal=proposal,
        merge_decision_report=decision,
    )

    expected = [
        "human_review_dossier.md",
        "human_review_dossier.json",
        "merge_decision_report.md",
        "merge_decision_report.json",
        "cold_start_validation_plan.md",
        "cold_start_validation_plan.json",
        "native_experiment_proposal.md",
        "native_experiment_proposal.json",
        "review_board_checklist.md",
        "phase13_execution_log.md",
        "phase13_exit_checklist.md",
        "phase13_test_result.md",
        "phase13_review_bundle.json",
    ]

    for filename in expected:
        assert (output_dir / filename).exists()

    assert bundle.bundle_hash
    report_json = json.loads((output_dir / "merge_decision_report.json").read_text())
    assert report_json["ok"] is True