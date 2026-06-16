import pytest
from pydantic import ValidationError

from hermes_ext.human_review.contracts import (
    DOCUMENT_ONLY_NOT_APPROVED,
    FAIL,
    PASS,
    ColdStartValidationPlan,
    DecisionFinding,
    EvidenceFile,
    HumanReviewDecision,
    HumanReviewDossier,
    MergeDecisionReport,
    NativeExperimentProposal,
    SEVERITY_CRITICAL,
)


def test_evidence_file_rejects_path_escape():
    with pytest.raises(ValidationError):
        EvidenceFile(
            name="bad",
            relative_path="../secret.json",
            exists=False,
        )


def test_decision_finding_blocking_failure():
    finding = DecisionFinding(
        id="example",
        status=FAIL,
        severity=SEVERITY_CRITICAL,
        message="blocked",
    )

    assert finding.is_blocking


def test_dossier_hash_is_stable():
    sections = {
        "executive_summary": "summary",
        "scope": "scope",
        "architecture_review": "architecture",
        "risk_register": "risk",
        "acceptance_criteria": "criteria",
        "review_questions": "questions",
        "next_phase_policy": "policy",
    }

    dossier = HumanReviewDossier(
        dossier_id="id",
        title="title",
        sections=sections,
        source_evidence=("reports/phase12/merge_readiness_report.json",),
    )

    assert dossier.dossier_hash
    assert dossier.phase == 13


def test_native_experiment_proposal_rejects_approved_status():
    with pytest.raises(ValidationError):
        NativeExperimentProposal(
            proposal_id="id",
            candidate_next_phase="Phase 14",
            status="approved",
            objective="bad",
            allowed_work=("docs",),
            forbidden_work=("native adapter",),
            required_preconditions=("review",),
            rollback_requirements=("rollback",),
        )


def test_merge_decision_report_validates_blocking_failures():
    finding = DecisionFinding(
        id="example",
        status=PASS,
        severity=SEVERITY_CRITICAL,
        message="ok",
    )

    report = MergeDecisionReport(
        report_id="id",
        decision=HumanReviewDecision.PENDING,
        ok=True,
        review_ready=True,
        decision_allowed=True,
        required_acknowledgements=(),
        provided_acknowledgements=(),
        missing_acknowledgements=(),
        findings=(finding,),
        blocking_failures=(),
        warnings=(),
        recommendations=("continue review",),
    )

    assert report.report_hash


def test_cold_start_plan_requires_steps():
    with pytest.raises(ValidationError):
        ColdStartValidationPlan(
            plan_id="id",
            title="bad",
            objective="bad",
            steps=(),
            pass_criteria=("pass",),
            forbidden_actions=("forbid",),
        )


def test_native_experiment_proposal_document_only_constant():
    proposal = NativeExperimentProposal(
        proposal_id="id",
        candidate_next_phase="Phase 14",
        status=DOCUMENT_ONLY_NOT_APPROVED,
        objective="docs only",
        allowed_work=("Write design documents only.",),
        forbidden_work=("Do not implement native adapter code.",),
        required_preconditions=("Human review first.",),
        rollback_requirements=("Rollback anchor required.",),
    )

    assert proposal.status == DOCUMENT_ONLY_NOT_APPROVED
    assert proposal.proposal_hash