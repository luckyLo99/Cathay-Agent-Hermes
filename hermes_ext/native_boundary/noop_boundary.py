from __future__ import annotations

from typing import Protocol, runtime_checkable

from hermes_ext.native_boundary.contracts import (
    NativeBoundaryEffect,
    NativeBoundaryOperation,
    NativeBoundaryRequest,
    NativeBoundaryResult,
    NativeBoundaryVerdict,
)


@runtime_checkable
class NativeBoundaryProtocol(Protocol):
    """
    Structural contract for native boundary implementations.

    A future implementation may satisfy this protocol without inheriting from Hermes core.
    """

    def handle(self, request: NativeBoundaryRequest) -> NativeBoundaryResult:
        ...


class NoopNativeBoundary:
    """
    Conservative no-op boundary.

    It never calls Hermes native code.
    Mutating or executable operations are blocked.
    Non-mutating operations are audit-only no-ops.
    """

    BLOCKED_OPERATIONS = {
        NativeBoundaryOperation.CALL,
        NativeBoundaryOperation.EXECUTE,
        NativeBoundaryOperation.WRITE,
        NativeBoundaryOperation.MUTATE,
        NativeBoundaryOperation.REGISTER,
        NativeBoundaryOperation.PATCH,
    }

    def handle(self, request: NativeBoundaryRequest) -> NativeBoundaryResult:
        verdict = (
            NativeBoundaryVerdict.BLOCKED
            if request.operation in self.BLOCKED_OPERATIONS
            else NativeBoundaryVerdict.NOOP
        )

        reason = (
            f"operation {request.operation.value} blocked by no-op native boundary"
            if verdict == NativeBoundaryVerdict.BLOCKED
            else f"operation {request.operation.value} recorded as audit-only no-op"
        )

        return NativeBoundaryResult(
            request_id=request.request_id,
            verdict=verdict,
            reason=reason,
            effects=[
                NativeBoundaryEffect.AUDIT_ONLY,
                NativeBoundaryEffect.NO_NATIVE_CALL,
                NativeBoundaryEffect.NO_TOOL_EXECUTION,
                NativeBoundaryEffect.NO_PROVIDER_CALL,
                NativeBoundaryEffect.NO_MEMORY_WRITE,
                NativeBoundaryEffect.NO_STATE_MUTATION,
                NativeBoundaryEffect.NO_PATCH_GENERATION,
                NativeBoundaryEffect.NO_SECRET_READ,
            ],
            audit={
                "kind": request.kind.value,
                "operation": request.operation.value,
                "target": request.target,
                "fingerprint": request.stable_fingerprint(),
                "phase": 9,
                "noop": True,
            },
        )