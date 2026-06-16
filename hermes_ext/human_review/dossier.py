"""Human review dossier and cold-start validation builders."""

from __future__ import annotations

from textwrap import dedent
from uuid import uuid4

from hermes_ext.human_review.contracts import (
    ColdStartValidationPlan,
    HumanReviewDossier,
    HumanReviewEvidence,
)


class HumanReviewDossierBuilder:
    """Build a deterministic human-review dossier from Phase 12 evidence."""

    def build(self, evidence: HumanReviewEvidence) -> HumanReviewDossier:
        source_evidence = tuple(doc.relative_path for doc in evidence.documents)

        sections = {
            "executive_summary": self._executive_summary(evidence),
            "scope": self._scope(),
            "architecture_review": self._architecture_review(),
            "risk_register": self._risk_register(),
            "acceptance_criteria": self._acceptance_criteria(),
            "review_questions": self._review_questions(),
            "next_phase_policy": self._next_phase_policy(),
        }

        return HumanReviewDossier(
            dossier_id=str(uuid4()),
            title="Phase 13 Human Review Dossier",
            sections=sections,
            source_evidence=source_evidence,
        )

    def _executive_summary(self, evidence: HumanReviewEvidence) -> str:
        missing = ", ".join(evidence.missing_required_names) or "none"
        invalid = ", ".join(evidence.invalid_required_names) or "none"
        return dedent(
            f"""
            Phase 13 packages Phase 12 evidence for human review and merge-decision
            discussion. It does not approve Hermes native integration.

            Required evidence missing: `{missing}`.
            Required evidence invalid: `{invalid}`.

            The default Phase 13 decision is `pending_human_review`. A shadow-merge
            approval requires explicit human reviewer identity and acknowledgements.
            Native experiment work remains proposal-only and not approved.
            """
        ).strip()

    def _scope(self) -> str:
        return dedent(
            """
            In scope:

            - Review Phase 12 finalization evidence.
            - Confirm shadow extension merge-readiness.
            - Produce a human review dossier.
            - Produce a merge decision report.
            - Produce a cold-start validation plan.
            - Produce a native experiment proposal for a later phase.

            Out of scope:

            - Modifying Hermes native lifeline files.
            - Creating native adapters.
            - Calling real providers or models.
            - Executing real tools.
            - Writing Hermes native memory.
            - Promoting shadow memory to native memory.
            - Generating patches against Hermes core.
            """
        ).strip()

    def _architecture_review(self) -> str:
        return dedent(
            """
            Architecture under review:

            ```text
            hermes_ext
              runtime / schema / hooks / security
              cathay / memoryx
              orchestration / harness
              adapter_scan / integration_spec
              native_boundary / golden_trace
              assembly / finalization
              human_review
            ```

            The review must preserve the shadow-only interpretation:

            - Cathay remains advisory signal only.
            - MemoryX remains isolated shadow memory only.
            - Native boundary remains no-op or blocked.
            - Feature flags remain disabled by default.
            - Kill switch remains dominant.
            - Reports remain reproducible markdown and JSON artifacts.
            """
        ).strip()

    def _risk_register(self) -> str:
        return dedent(
            """
            Primary risks to review:

            | Risk | Expected Control |
            |---|---|
            | Release gate misread as native approval | Phase 13 decision text must explicitly reject this interpretation |
            | Shadow memory accidentally promoted | Maintenance guide must preserve shadow-only memory rule |
            | Native boundary normalized into adapter | Proposal must remain document-only and not approved |
            | Future changes touch lifeline files | Any lifeline touch requires a new explicit phase |
            | Feature flags drift from default-off | Human review must check default-off and kill-switch precedence |
            | Evidence becomes stale | Cold-start validation must replay Phase 12 checks before merge |
            """
        ).strip()

    def _acceptance_criteria(self) -> str:
        return dedent(
            """
            Phase 13 acceptance criteria:

            - Phase 12 evidence is present and parseable.
            - Phase 12 merge readiness remains ok=true.
            - Phase 12 tests remain clean.
            - No-touch constraints are explicitly confirmed.
            - Maintenance rules remain strict.
            - Rollback evidence is present.
            - Native experiment proposal is document-only and not approved.
            - Any approval decision is explicit, attributable, and acknowledged.
            """
        ).strip()

    def _review_questions(self) -> str:
        return dedent(
            """
            Human reviewers should answer:

            1. Are the Phase 12 reports sufficient for shadow extension review?
            2. Is the no-touch boundary still acceptable and clear?
            3. Are feature flags and kill switch rules clear enough for operators?
            4. Is rollback documented well enough for merge review?
            5. Are there any ambiguous statements that imply native integration?
            6. Should the package be accepted as a shadow extension only?
            7. Should a separate future phase be opened for native experiment design?
            """
        ).strip()

    def _next_phase_policy(self) -> str:
        return dedent(
            """
            Phase 13 may produce one of four decisions:

            - `pending_human_review`
            - `approve_shadow_merge`
            - `request_changes`
            - `reject_shadow_merge`

            Even if `approve_shadow_merge` is selected, the approval is limited to
            hermes_ext shadow extension artifacts. It does not approve native
            adapter work. A native experiment can only begin in a separate later
            phase with explicit scope, rollback, and no-op-first constraints.
            """
        ).strip()


class ColdStartValidationPlanBuilder:
    """Build the cold-start validation plan for human reviewers."""

    def build(self) -> ColdStartValidationPlan:
        return ColdStartValidationPlan(
            plan_id=str(uuid4()),
            title="Phase 13 Cold Start Validation Plan",
            objective=(
                "Reproduce the Phase 12 evidence from a clean checkout before any "
                "human merge decision is treated as valid."
            ),
            steps=(
                "Checkout tag phase12-final-stabilization-merge-readiness.",
                "Create or reuse the isolated Python virtual environment.",
                "Run py_compile for hermes_ext source files.",
                "Run pytest tests/hermes_ext -q.",
                "Run hermes_ext.runtime.agent_doctor.",
                "Run hermes_ext.harness.cli doctor with all flags disabled.",
                "Run hermes_ext.finalization.cli to regenerate Phase 12 evidence.",
                "Run hermes_ext.human_review.cli to regenerate Phase 13 reports.",
                "Run cli.py --help.",
                "Run hermes doctor.",
                "Inspect git diff --stat and git status --short.",
            ),
            pass_criteria=(
                "All hermes_ext tests pass.",
                "Phase 12 merge readiness remains ok=true.",
                "Phase 13 merge decision report remains ok=true for pending review.",
                "No Hermes lifeline files appear in git diff.",
                "No provider, tool, native memory, state, secret, or patch side effect occurs.",
            ),
            forbidden_actions=(
                "Do not modify Hermes CLI or main loop.",
                "Do not modify pyproject.toml or lock files.",
                "Do not install new dependencies.",
                "Do not call real providers or models.",
                "Do not execute real tools.",
                "Do not write Hermes native memory.",
                "Do not generate native adapter code.",
            ),
        )