from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stable_json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class EnvelopeStatus(str, Enum):
    PENDING = "pending"
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"


class PromptSegment(BaseModel):
    """
    A normalized prompt segment.

    This is not a replacement for Hermes prompt_builder.
    It is a portable audit representation used by Phase 1 mock runtime.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    role: Literal["system", "developer", "user", "assistant", "tool", "context", "memory", "skill"]
    content: str = Field(min_length=0)
    segment_type: Literal["instruction", "conversation", "context", "memory", "tool_result", "skill"]
    cache_policy: Literal["static", "dynamic", "non_cacheable"] = "dynamic"
    source: str | None = None
    content_hash: str = Field(default="")

    @field_validator("content")
    @classmethod
    def reject_null_bytes(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("Prompt segment content must not contain null bytes")
        return value

    def with_hash(self) -> "PromptSegment":
        return self.model_copy(update={"content_hash": sha256_text(self.content)})

    @classmethod
    def from_message(
        cls,
        role: Literal["system", "developer", "user", "assistant", "tool", "context", "memory", "skill"],
        content: str,
        *,
        segment_type: Literal["instruction", "conversation", "context", "memory", "tool_result", "skill"] = "conversation",
        cache_policy: Literal["static", "dynamic", "non_cacheable"] = "dynamic",
        source: str | None = None,
    ) -> "PromptSegment":
        return cls(
            role=role,
            content=content,
            segment_type=segment_type,
            cache_policy=cache_policy,
            source=source,
        ).with_hash()


class ToolPlan(BaseModel):
    """
    Portable tool call plan.

    Phase 1 only records intent. It does not execute tools.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    name: str = Field(min_length=1)
    arguments: dict[str, Any] = Field(default_factory=dict)
    risk: Literal["low", "medium", "high", "unknown"] = "unknown"
    requires_approval: bool = False

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Tool name must not be empty")
        if "\x00" in value:
            raise ValueError("Tool name must not contain null bytes")
        return value


class LLMUsage(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    input_tokens: int = Field(default=0, ge=0)
    output_tokens: int = Field(default=0, ge=0)
    total_tokens: int = Field(default=0, ge=0)

    @classmethod
    def from_counts(cls, input_tokens: int, output_tokens: int) -> "LLMUsage":
        return cls(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
        )


class LLMResponse(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    trace_id: str
    provider: str
    model: str
    content: str
    tool_calls: list[ToolPlan] = Field(default_factory=list)
    usage: LLMUsage = Field(default_factory=LLMUsage)
    finish_reason: Literal["stop", "tool_calls", "length", "error"] = "stop"
    created_at: datetime = Field(default_factory=utc_now)

    @field_validator("trace_id", "provider", "model")
    @classmethod
    def non_empty_string(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Field must not be empty")
        return value


class LLMRequestEnvelope(BaseModel):
    """
    Stable request envelope for Phase 1.

    This is the future audit boundary:
    user input -> normalized segments -> mock provider -> response -> report.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    trace_id: str = Field(default_factory=lambda: str(uuid4()))
    session_id: str = Field(default_factory=lambda: str(uuid4()))
    turn_id: str = Field(default_factory=lambda: str(uuid4()))

    provider: str = "mock"
    model: str = "mock-offline-v1"

    messages: list[PromptSegment] = Field(default_factory=list)
    tools: list[ToolPlan] = Field(default_factory=list)

    status: EnvelopeStatus = EnvelopeStatus.PENDING
    created_at: datetime = Field(default_factory=utc_now)
    started_at: datetime | None = None
    completed_at: datetime | None = None

    input_hash: str = ""
    output_hash: str | None = None
    error: str | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("trace_id", "session_id", "turn_id", "provider", "model")
    @classmethod
    def non_empty_string(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Field must not be empty")
        if "\x00" in value:
            raise ValueError("Field must not contain null bytes")
        return value

    def compute_input_hash(self) -> str:
        payload = {
            "provider": self.provider,
            "model": self.model,
            "messages": [m.model_dump(mode="json") for m in self.messages],
            "tools": [t.model_dump(mode="json") for t in self.tools],
            "metadata": self.metadata,
        }
        return sha256_text(stable_json_dumps(payload))

    def prepared(self) -> "LLMRequestEnvelope":
        hashed_messages = [message.with_hash() for message in self.messages]
        prepared = self.model_copy(update={"messages": hashed_messages})
        return prepared.model_copy(update={"input_hash": prepared.compute_input_hash()})

    def mark_started(self) -> "LLMRequestEnvelope":
        return self.model_copy(
            update={
                "status": EnvelopeStatus.STARTED,
                "started_at": utc_now(),
                "input_hash": self.compute_input_hash() if not self.input_hash else self.input_hash,
            }
        )

    def mark_completed(self, response: LLMResponse) -> "LLMRequestEnvelope":
        output_hash = sha256_text(response.model_dump_json())
        return self.model_copy(
            update={
                "status": EnvelopeStatus.COMPLETED,
                "completed_at": utc_now(),
                "output_hash": output_hash,
                "error": None,
            }
        )

    def mark_failed(self, error: Exception | str) -> "LLMRequestEnvelope":
        error_text = str(error)
        return self.model_copy(
            update={
                "status": EnvelopeStatus.FAILED,
                "completed_at": utc_now(),
                "error": error_text,
            }
        )

    def to_audit_dict(self) -> dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "session_id": self.session_id,
            "turn_id": self.turn_id,
            "provider": self.provider,
            "model": self.model,
            "status": self.status.value,
            "input_hash": self.input_hash,
            "output_hash": self.output_hash,
            "message_count": len(self.messages),
            "tool_count": len(self.tools),
            "created_at": self.created_at.isoformat(),
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "error": self.error,
        }