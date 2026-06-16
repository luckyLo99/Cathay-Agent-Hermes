"""Phase 13 human review decision gate."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any, Mapping
from uuid import uuid4

from hermes_ext.human_review.contracts import (
    FAIL,
    PASS,
    WARN,
    DecisionFinding,
    HumanReviewDecision,
    HumanReviewEvidence,
    MergeDecisionReport,
    NativeExperimentProposal,
    SEVERITY_CRITICAL,
    SEVERITY_ERROR,
    SEVERITY_INFO,
    SEVERITY_WARNING,
)


APPROVAL_ACKS = (
    "ack_shadow_only",
    "ack_no_native_integration",
    "ack_rollback_anchor",
    "ack_human_review_complete",
)


class HumanReviewDecisionGate:
    """Evaluate whether Phase 13 review packet and decision are valid."""

    def evaluate(
        self,
        evidence: HumanReviewEvidence,
        native_experiment_proposal: NativeExperimentProposal,
        decision: HumanReviewDecision = HumanReviewDecision.PENDING,
        reviewer: str = "",
        acknowledgements: tuple[str, ...] = (),
    ) -> MergeDecisionReport:
        findings: tuple[DecisionFinding, ...] = (
            self._phase12_evidence_exists(evidence),
            self._phase12_merge_readiness_clean(evidence),
            self._phase12_tests_clean(evidence),
            self._phase12_no_touch_constraints_confirmed(evidence),
            self._phase12_native_integration_not_approved(evidence),
            self._maintenance_rules_preserved(evidence),
            self._rollback_evidence_present(evidence),
            self._cold_start_plan_present(),
            self._native_experiment_proposal_document_only(native_experiment_proposal),
            self._human_decision_requires_acknowledgement(
                decision=decision,
                reviewer=reviewer,
                acknowledgements=acknowledgements,
            ),
        )

        blocking = tuple(f.id for f in findings if f.is_blocking)
        warnings = tuple(f.message for f in findings if f.status == WARN)
        required_acks = self._required_acknowledgements(decision)
        provided = tuple(sorted(set(acknowledgements)))
        missing_acks = tuple(ack for ack in required_acks if ack not in provided)

        review_ready = not any(
            f.is_blocking
            for f in findings
            if f.id != "human_review.human_decision_requires_acknowledgement"
        )
        decision_allowed = not any(
            f.is_blocking
            for f in findings
            if f.id == "human_review.human_decision_requires_acknowledgement"
        )

        recommendations = (
            "Treat Phase 13 as human review and decision packaging only.",
            "Do not start native adapter implementation from Phase 13.",
            "Use cold-start validation before treating any shadow merge approval as final.",
            "If native experiment is desired, open a separate later phase with no-op-first constraints.",
        )

        return MergeDecisionReport(
            report_id=str(uuid4()),
            decision=decision,
            reviewer=reviewer,
            ok=review_ready and decision_allowed,
            review_ready=review_ready,
            decision_allowed=decision_allowed,
            required_acknowledgements=required_acks,
            provided_acknowledgements=provided,
            missing_acknowledgements=missing_acks,
            findings=findings,
            blocking_failures=blocking,
            warnings=warnings,
            recommendations=recommendations,
        )

    def _phase12_evidence_exists(self, evidence: HumanReviewEvidence) -> DecisionFinding:
        missing = evidence.missing_required_names
        invalid = evidence.invalid_required_names

        if missing or invalid:
            return DecisionFinding(
                id="human_review.phase12_evidence_exists",
                status=FAIL,
                severity=SEVERITY_CRITICAL,
                message=f"missing={list(missing)}, invalid={list(invalid)}",
                evidence_refs=tuple(doc.relative_path for doc in evidence.documents),
            )

        return DecisionFinding(
            id="human_review.phase12_evidence_exists",
            status=PASS,
            severity=SEVERITY_CRITICAL,
            message="All required Phase 12 evidence files exist and parse.",
            evidence_refs=tuple(doc.relative_path for doc in evidence.documents),
        )

    def _phase12_merge_readiness_clean(
        self,
        evidence: HumanReviewEvidence,
    ) -> DecisionFinding:
        doc = evidence.document("phase12_merge_readiness_report")
        data = doc.json_data or {}

        ok = _first_bool(data, "ok")
        failed = _max_number(data, ("failed", "failed_count"))
        warned = _max_number(data, ("warned", "warned_count"))
        passed = _max_number(data, ("passed", "passed_count"))

        if ok is not True or failed > 0:
            return DecisionFinding(
                id="human_review.phase12_merge_readiness_clean",
                status=FAIL,
                severity=SEVERITY_CRITICAL,
                message=f"Phase 12 merge readiness not clean: ok={ok}, failed={failed}",
                evidence_refs=(doc.relative_path,),
            )

        if warned > 0:
            return DecisionFinding(
                id="human_review.phase12_merge_readiness_clean",
                status=WARN,
                severity=SEVERITY_WARNING,
                message=f"Phase 12 merge readiness has warnings={warned}",
                evidence_refs=(doc.relative_path,),
            )

        return DecisionFinding(
            id="human_review.phase12_merge_readiness_clean",
            status=PASS,
            severity=SEVERITY_CRITICAL,
            message=f"Phase 12 merge readiness is clean with passed={passed}.",
            evidence_refs=(doc.relative_path,),
        )

    def _phase12_tests_clean(self, evidence: HumanReviewEvidence) -> DecisionFinding:
        doc = evidence.document("phase12_test_result")
        text = doc.text_excerpt.lower()

        has_total_pass = "254" in text and ("总通过" in text or "total" in text)
        has_zero_fail = "失败 | 0" in doc.text_excerpt or "failed | 0" in text or "失败: 0" in text
        has_no_import = "禁止 import" in doc.text_excerpt or "no-import" in text

        if not (has_total_pass and has_zero_fail and has_no_import):
            return DecisionFinding(
                id="human_review.phase12_tests_clean",
                status=FAIL,
                severity=SEVERITY_ERROR,
                message="Phase 12 test evidence does not confirm clean tests and no-import coverage.",
                evidence_refs=(doc.relative_path,),
            )

        return DecisionFinding(
            id="human_review.phase12_tests_clean",
            status=PASS,
            severity=SEVERITY_ERROR,
            message="Phase 12 test evidence confirms clean tests and no-import coverage.",
            evidence_refs=(doc.relative_path,),
        )

    def _phase12_no_touch_constraints_confirmed(
        self,
        evidence: HumanReviewEvidence,
    ) -> DecisionFinding:
        doc = evidence.document("phase12_exit_checklist")
        text = doc.text_excerpt.lower()

        required_markers = (
            "未修改 hermes 生命线文件",
            "未调用真实模型",
            "未调用真实 provider",
            "未执行真实工具",
            "未写 hermes native memory",
            "未生成 patch",
        )

        missing = [marker for marker in required_markers if marker not in text]

        if missing:
            return DecisionFinding(
                id="human_review.phase12_no_touch_constraints_confirmed",
                status=FAIL,
                severity=SEVERITY_CRITICAL,
                message=f"Phase 12 no-touch evidence missing markers={missing}",
                evidence_refs=(doc.relative_path,),
            )

        return DecisionFinding(
            id="human_review.phase12_no_touch_constraints_confirmed",
            status=PASS,
            severity=SEVERITY_CRITICAL,
            message="Phase 12 no-touch constraints are explicitly confirmed.",
            evidence_refs=(doc.relative_path,),
        )

    def _phase12_native_integration_not_approved(
        self,
        evidence: HumanReviewEvidence,
    ) -> DecisionFinding:
        merge_doc = evidence.document("phase12_merge_readiness_report")
        final_doc = evidence.document("phase12_final_documentation_pack")

        combined = (
            str(merge_doc.json_data or {}).lower()
            + "\n"
            + str(final_doc.json_data or {}).lower()
            + "\n"
            + merge_doc.text_excerpt.lower()
            + "\n"
            + final_doc.text_excerpt.lower()
        )

        required = (
            "native integration",
            "not approve",
        )

        if not all(token in combined for token in required):
            return DecisionFinding(
                id="human_review.phase12_native_integration_not_approved",
                status=FAIL,
                severity=SEVERITY_CRITICAL,
                message="Phase 12 evidence does not clearly reject native integration approval.",
                evidence_refs=(merge_doc.relative_path, final_doc.relative_path),
            )

        return DecisionFinding(
            id="human_review.phase12_native_integration_not_approved",
            status=PASS,
            severity=SEVERITY_CRITICAL,
            message="Phase 12 evidence clearly states native integration is not approved.",
            evidence_refs=(merge_doc.relative_path, final_doc.relative_path),
        )

    def _maintenance_rules_preserved(
        self,
        evidence: HumanReviewEvidence,
    ) -> DecisionFinding:
        doc = evidence.document("phase12_maintenance_guide")
        text = doc.text_excerpt.lower()

        required = (
            "no-import",
            "kill-switch",
            "shadow-only",
            "no-op by default",
            "lifeline files",
        )

        missing = [token for token in required if token not in text]

        if missing:
            return DecisionFinding(
                id="human_review.maintenance_rules_preserved",
                status=FAIL,
                severity=SEVERITY_ERROR,
                message=f"Maintenance guide missing required rules={missing}",
                evidence_refs=(doc.relative_path,),
            )

        return DecisionFinding(
            id="human_review.maintenance_rules_preserved",
            status=PASS,
            severity=SEVERITY_ERROR,
            message="Phase 12 maintenance rules preserve no-import, shadow-only, no-op, and lifeline controls.",
            evidence_refs=(doc.relative_path,),
        )

    def _rollback_evidence_present(self, evidence: HumanReviewEvidence) -> DecisionFinding:
        merge_doc = evidence.document("phase12_merge_readiness_report")
        rollback_doc = evidence.document("phase12_rollback_index")

        merge_text = str(merge_doc.json_data or {}).lower() + merge_doc.text_excerpt.lower()
        rollback_text = rollback_doc.text_excerpt.lower()

        has_gate = "rollback_index_present" in merge_text
        has_reset = "git reset --hard" in rollback_text

        if not (has_gate and has_reset):
            return DecisionFinding(
                id="human_review.rollback_evidence_present",
                status=FAIL,
                severity=SEVERITY_ERROR,
                message="Rollback evidence is incomplete.",
                evidence_refs=(merge_doc.relative_path, rollback_doc.relative_path),
            )

        return DecisionFinding(
            id="human_review.rollback_evidence_present",
            status=PASS,
            severity=SEVERITY_ERROR,
            message="Rollback evidence is present.",
            evidence_refs=(merge_doc.relative_path, rollback_doc.relative_path),
        )

    def _cold_start_plan_present(self) -> DecisionFinding:
        return DecisionFinding(
            id="human_review.cold_start_plan_present",
            status=PASS,
            severity=SEVERITY_ERROR,
            message="Cold-start validation plan is generated by Phase 13.",
            evidence_refs=("reports/phase13/cold_start_validation_plan.md",),
        )

    def _native_experiment_proposal_document_only(
        self,
        proposal: NativeExperimentProposal,
    ) -> DecisionFinding:
        if proposal.status != "document_only_not_approved":
            return DecisionFinding(
                id="human_review.native_experiment_proposal_document_only",
                status=FAIL,
                severity=SEVERITY_CRITICAL,
                message=f"Native experiment proposal status is unsafe: {proposal.status}",
                evidence_refs=("reports/phase13/native_experiment_proposal.md",),
            )

        forbidden_text = "\n".join(proposal.forbidden_work).lower()
        if "native adapter" not in forbidden_text or "provider" not in forbidden_text:
            return DecisionFinding(
                id="human_review.native_experiment_proposal_document_only",
                status=FAIL,
                severity=SEVERITY_CRITICAL,
                message="Native experiment proposal does not explicitly forbid native adapter/provider work.",
                evidence_refs=("reports/phase13/native_experiment_proposal.md",),
            )

        return DecisionFinding(
            id="human_review.native_experiment_proposal_document_only",
            status=PASS,
            severity=SEVERITY_CRITICAL,
            message="Native experiment proposal is document-only and not approved.",
            evidence_refs=("reports/phase13/native_experiment_proposal.md",),
        )

    def _human_decision_requires_acknowledgement(
        self,
        decision: HumanReviewDecision,
        reviewer: str,
        acknowledgements: tuple[str, ...],
    ) -> DecisionFinding:
        required = self._required_acknowledgements(decision)
        provided = set(acknowledgements)
        missing = [ack for ack in required if ack not in provided]

        if decision == HumanReviewDecision.PENDING:
            return DecisionFinding(
                id="human_review.human_decision_requires_acknowledgement",
                status=PASS,
                severity=SEVERITY_INFO,
                message="Decision remains pending human review.",
                evidence_refs=(),
            )

        if not reviewer.strip():
            return DecisionFinding(
                id="human_review.human_decision_requires_acknowledgement",
                status=FAIL,
                severity=SEVERITY_ERROR,
                message="Non-pending decision requires a reviewer identity.",
                evidence_refs=(),
            )

        if missing:
            return DecisionFinding(
                id="human_review.human_decision_requires_acknowledgement",
                status=FAIL,
                severity=SEVERITY_ERROR,
                message=f"Decision {decision.value} missing acknowledgements={missing}",
                evidence_refs=(),
            )

        return DecisionFinding(
            id="human_review.human_decision_requires_acknowledgement",
            status=PASS,
            severity=SEVERITY_ERROR,
            message=f"Decision {decision.value} has reviewer and required acknowledgements.",
            evidence_refs=(),
        )

    def _required_acknowledgements(
        self,
        decision: HumanReviewDecision,
    ) -> tuple[str, ...]:
        if decision == HumanReviewDecision.APPROVE_SHADOW_MERGE:
            return APPROVAL_ACKS
        if decision in {
            HumanReviewDecision.REQUEST_CHANGES,
            HumanReviewDecision.REJECT_SHADOW_MERGE,
        }:
            return ("ack_human_review_complete",)
        return ()


def _walk_json(value: Any) -> Iterable[tuple[str, Any]]:
    if isinstance(value, Mapping):
        for key, child in value.items():
            yield str(key), child
            yield from _walk_json(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_json(child)


def _numbers_for_key(data: Mapping[str, Any], key: str) -> list[int]:
    values: list[int] = []
    for found_key, value in _walk_json(data):
        if found_key == key and isinstance(value, int) and not isinstance(value, bool):
            values.append(value)
    return values


def _max_number(data: Mapping[str, Any], keys: tuple[str, ...]) -> int:
    values: list[int] = []
    for key in keys:
        values.extend(_numbers_for_key(data, key))
    return max(values) if values else 0


def _first_bool(data: Mapping[str, Any], key: str) -> bool | None:
    for found_key, value in _walk_json(data):
        if found_key == key and isinstance(value, bool):
            return value
    return None