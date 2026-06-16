from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from hermes_ext.hooks.contracts import HookDecision, HookDecisionType


class SecurityDecisionType(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    ASK = "ask"
    WARN = "warn"


class SecurityDecision(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    decision: SecurityDecisionType
    reason: str
    rule_id: str = "unknown"
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("reason", "rule_id")
    @classmethod
    def text_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("field must not be empty")
        if "\x00" in value:
            raise ValueError("field must not contain null bytes")
        return value

    @classmethod
    def allow(cls, reason: str, *, rule_id: str = "allow", metadata: dict[str, Any] | None = None) -> "SecurityDecision":
        return cls(decision=SecurityDecisionType.ALLOW, reason=reason, rule_id=rule_id, metadata=metadata or {})

    @classmethod
    def deny(cls, reason: str, *, rule_id: str = "deny", metadata: dict[str, Any] | None = None) -> "SecurityDecision":
        return cls(decision=SecurityDecisionType.DENY, reason=reason, rule_id=rule_id, metadata=metadata or {})

    @classmethod
    def ask(cls, reason: str, *, rule_id: str = "ask", metadata: dict[str, Any] | None = None) -> "SecurityDecision":
        return cls(decision=SecurityDecisionType.ASK, reason=reason, rule_id=rule_id, metadata=metadata or {})

    @classmethod
    def warn(cls, reason: str, *, rule_id: str = "warn", metadata: dict[str, Any] | None = None) -> "SecurityDecision":
        return cls(decision=SecurityDecisionType.WARN, reason=reason, rule_id=rule_id, metadata=metadata or {})

    def to_hook_decision(self, *, handler_name: str) -> HookDecision:
        mapping = {
            SecurityDecisionType.ALLOW: HookDecisionType.ALLOW,
            SecurityDecisionType.DENY: HookDecisionType.DENY,
            SecurityDecisionType.ASK: HookDecisionType.ASK,
            SecurityDecisionType.WARN: HookDecisionType.WARN,
        }
        return HookDecision(
            decision=mapping[self.decision],
            reason=self.reason,
            handler_name=handler_name,
            metadata={
                "rule_id": self.rule_id,
                **self.metadata,
            },
        )