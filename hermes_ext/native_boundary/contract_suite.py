from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from hermes_ext.integration_spec.contracts import IntegrationMode, ZeroTouchIntegrationSpec
from hermes_ext.native_boundary.contracts import (
    NativeBoundaryContractCase,
    NativeBoundaryContractRunResult,
    NativeBoundaryContractViolation,
    NativeBoundaryKind,
    NativeBoundaryOperation,
    NativeBoundaryRequest,
    NativeBoundaryResult,
    NativeBoundaryVerdict,
)
from hermes_ext.native_boundary.noop_boundary import NoopNativeBoundary


class NoopNativeBoundaryContractSuite:
    """
    Contract suite for proving that native boundary remains no-op.

    It can run synthetic cases or derive cases from Phase 8 zero-touch spec.
    """

    def __init__(
        self,
        *,
        cases: list[NativeBoundaryContractCase],
        boundary: NoopNativeBoundary | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        self.cases = cases
        self.boundary = boundary or NoopNativeBoundary()
        self.metadata = metadata or {}

    @classmethod
    def synthetic(cls) -> "NoopNativeBoundaryContractSuite":
        cases = [
            cls._case("tool execution is blocked", NativeBoundaryKind.TOOL, NativeBoundaryOperation.EXECUTE, "bash"),
            cls._case("memory write is blocked", NativeBoundaryKind.MEMORY, NativeBoundaryOperation.WRITE, "native_memory"),
            cls._case("provider call is blocked", NativeBoundaryKind.PROVIDER, NativeBoundaryOperation.CALL, "openai"),
            cls._case("prompt mutation is blocked", NativeBoundaryKind.PROMPT, NativeBoundaryOperation.MUTATE, "system_prompt"),
            cls._case("state mutation is blocked", NativeBoundaryKind.STATE, NativeBoundaryOperation.MUTATE, "hermes_state"),
            cls._case("patch generation is blocked", NativeBoundaryKind.SECURITY, NativeBoundaryOperation.PATCH, "source_patch"),
            cls._case("gateway observation is audit-only noop", NativeBoundaryKind.GATEWAY, NativeBoundaryOperation.OBSERVE, "session_event"),
        ]
        return cls(cases=cases, metadata={"source": "synthetic"})

    @classmethod
    def from_spec_json(
        cls,
        path: Path,
        *,
        limit: int = 100,
    ) -> "NoopNativeBoundaryContractSuite":
        data = json.loads(path.read_text(encoding="utf-8"))
        spec = ZeroTouchIntegrationSpec.model_validate(data, strict=False)
        cases: list[NativeBoundaryContractCase] = []

        for entry in spec.matrix.entries[:limit]:
            cases.append(
                NativeBoundaryContractCase(
                    name=f"{entry.integration_mode.value}: {entry.relative_path}",
                    request=NativeBoundaryRequest(
                        kind=cls._kind_from_surface(entry.surface.value),
                        operation=cls._operation_from_mode(entry.integration_mode),
                        target=entry.relative_path,
                        payload={
                            "symbol": entry.symbol,
                            "surface": entry.surface.value,
                            "source_posture": entry.source_posture.value,
                            "source_risk": entry.source_risk.value,
                            "required_flags": [flag.value for flag in entry.required_flags],
                        },
                        metadata={
                            "entry_id": entry.entry_id,
                            "candidate_id": entry.candidate_id,
                            "phase": 9,
                        },
                    ),
                )
            )

        return cls(
            cases=cases,
            metadata={
                "source": str(path),
                "spec_id": spec.spec_id,
                "spec_hash": spec.spec_hash,
                "limit": limit,
            },
        )

    def run(self) -> NativeBoundaryContractRunResult:
        results: list[NativeBoundaryResult] = []
        violations: list[NativeBoundaryContractViolation] = []

        for case in self.cases:
            try:
                result = self.boundary.handle(case.request)
                results.append(result)
                violations.extend(self._validate_case(case, result))
            except Exception as exc:
                violations.append(
                    NativeBoundaryContractViolation(
                        request_id=case.request.request_id,
                        rule_id="native_boundary.exception",
                        message=f"boundary raised exception: {exc}",
                    )
                )

        failed_request_ids = {violation.request_id for violation in violations}
        failed = sum(1 for case in self.cases if case.request.request_id in failed_request_ids)
        passed = len(self.cases) - failed

        return NativeBoundaryContractRunResult(
            ok=failed == 0,
            case_count=len(self.cases),
            passed=passed,
            failed=failed,
            results=results,
            violations=violations,
            metadata=self.metadata,
        )

    def _validate_case(
        self,
        case: NativeBoundaryContractCase,
        result: NativeBoundaryResult,
    ) -> list[NativeBoundaryContractViolation]:
        violations: list[NativeBoundaryContractViolation] = []

        if result.verdict not in case.expected_verdicts:
            violations.append(
                NativeBoundaryContractViolation(
                    request_id=case.request.request_id,
                    rule_id="native_boundary.unexpected_verdict",
                    message=f"unexpected verdict: {result.verdict.value}",
                )
            )

        side_effects = {
            "native_called": result.native_called,
            "tool_executed": result.tool_executed,
            "provider_called": result.provider_called,
            "memory_written": result.memory_written,
            "state_mutated": result.state_mutated,
            "patch_generated": result.patch_generated,
            "secret_read": result.secret_read,
        }
        for name, enabled in side_effects.items():
            if enabled:
                violations.append(
                    NativeBoundaryContractViolation(
                        request_id=case.request.request_id,
                        rule_id=f"native_boundary.side_effect.{name}",
                        message=f"side effect flag was enabled: {name}",
                    )
                )

        if case.request.operation in NoopNativeBoundary.BLOCKED_OPERATIONS:
            if result.verdict != NativeBoundaryVerdict.BLOCKED:
                violations.append(
                    NativeBoundaryContractViolation(
                        request_id=case.request.request_id,
                        rule_id="native_boundary.mutating_operation_not_blocked",
                        message=f"mutating operation was not blocked: {case.request.operation.value}",
                    )
                )

        return violations

    @staticmethod
    def _case(
        name: str,
        kind: NativeBoundaryKind,
        operation: NativeBoundaryOperation,
        target: str,
    ) -> NativeBoundaryContractCase:
        return NativeBoundaryContractCase(
            name=name,
            request=NativeBoundaryRequest(
                kind=kind,
                operation=operation,
                target=target,
                payload={"phase": 9, "synthetic": True},
            ),
        )

    @staticmethod
    def _operation_from_mode(mode: IntegrationMode) -> NativeBoundaryOperation:
        if mode == IntegrationMode.FORBIDDEN:
            return NativeBoundaryOperation.PATCH
        if mode == IntegrationMode.FEATURE_FLAG_SHADOW:
            return NativeBoundaryOperation.EXECUTE
        if mode == IntegrationMode.EXTERNAL_WRAPPER:
            return NativeBoundaryOperation.CALL
        if mode == IntegrationMode.SIDE_CAR_OBSERVER:
            return NativeBoundaryOperation.OBSERVE
        if mode == IntegrationMode.EXTERNAL_HARNESS:
            return NativeBoundaryOperation.ADAPT
        return NativeBoundaryOperation.READ

    @staticmethod
    def _kind_from_surface(surface: str) -> NativeBoundaryKind:
        mapping = {
            "tool_registry": NativeBoundaryKind.TOOL,
            "tool_orchestration": NativeBoundaryKind.TOOL,
            "memory": NativeBoundaryKind.MEMORY,
            "provider": NativeBoundaryKind.PROVIDER,
            "prompt": NativeBoundaryKind.PROMPT,
            "context": NativeBoundaryKind.CONTEXT,
            "gateway": NativeBoundaryKind.GATEWAY,
            "cron": NativeBoundaryKind.CRON,
            "state_db": NativeBoundaryKind.STATE,
            "security": NativeBoundaryKind.SECURITY,
            "cli": NativeBoundaryKind.SECURITY,
            "runtime_loop": NativeBoundaryKind.SECURITY,
        }
        return mapping.get(surface, NativeBoundaryKind.UNKNOWN)