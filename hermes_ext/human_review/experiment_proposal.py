"""Document-only native experiment proposal builder for Phase 13."""

from __future__ import annotations

from uuid import uuid4

from hermes_ext.human_review.contracts import (
    DOCUMENT_ONLY_NOT_APPROVED,
    NativeExperimentProposal,
)


class NativeExperimentProposalBuilder:
    """Build a proposal for a later phase without approving the work."""

    def build(self) -> NativeExperimentProposal:
        return NativeExperimentProposal(
            proposal_id=str(uuid4()),
            candidate_next_phase="Phase 14: No-op-first Native Experiment Design",
            status=DOCUMENT_ONLY_NOT_APPROVED,
            objective=(
                "Describe what a future native experiment phase would need to prove "
                "before any Hermes native boundary could be reconsidered."
            ),
            allowed_work=(
                "Write design documents only.",
                "Define candidate native experiment scope.",
                "Define no-op-first test requirements.",
                "Define rollback and kill-switch requirements.",
                "Define human approval requirements for a later phase.",
            ),
            forbidden_work=(
                "Do not implement native adapter code.",
                "Do not modify Hermes native lifeline files.",
                "Do not call native providers or model SDKs.",
                "Do not execute real tools.",
                "Do not write Hermes native memory.",
                "Do not write Hermes skills.",
                "Do not modify state databases.",
                "Do not generate patches against Hermes core.",
            ),
            required_preconditions=(
                "Phase 13 human review must explicitly approve shadow merge or request changes.",
                "A separate future phase must explicitly authorize native experiment design.",
                "The future phase must start from no-op-first contracts.",
                "The future phase must include rollback and exit criteria before code.",
                "The future phase must preserve feature flags default-off and kill-switch dominance.",
            ),
            rollback_requirements=(
                "Primary rollback anchor remains phase12-final-stabilization-merge-readiness.",
                "Previous rollback anchor remains phase11-shadow-assembly-manifest.",
                "No rollback step may partially delete Hermes native files.",
                "Any future experimental files must be deletable without affecting Hermes runtime.",
            ),
        )