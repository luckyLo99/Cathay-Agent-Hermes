from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class HookEventName(str, Enum):
    SESSION_START = "SessionStart"
    USER_PROMPT_SUBMIT = "UserPromptSubmit"
    PRE_TOOL_USE = "PreToolUse"
    POST_TOOL_USE = "PostToolUse"
    STOP = "Stop"
    SUBAGENT_STOP = "SubagentStop"
    PRE_COMPACT = "PreCompact"


class HookDecisionType(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    ASK = "ask"
    WARN = "warn"
    NOOP = "noop"


class HookEvent(BaseModel):
    """
    Portable hook event.

    This is intentionally similar to Claude Code's lifecycle hook concept,
    but does not depend on Claude Code or Hermes internals.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    event_id: str = Field(default_factory=lambda: str(uuid4()))
    event_name: HookEventName
    trace_id: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    turn_id: str | None = None
    tool_name: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=utc_now)

    @field_validator("event_id", "trace_id", "session_id")
    @classmethod
    def non_empty_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("field must not be empty")
        if "\x00" in value:
            raise ValueError("field must not contain null bytes")
        return value

    @field_validator("tool_name")
    @classmethod
    def optional_tool_name_must_be_clean(cls, value: str | None) -> str | None:
        if value is None:
            return None
        value = value.strip()
        if not value:
            raise ValueError("tool_name must not be empty when provided")
        if "\x00" in value:
            raise ValueError("tool_name must not contain null bytes")
        return value

    @classmethod
    def pre_tool_use(
        cls,
        *,
        trace_id: str,
        session_id: str,
        tool_name: str,
        payload: dict[str, Any],
        turn_id: str | None = None,
    ) -> "HookEvent":
        return cls(
            event_name=HookEventName.PRE_TOOL_USE,
            trace_id=trace_id,
            session_id=session_id,
            turn_id=turn_id,
            tool_name=tool_name,
            payload=payload,
        )


class HookDecision(BaseModel):
    """
    Decision emitted by a hook handler.

    allow: continue
    warn: continue but record warning
    ask: requires human approval
    deny: block
    noop: no opinion
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    decision: HookDecisionType = HookDecisionType.NOOP
    reason: str = ""
    handler_name: str = "unknown"
    updated_payload: dict[str, Any] | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("reason")
    @classmethod
    def reason_must_be_text(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("reason must not contain null bytes")
        return value

    @classmethod
    def allow(cls, reason: str, *, handler_name: str) -> "HookDecision":
        return cls(decision=HookDecisionType.ALLOW, reason=reason, handler_name=handler_name)

    @classmethod
    def deny(cls, reason: str, *, handler_name: str) -> "HookDecision":
        return cls(decision=HookDecisionType.DENY, reason=reason, handler_name=handler_name)

    @classmethod
    def ask(cls, reason: str, *, handler_name: str) -> "HookDecision":
        return cls(decision=HookDecisionType.ASK, reason=reason, handler_name=handler_name)

    @classmethod
    def warn(cls, reason: str, *, handler_name: str) -> "HookDecision":
        return cls(decision=HookDecisionType.WARN, reason=reason, handler_name=handler_name)

    @classmethod
    def noop(cls, *, handler_name: str) -> "HookDecision":
        return cls(decision=HookDecisionType.NOOP, reason="", handler_name=handler_name)


class HookResult(BaseModel):
    """
    Aggregated result after dispatching one hook event.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    event_id: str
    event_name: HookEventName
    final_decision: HookDecisionType
    decisions: list[HookDecision] = Field(default_factory=list)
    effective_payload: dict[str, Any] = Field(default_factory=dict)

    @property
    def allowed(self) -> bool:
        return self.final_decision in {
            HookDecisionType.ALLOW,
            HookDecisionType.WARN,
            HookDecisionType.NOOP,
        }

    @property
    def blocked(self) -> bool:
        return self.final_decision == HookDecisionType.DENY

    @property
    def requires_approval(self) -> bool:
        return self.final_decision == HookDecisionType.ASK