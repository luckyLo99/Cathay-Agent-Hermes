from __future__ import annotations

from collections.abc import Callable
from typing import Protocol

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.hooks.contracts import (
    HookDecision,
    HookDecisionType,
    HookEvent,
    HookEventName,
    HookResult,
)


class HookHandler(Protocol):
    name: str

    def handle(self, event: HookEvent) -> HookDecision:
        ...


HookCallable = Callable[[HookEvent], HookDecision]


class RegisteredHandler(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", arbitrary_types_allowed=True)

    name: str
    event_name: HookEventName
    priority: int = Field(default=100, ge=0, le=10_000)
    handler: HookCallable


class HookDispatcher:
    """
    Deterministic in-process hook dispatcher.

    Decision precedence:
    DENY > ASK > WARN > ALLOW > NOOP

    Payload rewrite:
    - only decisions with updated_payload participate
    - later handlers can see earlier payload updates only in final result,
      not during the same dispatch, to keep Phase 2 deterministic and simple
    """

    def __init__(self) -> None:
        self._handlers: list[RegisteredHandler] = []

    def register(
        self,
        event_name: HookEventName,
        handler: HookCallable,
        *,
        name: str,
        priority: int = 100,
    ) -> None:
        self._handlers.append(
            RegisteredHandler(
                name=name,
                event_name=event_name,
                priority=priority,
                handler=handler,
            )
        )
        self._handlers.sort(key=lambda item: (item.priority, item.name))

    def dispatch(self, event: HookEvent) -> HookResult:
        matched = [
            registered
            for registered in self._handlers
            if registered.event_name == event.event_name
        ]

        decisions: list[HookDecision] = []
        effective_payload = dict(event.payload)

        for registered in matched:
            decision = registered.handler(event)
            if decision.handler_name == "unknown":
                decision = decision.model_copy(update={"handler_name": registered.name})
            decisions.append(decision)

            if decision.updated_payload is not None:
                effective_payload.update(decision.updated_payload)

        final_decision = self._reduce_decisions(decisions)

        return HookResult(
            event_id=event.event_id,
            event_name=event.event_name,
            final_decision=final_decision,
            decisions=decisions,
            effective_payload=effective_payload,
        )

    @staticmethod
    def _reduce_decisions(decisions: list[HookDecision]) -> HookDecisionType:
        if not decisions:
            return HookDecisionType.NOOP

        order = [
            HookDecisionType.DENY,
            HookDecisionType.ASK,
            HookDecisionType.WARN,
            HookDecisionType.ALLOW,
            HookDecisionType.NOOP,
        ]

        decision_types = {decision.decision for decision in decisions}
        for item in order:
            if item in decision_types:
                return item

        return HookDecisionType.NOOP