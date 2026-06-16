from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stable_json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class MemoryNodeKind(str, Enum):
    OBSERVATION = "observation"
    SAFETY_SIGNAL = "safety_signal"
    PROFILE_HYPOTHESIS = "profile_hypothesis"
    LEARNING_SIGNAL = "learning_signal"
    PROACTIVE_SUGGESTION = "proactive_suggestion"
    ENVELOPE_METADATA = "envelope_metadata"
    SUMMARY = "summary"


class MemoryNodeStatus(str, Enum):
    SHADOW = "shadow"
    QUARANTINED = "quarantined"
    REJECTED = "rejected"
    PROMOTION_CANDIDATE = "promotion_candidate"


class MemoryPIILevel(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class MemoryEdgeType(str, Enum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    UPDATES = "updates"
    DEPENDS_ON = "depends_on"
    DERIVED_FROM = "derived_from"


class ShadowMemoryNode(BaseModel):
    """
    Shadow memory node.

    This is not Hermes native memory.
    It is an isolated, auditable, disposable memory candidate.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    node_id: str = Field(default_factory=lambda: str(uuid4()))
    trace_id: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    turn_id: str = Field(min_length=1)
    kind: MemoryNodeKind
    status: MemoryNodeStatus = MemoryNodeStatus.SHADOW
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    content_hash: str = ""
    source: str = "phase4"
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    pii_level: MemoryPIILevel = MemoryPIILevel.NONE
    created_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("node_id", "trace_id", "session_id", "turn_id", "title", "content", "source")
    @classmethod
    def text_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("text fields must not be empty")
        if "\x00" in value:
            raise ValueError("text fields must not contain null bytes")
        return value

    @model_validator(mode="after")
    def high_pii_must_be_quarantined(self) -> "ShadowMemoryNode":
        if self.pii_level == MemoryPIILevel.HIGH and self.status != MemoryNodeStatus.QUARANTINED:
            raise ValueError("high PII shadow memory must be quarantined")
        return self

    def with_hash(self) -> "ShadowMemoryNode":
        payload = {
            "kind": self.kind.value,
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "metadata": self.metadata,
        }
        return self.model_copy(update={"content_hash": sha256_text(stable_json_dumps(payload))})


class ShadowMemoryEdge(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    edge_id: str = Field(default_factory=lambda: str(uuid4()))
    source_node_id: str = Field(min_length=1)
    target_node_id: str = Field(min_length=1)
    edge_type: MemoryEdgeType
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    reason: str = Field(min_length=1)
    created_at: datetime = Field(default_factory=utc_now)

    @field_validator("source_node_id", "target_node_id", "reason")
    @classmethod
    def fields_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("edge fields must not be empty")
        if "\x00" in value:
            raise ValueError("edge fields must not contain null bytes")
        return value

    @model_validator(mode="after")
    def no_self_edge(self) -> "ShadowMemoryEdge":
        if self.source_node_id == self.target_node_id:
            raise ValueError("self edges are not allowed")
        return self


class ShadowMemoryWriteRequest(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    node: ShadowMemoryNode
    edges: list[ShadowMemoryEdge] = Field(default_factory=list)
    allow_quarantine: bool = True

    @model_validator(mode="after")
    def validate_quarantine_policy(self) -> "ShadowMemoryWriteRequest":
        if self.node.status == MemoryNodeStatus.QUARANTINED and not self.allow_quarantine:
            raise ValueError("quarantined node rejected by write request")
        return self


class ShadowMemoryQuery(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    query: str = Field(min_length=1)
    limit: int = Field(default=10, ge=1, le=50)
    include_quarantined: bool = False
    kinds: list[MemoryNodeKind] = Field(default_factory=list)

    @field_validator("query")
    @classmethod
    def query_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("query must not be empty")
        if "\x00" in value:
            raise ValueError("query must not contain null bytes")
        return value


class ShadowMemoryRecallResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    node: ShadowMemoryNode
    score: float = Field(ge=0.0)
    matched_by: str = "keyword"