from __future__ import annotations

from typing import Any

from hermes_ext.native_boundary.contracts import (
    NativeBoundaryKind,
    NativeBoundaryOperation,
    NativeBoundaryRequest,
    NativeBoundaryResult,
)
from hermes_ext.native_boundary.noop_boundary import NoopNativeBoundary


class _BaseNoopBoundaryAdapter:
    def __init__(self, boundary: NoopNativeBoundary | None = None) -> None:
        self.boundary = boundary or NoopNativeBoundary()

    def _request(
        self,
        *,
        kind: NativeBoundaryKind,
        operation: NativeBoundaryOperation,
        target: str,
        payload: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> NativeBoundaryRequest:
        return NativeBoundaryRequest(
            kind=kind,
            operation=operation,
            target=target,
            payload=payload or {},
            metadata=metadata or {},
        )


class NoopToolBoundaryAdapter(_BaseNoopBoundaryAdapter):
    """
    Tool boundary adapter.

    It only builds a contract request and returns no-op/block result.
    It does not execute tools.
    """

    def before_tool_use(
        self,
        *,
        tool_name: str,
        payload: dict[str, Any] | None = None,
    ) -> NativeBoundaryResult:
        request = self._request(
            kind=NativeBoundaryKind.TOOL,
            operation=NativeBoundaryOperation.EXECUTE,
            target=tool_name,
            payload=payload,
            metadata={"adapter": "NoopToolBoundaryAdapter"},
        )
        return self.boundary.handle(request)


class NoopMemoryBoundaryAdapter(_BaseNoopBoundaryAdapter):
    """
    Memory boundary adapter.

    It never writes Hermes native memory.
    """

    def before_memory_write(
        self,
        *,
        memory_key: str,
        payload: dict[str, Any] | None = None,
    ) -> NativeBoundaryResult:
        request = self._request(
            kind=NativeBoundaryKind.MEMORY,
            operation=NativeBoundaryOperation.WRITE,
            target=memory_key,
            payload=payload,
            metadata={"adapter": "NoopMemoryBoundaryAdapter"},
        )
        return self.boundary.handle(request)


class NoopProviderBoundaryAdapter(_BaseNoopBoundaryAdapter):
    """
    Provider boundary adapter.

    It never calls a real model/provider.
    """

    def before_provider_call(
        self,
        *,
        provider_name: str,
        payload: dict[str, Any] | None = None,
    ) -> NativeBoundaryResult:
        request = self._request(
            kind=NativeBoundaryKind.PROVIDER,
            operation=NativeBoundaryOperation.CALL,
            target=provider_name,
            payload=payload,
            metadata={"adapter": "NoopProviderBoundaryAdapter"},
        )
        return self.boundary.handle(request)


class NoopGatewayBoundaryAdapter(_BaseNoopBoundaryAdapter):
    """
    Gateway/session boundary adapter.

    It is observe-only and sidecar-shaped.
    """

    def observe_gateway_event(
        self,
        *,
        event_name: str,
        payload: dict[str, Any] | None = None,
    ) -> NativeBoundaryResult:
        request = self._request(
            kind=NativeBoundaryKind.GATEWAY,
            operation=NativeBoundaryOperation.OBSERVE,
            target=event_name,
            payload=payload,
            metadata={"adapter": "NoopGatewayBoundaryAdapter"},
        )
        return self.boundary.handle(request)


class NoopStateBoundaryAdapter(_BaseNoopBoundaryAdapter):
    """
    State boundary adapter.

    It never mutates Hermes native state.
    """

    def before_state_mutation(
        self,
        *,
        state_key: str,
        payload: dict[str, Any] | None = None,
    ) -> NativeBoundaryResult:
        request = self._request(
            kind=NativeBoundaryKind.STATE,
            operation=NativeBoundaryOperation.MUTATE,
            target=state_key,
            payload=payload,
            metadata={"adapter": "NoopStateBoundaryAdapter"},
        )
        return self.boundary.handle(request)


class NoopPromptBoundaryAdapter(_BaseNoopBoundaryAdapter):
    """
    Prompt/context boundary adapter.

    It never mutates Hermes prompts or context.
    """

    def before_prompt_mutation(
        self,
        *,
        prompt_target: str,
        payload: dict[str, Any] | None = None,
    ) -> NativeBoundaryResult:
        request = self._request(
            kind=NativeBoundaryKind.PROMPT,
            operation=NativeBoundaryOperation.MUTATE,
            target=prompt_target,
            payload=payload,
            metadata={"adapter": "NoopPromptBoundaryAdapter"},
        )
        return self.boundary.handle(request)