from __future__ import annotations

import pytest
from pydantic import ValidationError

from hermes_ext.native_boundary.contracts import (
    NativeBoundaryKind,
    NativeBoundaryOperation,
    NativeBoundaryRequest,
    NativeBoundaryResult,
    NativeBoundaryVerdict,
)


def test_boundary_request_fingerprint_is_stable() -> None:
    request = NativeBoundaryRequest(
        kind=NativeBoundaryKind.TOOL,
        operation=NativeBoundaryOperation.EXECUTE,
        target="bash",
        payload={"argv": ["rm", "-rf", "/"]},
    )

    assert request.stable_fingerprint()
    assert request.stable_fingerprint() == request.stable_fingerprint()


def test_boundary_result_rejects_side_effect_flags() -> None:
    with pytest.raises(ValidationError):
        NativeBoundaryResult(
            request_id="request",
            verdict=NativeBoundaryVerdict.NOOP,
            reason="bad",
            tool_executed=True,
        )


def test_boundary_result_allows_noop_without_side_effects() -> None:
    result = NativeBoundaryResult(
        request_id="request",
        verdict=NativeBoundaryVerdict.NOOP,
        reason="audit only",
    )

    assert result.verdict == NativeBoundaryVerdict.NOOP
    assert not result.tool_executed


def test_contracts_reject_extra_fields() -> None:
    with pytest.raises(ValidationError):
        NativeBoundaryRequest(
            kind=NativeBoundaryKind.TOOL,
            operation=NativeBoundaryOperation.EXECUTE,
            unexpected=True,  # type: ignore[call-arg]
        )