from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stable_json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class CathaySignalSource(str, Enum):
    RAW_PAYLOAD = "raw_payload"
    SAFETY_BRIDGE = "safety_bridge"
    PROFILE_BRIDGE = "profile_bridge"
    LEARNING_BRIDGE = "learning_bridge"
    PROACTIVE_BRIDGE = "proactive_bridge"
    SIGNAL_FUSION = "signal_fusion"


class CathaySignalSeverity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class CathayIntent(str, Enum):
    UNKNOWN = "unknown"
    CODING = "coding"
    LEARNING = "learning"
    REFLECTION = "reflection"
    PLANNING = "planning"
    EMOTIONAL_SUPPORT = "emotional_support"
    SYSTEM_OPERATION = "system_operation"


class CathayAdapterMode(str, Enum):
    OFF = "off"
    OBSERVE_ONLY = "observe_only"
    ADVISE_ONLY = "advise_only"


class CathayTextObservation(BaseModel):
    """
    Read-only turn observation.

    This is a portable representation of the current user turn.
    It does not include model hidden reasoning and does not store memory.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    role: Literal["user", "assistant", "system", "tool", "context"] = "user"
    text: str = Field(min_length=0)
    source: str = "turn"
    created_at: datetime = Field(default_factory=utc_now)
    content_hash: str = ""

    @field_validator("text", "source")
    @classmethod
    def reject_null_bytes(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("text fields must not contain null bytes")
        return value

    def with_hash(self) -> "CathayTextObservation":
        return self.model_copy(update={"content_hash": sha256_text(self.text)})


class CathayAdapterInput(BaseModel):
    """
    Input to CathayContractAdapter.

    raw_cathay_payload is allowed but never trusted.
    It is normalized into typed read-only signals.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    trace_id: str = Field(default_factory=lambda: str(uuid4()))
    session_id: str = Field(default_factory=lambda: str(uuid4()))
    turn_id: str = Field(default_factory=lambda: str(uuid4()))
    mode: CathayAdapterMode = CathayAdapterMode.OBSERVE_ONLY
    observations: list[CathayTextObservation] = Field(default_factory=list)
    raw_cathay_payload: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("trace_id", "session_id", "turn_id")
    @classmethod
    def non_empty_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("id fields must not be empty")
        if "\x00" in value:
            raise ValueError("id fields must not contain null bytes")
        return value

    def prepared(self) -> "CathayAdapterInput":
        return self.model_copy(
            update={
                "observations": [item.with_hash() for item in self.observations],
            }
        )


