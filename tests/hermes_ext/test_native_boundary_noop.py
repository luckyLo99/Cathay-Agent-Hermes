from __future__ import annotations

from hermes_ext.native_boundary.contracts import (
    NativeBoundaryKind,
    NativeBoundaryOperation,
    NativeBoundaryRequest,
    NativeBoundaryVerdict,
)
from hermes_ext.native_boundary.noop_boundary import NativeBoundaryProtocol, NoopNativeBoundary


def test_noop_boundary_satisfies_protocol() -> None:
    boundary = NoopNativeBoundary()

    assert isinstance(boundary, NativeBoundaryProtocol)


def test_noop_boundary_blocks_tool_execution() -> None:
    request = NativeBoundaryRequest(
        kind=NativeBoundaryKind.TOOL,
        operation=NativeBoundaryOperation.EXECUTE,
        target="bash",
    )

    result = NoopNativeBoundary().handle(request)

    assert result.verdict == NativeBoundaryVerdict.BLOCKED
    assert not result.native_called
    assert not result.tool_executed


def test_noop_boundary_blocks_memory_write() -> None:
    request = NativeBoundaryRequest(
        kind=NativeBoundaryKind.MEMORY,
        operation=NativeBoundaryOperation.WRITE,
        target="native_memory",
    )

    result = NoopNativeBoundary().handle(request)

    assert result.verdict == NativeBoundaryVerdict.BLOCKED
    assert not result.memory_written


def test_noop_boundary_allows_observe_as_noop() -> None:
    request = NativeBoundaryRequest(
        kind=NativeBoundaryKind.GATEWAY,
        operation=NativeBoundaryOperation.OBSERVE,
        target="session_event",
    )

    result = NoopNativeBoundary().handle(request)

    assert result.verdict == NativeBoundaryVerdict.NOOP
    assert result.audit["noop"] is True