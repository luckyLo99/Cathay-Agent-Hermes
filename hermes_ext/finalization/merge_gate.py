from __future__ import annotations

import re

from hermes_ext.finalization.contracts import (
    FinalizationConfig,
    FinalizationEvidence,
    MergeReadinessReport,
    ReadinessInvariant,
    ReadinessInvariantSeverity,
    ReadinessInvariantStatus,
)


class MergeReadinessGate:
    """
    Final Phase 12 gate.

    It reads prior evidence and determines whether the shadow extension is merge-ready.
    """

    def __init__(self, config: FinalizationConfig) -> None:
        self.config = config

    def evaluate(self, evidence: list[FinalizationEvidence]) -> MergeReadinessReport:
        by_path = {item.relative_path: item for item in evidence}
        invariants = [
            self._all_required_evidence_exists(evidence),
            self._phase11_release_gate_clean(by_path),
            self._phase11_manifest_clean(by_path),
            self._phase11_tests_clean(by_path),
            self._phase11_exit_checklist_clean(by_path),
            self._phase10_golden_trace_stable(by_path),
            self._phase9_native_boundary_clean(by_path),
            self._rollback_index_present(by_path),
        ]

        passed = sum(1 for item in invariants if item.status == ReadinessInvariantStatus.PASS)
        warned = sum(1 for item in invariants if item.status == ReadinessInvariantStatus.WARN)
        failed = sum(1 for item in invariants if item.status == ReadinessInvariantStatus.FAIL)

        report = MergeReadinessReport(
            ok=failed == 0,
            invariants=invariants,
            evidence_count=len(evidence),
            passed=passed,
            warned=warned,
            failed=failed,
        ).with_hash()

        return report

    def _all_required_evidence_exists(self, evidence: list[FinalizationEvidence]) -> ReadinessInvariant:
        missing = [item.relative_path for item in evidence if not item.exists]
        if missing:
            return ReadinessInvariant(
                invariant_id="finalization.required_evidence_exists",
                status=ReadinessInvariantStatus.FAIL,
                severity=ReadinessInvariantSeverity.CRITICAL,
                message="Required Phase 9-11 evidence is missing.",
                evidence={"missing": missing},
            )

        return ReadinessInvariant(
            invariant_id="finalization.required_evidence_exists",
            status=ReadinessInvariantStatus.PASS,
            severity=ReadinessInvariantSeverity.CRITICAL,
            message="All required Phase 9-11 evidence files exist.",
            evidence={"count": len(evidence)},
        )

    def _phase11_release_gate_clean(self, by_path: dict[str, FinalizationEvidence]) -> ReadinessInvariant:
        item = by_path.get("reports/phase11/release_gate_report.json")
        payload = item.json_payload if item else None

        ok = bool((payload or {}).get("ok"))
        blocking = (payload or {}).get("blocking_failures", [])
        warnings = (payload or {}).get("warnings", [])

        if ok and not blocking and not warnings:
            return ReadinessInvariant(
                invariant_id="finalization.phase11_release_gate_clean",
                status=ReadinessInvariantStatus.PASS,
                severity=ReadinessInvariantSeverity.CRITICAL,
                message="Phase 11 release gate is clean.",
                evidence={"ok": ok, "blocking_failures": len(blocking), "warnings": len(warnings)},
            )

        return ReadinessInvariant(
            invariant_id="finalization.phase11_release_gate_clean",
            status=ReadinessInvariantStatus.FAIL if self.config.require_clean_phase11_gate else ReadinessInvariantStatus.WARN,
            severity=ReadinessInvariantSeverity.CRITICAL,
            message="Phase 11 release gate is not clean.",
            evidence={"ok": ok, "blocking_failures": blocking, "warnings": warnings},
        )

    def _phase11_manifest_clean(self, by_path: dict[str, FinalizationEvidence]) -> ReadinessInvariant:
        item = by_path.get("reports/phase11/shadow_assembly_manifest.json")
        payload = item.json_payload if item else None
        summary = (payload or {}).get("summary", {})
        manifest_hash = (payload or {}).get("manifest_hash")

        failed = int(summary.get("invariants_failed", -1)) if isinstance(summary, dict) else -1
        warned = int(summary.get("invariants_warned", -1)) if isinstance(summary, dict) else -1
        passed = int(summary.get("invariants_passed", 0)) if isinstance(summary, dict) else 0

        if manifest_hash and failed == 0 and warned == 0 and passed >= 1:
            return ReadinessInvariant(
                invariant_id="finalization.phase11_manifest_clean",
                status=ReadinessInvariantStatus.PASS,
                severity=ReadinessInvariantSeverity.CRITICAL,
                message="Phase 11 assembly manifest is clean.",
                evidence={"manifest_hash": manifest_hash, "passed": passed, "warned": warned, "failed": failed},
            )

        return ReadinessInvariant(
            invariant_id="finalization.phase11_manifest_clean",
            status=ReadinessInvariantStatus.FAIL,
            severity=ReadinessInvariantSeverity.CRITICAL,
            message="Phase 11 assembly manifest is not clean.",
            evidence={"manifest_hash": manifest_hash, "passed": passed, "warned": warned, "failed": failed},
        )

    def _phase11_tests_clean(self, by_path: dict[str, FinalizationEvidence]) -> ReadinessInvariant:
        item = by_path.get("reports/phase11/phase11_test_result.md")
        text = item.text_excerpt if item else ""

        expected = self.config.expected_total_tests
        has_expected_total = (
            f"{expected}/" in text
            or f"总通过 | {expected}" in text
            or re.search(rf"\b{expected}\s+PASS\b", text) is not None
        )
        has_zero_fail = ("失败 | 0" in text) or ("failed | 0" in text.lower()) or ("0 failed" in text.lower())

        if has_expected_total and has_zero_fail:
            return ReadinessInvariant(
                invariant_id="finalization.phase11_tests_clean",
                status=ReadinessInvariantStatus.PASS,
                severity=ReadinessInvariantSeverity.CRITICAL,
                message="Phase 11 test evidence is clean.",
                evidence={"expected_total_tests": expected, "has_zero_fail": has_zero_fail},
            )

        return ReadinessInvariant(
            invariant_id="finalization.phase11_tests_clean",
            status=ReadinessInvariantStatus.FAIL,
            severity=ReadinessInvariantSeverity.CRITICAL,
            message="Phase 11 test evidence is incomplete or not clean.",
            evidence={"expected_total_tests": expected, "has_expected_total": has_expected_total, "has_zero_fail": has_zero_fail},
        )

    def _phase11_exit_checklist_clean(self, by_path: dict[str, FinalizationEvidence]) -> ReadinessInvariant:
        item = by_path.get("reports/phase11/phase11_exit_checklist.md")
        text = item.text_excerpt if item else ""

        required_phrases = [
            "未修改 Hermes 生命线文件",
            "未修改 Hermes CLI 入口",
            "未修改 pyproject.toml",
            "未修改 lock 文件",
            "未安装新依赖",
            "release_gate ok=true",
        ]
        missing = [phrase for phrase in required_phrases if phrase not in text]

        if not missing:
            return ReadinessInvariant(
                invariant_id="finalization.phase11_exit_checklist_clean",
                status=ReadinessInvariantStatus.PASS,
                severity=ReadinessInvariantSeverity.CRITICAL,
                message="Phase 11 exit checklist confirms no-touch constraints.",
                evidence={"missing": []},
            )

        return ReadinessInvariant(
            invariant_id="finalization.phase11_exit_checklist_clean",
            status=ReadinessInvariantStatus.FAIL,
            severity=ReadinessInvariantSeverity.CRITICAL,
            message="Phase 11 exit checklist is missing required no-touch evidence.",
            evidence={"missing": missing},
        )

    def _phase10_golden_trace_stable(self, by_path: dict[str, FinalizationEvidence]) -> ReadinessInvariant:
        item = by_path.get("reports/phase10/golden_trace_replay_report.json")
        payload = item.json_payload if item else None

        ok = bool((payload or {}).get("ok"))
        case_count = int((payload or {}).get("case_count", 0))
        stable_cases = int((payload or {}).get("stable_cases", -1))
        unstable_cases = int((payload or {}).get("unstable_cases", -1))
        failed = int((payload or {}).get("failed", -1))
        violations = (payload or {}).get("violations", [])

        clean = ok and case_count == stable_cases and unstable_cases == 0 and failed == 0 and not violations
        if clean:
            return ReadinessInvariant(
                invariant_id="finalization.phase10_golden_trace_stable",
                status=ReadinessInvariantStatus.PASS,
                severity=ReadinessInvariantSeverity.CRITICAL,
                message="Phase 10 golden trace remains stable.",
                evidence={"case_count": case_count, "stable_cases": stable_cases, "unstable_cases": unstable_cases, "failed": failed},
            )

        return ReadinessInvariant(
            invariant_id="finalization.phase10_golden_trace_stable",
            status=ReadinessInvariantStatus.FAIL if self.config.require_phase10_stability else ReadinessInvariantStatus.WARN,
            severity=ReadinessInvariantSeverity.CRITICAL,
            message="Phase 10 golden trace is not clean.",
            evidence={"ok": ok, "case_count": case_count, "stable_cases": stable_cases, "unstable_cases": unstable_cases, "failed": failed, "violations": violations},
        )

    def _phase9_native_boundary_clean(self, by_path: dict[str, FinalizationEvidence]) -> ReadinessInvariant:
        item = by_path.get("reports/phase9/native_boundary_contract_report.json")
        payload = item.json_payload if item else None
        results = (payload or {}).get("results", [])

        side_effect_fields = [
            "native_called",
            "tool_executed",
            "provider_called",
            "memory_written",
            "state_mutated",
            "patch_generated",
            "secret_read",
        ]
        side_effect_counts = {
            field: sum(1 for result in results if isinstance(result, dict) and bool(result.get(field)))
            for field in side_effect_fields
        }

        ok = bool((payload or {}).get("ok"))
        failed = int((payload or {}).get("failed", -1))
        violations = (payload or {}).get("violations", [])
        clean = ok and failed == 0 and not violations and all(count == 0 for count in side_effect_counts.values())

        if clean:
            return ReadinessInvariant(
                invariant_id="finalization.phase9_native_boundary_no_side_effects",
                status=ReadinessInvariantStatus.PASS,
                severity=ReadinessInvariantSeverity.CRITICAL,
                message="Phase 9 native boundary remains no-op and side-effect free.",
                evidence={"failed": failed, "violations": len(violations), "side_effect_counts": side_effect_counts},
            )

        return ReadinessInvariant(
            invariant_id="finalization.phase9_native_boundary_no_side_effects",
            status=ReadinessInvariantStatus.FAIL if self.config.require_phase9_no_side_effects else ReadinessInvariantStatus.WARN,
            severity=ReadinessInvariantSeverity.CRITICAL,
            message="Phase 9 native boundary evidence is not clean.",
            evidence={"ok": ok, "failed": failed, "violations": violations, "side_effect_counts": side_effect_counts},
        )

    def _rollback_index_present(self, by_path: dict[str, FinalizationEvidence]) -> ReadinessInvariant:
        item = by_path.get("reports/phase11/phase11_exit_checklist.md")
        text = item.text_excerpt if item else ""

        has_rollback = "rollback" in text.lower() or "回滚" in text
        if has_rollback:
            return ReadinessInvariant(
                invariant_id="finalization.rollback_index_present",
                status=ReadinessInvariantStatus.PASS,
                severity=ReadinessInvariantSeverity.ERROR,
                message="Rollback evidence is present.",
                evidence={"present": True},
            )

        return ReadinessInvariant(
            invariant_id="finalization.rollback_index_present",
            status=ReadinessInvariantStatus.FAIL,
            severity=ReadinessInvariantSeverity.ERROR,
            message="Rollback evidence is missing.",
            evidence={"present": False},
        )