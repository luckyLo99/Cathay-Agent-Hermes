from hermes_ext.human_review.contracts import DOCUMENT_ONLY_NOT_APPROVED
from hermes_ext.human_review.experiment_proposal import NativeExperimentProposalBuilder


def test_native_experiment_proposal_is_document_only_not_approved():
    proposal = NativeExperimentProposalBuilder().build()

    assert proposal.status == DOCUMENT_ONLY_NOT_APPROVED
    assert proposal.candidate_next_phase.startswith("Phase 14")
    assert any("Do not implement native adapter" in item for item in proposal.forbidden_work)
    assert any("Do not call native providers" in item for item in proposal.forbidden_work)
    assert proposal.proposal_hash