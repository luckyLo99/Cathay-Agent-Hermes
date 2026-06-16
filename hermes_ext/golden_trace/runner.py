from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from hermes_ext.golden_trace.contracts import (
    GoldenTraceCase,
    GoldenTraceCaseResult,
    GoldenTraceKind,
    GoldenTraceReplayReport,
    GoldenTraceRunConfig,
    GoldenTraceStatus,
)
from hermes_ext.golden_trace.normalizer import GoldenTraceNormalizer
from hermes_ext.golden_trace.trace_pack import build_default_golden_trace_pack
from hermes_ext.golden_trace.verifier import GoldenTraceVerifier
from hermes_ext.harness.contracts import ExtensionHarnessMode, HarnessRunRequest
from hermes_ext.harness.feature_flags import FeatureFlagResolver
from hermes_ext.harness.integration_harness import IntegrationHarness
from hermes_ext.native_boundary.contract_suite import NoopNativeBoundaryContractSuite


class GoldenTraceRunner:
    """
    Runs golden traces multiple times and verifies stable canonical hashes.

    It only uses hermes_ext shadow harness and no-op native boundary.
    """

    def __init__(self, config: GoldenTraceRunConfig) -> None:
        self.config = config
        self.normalizer = GoldenTraceNormalizer()

    def run_default_pack(self) -> GoldenTraceReplayReport:
        pack = build_default_golden_trace_pack()
        results: list[GoldenTraceCaseResult] = []

        for iteration in range(self.config.repeat):
            for case in pack.cases:
                result = self._run_case(case, iteration=iteration)
                results.append(result)
                if self.config.fail_fast and not result.ok:
                    break

        verifier = GoldenTraceVerifier()
        verification = verifier.verify(pack=pack, results=results)

        report = GoldenTraceReplayReport(
            pack_id=pack.pack_id,
            ok=verification.ok and all(result.ok for result in results),
            repeat=self.config.repeat,
            case_count=len(pack.cases),
            result_count=len(results),
            passed=sum(1 for result in results if result.ok),
            failed=sum(1 for result in results if not result.ok),
            stable_cases=verification.stable_cases,
            unstable_cases=verification.unstable_cases,
            results=results,
            violations=verification.violations,
            metadata={
                "phase": 10,
                "project_root": str(self.config.project_root),
                "state_dir": str(self.config.state_dir),
            },
        ).with_hash()

        return report

    def _run_case(self, case: GoldenTraceCase, *, iteration: int) -> GoldenTraceCaseResult:
        state_dir = self._case_state_dir(case, iteration)
        self._reset_dir(state_dir)

        try:
            raw_output = self._execute_case(case, state_dir=state_dir)
            normalized_output = self.normalizer.normalize(raw_output)
            canonical_hash = self.normalizer.canonical_hash(normalized_output)
            ok, error = self._validate_case(case, raw_output)

            return GoldenTraceCaseResult(
                case_id=case.case_id,
                iteration=iteration,
                ok=ok,
                status=GoldenTraceStatus.PASSED if ok else GoldenTraceStatus.FAILED,
                canonical_hash=canonical_hash,
                normalized_output=normalized_output,
                error=error,
            )
        except Exception as exc:
            normalized_output = {"exception": exc.__class__.__name__, "message": str(exc)}
            return GoldenTraceCaseResult(
                case_id=case.case_id,
                iteration=iteration,
                ok=False,
                status=GoldenTraceStatus.FAILED,
                canonical_hash=self.normalizer.canonical_hash(normalized_output),
                normalized_output=normalized_output,
                error=str(exc),
            )

    def _execute_case(self, case: GoldenTraceCase, *, state_dir: Path) -> dict[str, Any]:
        if case.kind == GoldenTraceKind.NATIVE_BOUNDARY_SPEC:
            if self.config.spec_json is None:
                suite = NoopNativeBoundaryContractSuite.synthetic()
            else:
                suite = NoopNativeBoundaryContractSuite.from_spec_json(
                    self.config.spec_json,
                    limit=self.config.native_boundary_limit,
                )
            return {
                "case_kind": case.kind.value,
                "native_boundary": suite.run().model_dump(mode="json"),
            }

        flags = FeatureFlagResolver(env={}, explicit=case.flags).resolve()
        mode = (
            ExtensionHarnessMode.DIAGNOSTIC
            if case.kind == GoldenTraceKind.DIAGNOSTIC
            else ExtensionHarnessMode.SHADOW
        )

        request = HarnessRunRequest(
            request_id=f"golden-{case.case_id}-{iteration_safe_name(state_dir.name)}",
            mode=mode,
            text=case.text,
            state_dir=state_dir,
            flags=flags,
            tool_payload=case.tool_payload,
            metadata={"golden_case_id": case.case_id},
        )

        result = IntegrationHarness(project_root=self.config.project_root).run(request)
        return {
            "case_kind": case.kind.value,
            "harness": result.model_dump(mode="json"),
        }

    def _validate_case(self, case: GoldenTraceCase, raw_output: dict[str, Any]) -> tuple[bool, str | None]:
        if case.kind == GoldenTraceKind.NATIVE_BOUNDARY_SPEC:
            native = raw_output.get("native_boundary", {})
            ok = bool(native.get("ok")) == case.expected_ok
            if not ok:
                return False, "native boundary suite ok mismatch"

            if case.expected_native_violations is not None:
                violations = len(native.get("violations", []))
                if violations != case.expected_native_violations:
                    return False, f"native boundary violations mismatch: {violations}"

            return True, None

        harness = raw_output.get("harness", {})
        if bool(harness.get("ok")) != case.expected_ok:
            return False, "harness ok mismatch"

        if case.expected_shadow_status is not None:
            shadow = harness.get("shadow_result") or {}
            if shadow.get("status") != case.expected_shadow_status:
                return False, "shadow status mismatch"

        if case.expected_blocked is not None:
            shadow = harness.get("shadow_result") or {}
            blocked = bool((shadow.get("metadata") or {}).get("blocked"))
            if blocked != case.expected_blocked:
                return False, "blocked metadata mismatch"

        return True, None

    def _case_state_dir(self, case: GoldenTraceCase, iteration: int) -> Path:
        return self.config.state_dir / f"{case.case_id}" / f"iteration-{iteration}"

    @staticmethod
    def _reset_dir(path: Path) -> None:
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)


def iteration_safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "-" for ch in value)