import json
from pathlib import Path

from hermes_ext.human_review.contracts import HumanReviewDecision
from hermes_ext.human_review.decision_gate import APPROVAL_ACKS, HumanReviewDecisionGate
from hermes_ext.human_review.evidence_loader import HumanReviewEvidenceLoader
from hermes_ext.human_review.experiment_proposal import NativeExperimentProposalBuilder


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
            "invariants": [{"id": "finalization.rollback_index_present", "status": "pass"}],
        },
    )
    _write_json(
        root,
        "reports/phase12/final_documentation_pack.json",
        {"note": "does not approve native integration"},
    )
    _write_json(root, "reports/phase12/final_stabilization_bundle.json", {"bundle": True})
    _write(
        root,
        "reports/phase12/phase12_test_result.md",
        "总通过 | 254\n失败 | 0\n禁止 import Hermes core / providers / tools",
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


def _evaluate(root: Path, decision=HumanReviewDecision.PENDING, reviewer="", acks=()):
    evidence = HumanReviewEvidenceLoader(root).load()
    proposal = NativeExperimentProposalBuilder().build()
    return HumanReviewDecisionGate().evaluate(
        evidence=evidence,
        native_experiment_proposal=proposal,
        decision=decision,
        reviewer=reviewer,
        acknowledgements=acks,
    )


def test_gate_passes_pending_review_with_clean_evidence(tmp_path):
    _write_clean_phase12_evidence(tmp_path)

    report = _evaluate(tmp_path)

    assert report.ok is True
    assert report.review_ready is True
    assert report.decision_allowed is True
    assert report.decision == HumanReviewDecision.PENDING
    assert not report.blocking_failures


def test_gate_fails_approve_without_reviewer_and_ack(tmp_path):
    _write_clean_phase12_evidence(tmp_path)

    report = _evaluate(tmp_path, decision=HumanReviewDecision.APPROVE_SHADOW_MERGE)

    assert report.ok is False
    assert report.review_ready is True
    assert report.decision_allowed is False
    assert "human_review.human_decision_requires_acknowledgement" in report.blocking_failures


def test_gate_allows_approve_shadow_merge_with_reviewer_and_ack(tmp_path):
    _write_clean_phase12_evidence(tmp_path)

    report = _evaluate(
        tmp_path,
        decision=HumanReviewDecision.APPROVE_SHADOW_MERGE,
        reviewer="reviewer@example.com",
        acks=APPROVAL_ACKS,
    )

    assert report.ok is True
    assert report.decision_allowed is True
    assert report.missing_acknowledgements == ()


def test_gate_fails_bad_phase12_merge_readiness(tmp_path):
    _write_clean_phase12_evidence(tmp_path)
    _write_json(
        tmp_path,
        "reports/phase12/merge_readiness_report.json",
        {"ok": False, "passed": 7, "warned": 0, "failed": 1},
    )

    report = _evaluate(tmp_path)

    assert report.ok is False
    assert "human_review.phase12_merge_readiness_clean" in report.blocking_failures


def test_gate_fails_missing_no_touch_markers(tmp_path):
    _write_clean_phase12_evidence(tmp_path)
    _write(tmp_path, "reports/phase12/phase12_exit_checklist.md", "incomplete")

    report = _evaluate(tmp_path)

    assert report.ok is False
    assert "human_review.phase12_no_touch_constraints_confirmed" in report.blocking_failures