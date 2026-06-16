from __future__ import annotations

from hermes_ext.hooks.contracts import HookDecision, HookDecisionType, HookEvent, HookEventName
from hermes_ext.hooks.dispatcher import HookDispatcher


def make_event() -> HookEvent:
    return HookEvent(
        event_name=HookEventName.PRE_TOOL_USE,
        trace_id="trace",
        session_id="session",
        tool_name="bash",
        payload={"argv": ["git", "status"]},
    )


def test_dispatcher_no_handlers_returns_noop() -> None:
    result = HookDispatcher().dispatch(make_event())

    assert result.final_decision == HookDecisionType.NOOP
    assert result.allowed


def test_dispatcher_denies_over_allow() -> None:
    dispatcher = HookDispatcher()

    dispatcher.register(
        HookEventName.PRE_TOOL_USE,
        lambda event: HookDecision.allow("ok", handler_name="allow"),
        name="allow",
        priority=20,
    )
    dispatcher.register(
        HookEventName.PRE_TOOL_USE,
        lambda event: HookDecision.deny("no", handler_name="deny"),
        name="deny",
        priority=30,
    )

    result = dispatcher.dispatch(make_event())

    assert result.final_decision == HookDecisionType.DENY
    assert result.blocked


def test_dispatcher_ask_over_warn() -> None:
    dispatcher = HookDispatcher()

    dispatcher.register(
        HookEventName.PRE_TOOL_USE,
        lambda event: HookDecision.warn("warn", handler_name="warn"),
        name="warn",
    )
    dispatcher.register(
        HookEventName.PRE_TOOL_USE,
        lambda event: HookDecision.ask("ask", handler_name="ask"),
        name="ask",
    )

    result = dispatcher.dispatch(make_event())

    assert result.final_decision == HookDecisionType.ASK
    assert result.requires_approval


def test_dispatcher_payload_update_is_collected() -> None:
    dispatcher = HookDispatcher()

    def handler(event: HookEvent) -> HookDecision:
        return HookDecision(
            decision=HookDecisionType.ALLOW,
            reason="normalized",
            handler_name="normalizer",
            updated_payload={"normalized": True},
        )

    dispatcher.register(HookEventName.PRE_TOOL_USE, handler, name="normalizer")

    result = dispatcher.dispatch(make_event())

    assert result.effective_payload["normalized"] is True