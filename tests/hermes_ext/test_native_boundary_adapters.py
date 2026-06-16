from __future__ import annotations

from hermes_ext.native_boundary.adapters import (
    NoopGatewayBoundaryAdapter,
    NoopMemoryBoundaryAdapter,
    NoopProviderBoundaryAdapter,
    NoopStateBoundaryAdapter,
    NoopToolBoundaryAdapter,
)
from hermes_ext.native_boundary.contracts import NativeBoundaryVerdict


def test_tool_adapter_never_executes_tool() -> None:
    result = NoopToolBoundaryAdapter().before_tool_use(
        tool_name="bash",
        payload={"argv": ["rm", "-rf", "/"]},
    )

    assert result.verdict == NativeBoundaryVerdict.BLOCKED
    assert not result.tool_executed


def test_memory_adapter_never_writes_native_memory() -> None:
    result = NoopMemoryBoundaryAdapter().before_memory_write(
        memory_key="user_preference",
        payload={"value": "stability first"},
    )

    assert result.verdict == NativeBoundaryVerdict.BLOCKED
    assert not result.memory_written


def test_provider_adapter_never_calls_provider() -> None:
    result = NoopProviderBoundaryAdapter().before_provider_call(
        provider_name="openai",
        payload={"model": "real-model"},
    )

    assert result.verdict == NativeBoundaryVerdict.BLOCKED
    assert not result.provider_called


def test_gateway_adapter_observes_only() -> None:
    result = NoopGatewayBoundaryAdapter().observe_gateway_event(
        event_name="session_start",
        payload={"session": "x"},
    )

    assert result.verdict == NativeBoundaryVerdict.NOOP
    assert not result.native_called


def test_state_adapter_never_mutates_state() -> None:
    result = NoopStateBoundaryAdapter().before_state_mutation(
        state_key="hermes_state",
        payload={"mutation": True},
    )

    assert result.verdict == NativeBoundaryVerdict.BLOCKED
    assert not result.state_mutated