class CathayBaseSignal(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    signal_id: str = Field(default_factory=lambda: str(uuid4()))
    source: CathaySignalSource
    severity: CathaySignalSeverity = CathaySignalSeverity.INFO
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    reason: str = Field(min_length=1)
    evidence: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("reason")
    @classmethod
    def reason_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("reason must not be empty")
        if "\x00" in value:
            raise ValueError("reason must not contain null bytes")
        return value

    @field_validator("evidence")
    @classmethod
    def evidence_must_be_clean(cls, value: list[str]) -> list[str]:
        for item in value:
            if "\x00" in item:
                raise ValueError("evidence must not contain null bytes")
        return value


class CathaySafetySignal(CathayBaseSignal):
    """
    Safety signal from Cathay-style analysis.

    It is advisory unless converted into a Hook/PreTool policy elsewhere.
    """

    category: Literal[
        "allow",
        "crisis",
        "diagnosis",
        "dependency",
        "prompt_injection",
        "tool_risk",
        "privacy",
        "unknown",
    ] = "unknown"
    should_block: bool = False
    requires_human_review: bool = False

    @model_validator(mode="after")
    def ensure_high_severity_blocks_or_reviews(self) -> "CathaySafetySignal":
        if self.severity in {CathaySignalSeverity.HIGH, CathaySignalSeverity.CRITICAL}:
            if not self.should_block and not self.requires_human_review:
                raise ValueError("high/critical safety signals must block or require review")
        return self


class CathayProfileHypothesis(CathayBaseSignal):
    """
    User profile hypothesis.

    This is a hypothesis, never a permanent truth.
    Phase 3 does not write it to memory.
    """

    key: str = Field(min_length=1)
    value: str = Field(min_length=1)
    hypothesis_type: Literal[
        "preference",
        "skill_level",
        "communication_style",
        "goal",
        "constraint",
        "working_context",
        "unknown",
    ] = "unknown"
    is_sensitive: bool = False
    write_permission: Literal["forbidden", "requires_review"] = "requires_review"

    @field_validator("key", "value")
    @classmethod
    def key_value_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("profile key/value must not be empty")
        if "\x00" in value:
            raise ValueError("profile key/value must not contain null bytes")
        return value

    @model_validator(mode="after")
    def sensitive_profile_must_be_forbidden(self) -> "CathayProfileHypothesis":
        if self.is_sensitive and self.write_permission != "forbidden":
            raise ValueError("sensitive profile hypotheses must be write-forbidden")
        return self


class CathayLearningSignal(CathayBaseSignal):
    skill_area: str = Field(min_length=1)
    learner_state: Literal[
        "unknown",
        "novice",
        "practicing",
        "blocked",
        "ready_for_challenge",
        "mastery_candidate",
    ] = "unknown"
    suggested_method: Literal[
        "none",
        "socratic_question",
        "retrieval_practice",
        "worked_example",
        "spaced_repetition",
        "project_based",
    ] = "none"
    should_create_skill: bool = False
    skill_write_permission: Literal["forbidden", "requires_review"] = "requires_review"

    @field_validator("skill_area")
    @classmethod
    def skill_area_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("skill_area must not be empty")
        if "\x00" in value:
            raise ValueError("skill_area must not contain null bytes")
        return value


class CathayProactiveSuggestion(CathayBaseSignal):
    """
    A proactive suggestion is not a notification.

    Phase 3 only emits suggestions; it must not schedule or send them.
    """

    suggestion_type: Literal[
        "none",
        "follow_up_question",
        "learning_review",
        "task_checkpoint",
        "safety_reminder",
        "reflection_prompt",
    ] = "none"
    message: str = Field(min_length=1)
    allowed_to_notify: bool = False
    requires_user_consent: bool = True

    @field_validator("message")
    @classmethod
    def message_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("proactive message must not be empty")
        if "\x00" in value:
            raise ValueError("proactive message must not contain null bytes")
        return value

    @model_validator(mode="after")
    def phase3_never_allows_notification(self) -> "CathayProactiveSuggestion":
        if self.allowed_to_notify:
            raise ValueError("Phase 3 proactive suggestions must not notify")
        return self


class CathaySignalBundle(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    trace_id: str
    session_id: str
    turn_id: str
    intent: CathayIntent = CathayIntent.UNKNOWN
    safety: list[CathaySafetySignal] = Field(default_factory=list)
    profile: list[CathayProfileHypothesis] = Field(default_factory=list)
    learning: list[CathayLearningSignal] = Field(default_factory=list)
    proactive: list[CathayProactiveSuggestion] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=utc_now)
    bundle_hash: str = ""

    @field_validator("trace_id", "session_id", "turn_id")
    @classmethod
    def ids_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("bundle ids must not be empty")
        if "\x00" in value:
            raise ValueError("bundle ids must not contain null bytes")
        return value

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"bundle_hash"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "CathaySignalBundle":
        return self.model_copy(update={"bundle_hash": self.compute_hash()})

    def has_blocking_safety(self) -> bool:
        return any(item.should_block for item in self.safety)

    def requires_review(self) -> bool:
        if any(item.requires_human_review for item in self.safety):
            return True
        if any(item.write_permission == "requires_review" for item in self.profile):
            return True
        if any(item.skill_write_permission == "requires_review" for item in self.learning):
            return True
        if any(item.requires_user_consent for item in self.proactive):
            return True
        return False


class CathayAdapterOutput(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    ok: bool
    mode: CathayAdapterMode
    bundle: CathaySignalBundle | None = None
    error: str | None = None
    warnings: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_output_shape(self) -> "CathayAdapterOutput":
        if self.ok and self.bundle is None:
            raise ValueError("ok output requires bundle")
        if not self.ok and not self.error:
            raise ValueError("failed output requires error")
        return self