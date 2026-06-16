from __future__ import annotations

import pytest
from pydantic import ValidationError

from hermes_ext.hooks.contracts import (
    HookDecision,
    HookDecisionType,
    HookEvent,
    HookEventName,
)


def test_pre_tool_use_event_factory() -> None:
    event = HookEvent.pre_tool_use(
        trace_id="trace-1",
        session_id="session-1",
        turn_id="turn-1",
        tool_name="bash",
        payload={"argv": ["git", "status"]},
    )

    assert event.event_name == HookEventName.PRE_TOOL_USE
    assert event.tool_name == "bash"
    assert event.payload["argv"] == ["git", "status"]


def test_hook_decision_helpers() -> None:
    decision = HookDecision.deny("blocked", handler_name="test")

    assert decision.decision == HookDecisionType.DENY
    assert decision.reason == "blocked"
    assert decision.handler_name == "test"


def test_hook_event_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        HookEvent(
            event_name=HookEventName.SESSION_START,
            trace_id="trace",
            session_id="session",
            extra_field=True,  # type: ignore[call-arg]
        )