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


class ShadowStepName(str, Enum):
    PREPARE_ENVELOPE = "prepare_envelope"
    PRETOOL_GUARD = "pretool_guard"
    MOCK_PROVIDER = "mock_provider"
    CATHAY_ADAPTER = "cathay_adapter"
    SHADOW_MEMORY_WRITE = "shadow_memory_write"
    FINALIZE = "finalize"


class CheckpointKind(str, Enum):
    INPUT = "input"
    BEFORE_STEP = "before_step"
    AFTER_STEP = "after_step"
    ERROR = "error"
    FINAL = "final"


class ShadowRunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    INTERRUPTED = "interrupted"
    CIRCUIT_OPEN = "circuit_open"


class ReplayMode(str, Enum):
    FULL = "full"
    FROM_CHECKPOINT = "from_checkpoint"
    DRY_RUN = "dry_run"


class ShadowRunConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    run_id: str = Field(default_factory=lambda: str(uuid4()))
    session_id: str = Field(default_factory=lambda: str(uuid4()))
    max_steps: int = Field(default=16, ge=1, le=128)
    enable_cathay: bool = True
    enable_shadow_memory: bool = True
    enable_pretool_guard: bool = True
    fail_fast: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("run_id", "session_id")
    @classmethod
    def id_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("id must not be empty")
        if "\x00" in value:
            raise ValueError("id must not contain null bytes")
        return value


class ShadowCheckpoint(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    checkpoint_id: str = Field(default_factory=lambda: str(uuid4()))
    run_id: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    step_name: ShadowStepName
    kind: CheckpointKind
    sequence: int = Field(ge=0)
    state: dict[str, Any] = Field(default_factory=dict)
    state_hash: str = ""
    created_at: datetime = Field(default_factory=utc_now)
    error: str | None = None

    @field_validator("checkpoint_id", "run_id", "session_id")
    @classmethod
    def fields_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("checkpoint fields must not be empty")
        if "\x00" in value:
            raise ValueError("checkpoint fields must not contain null bytes")
        return value

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"state_hash"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "ShadowCheckpoint":
        return self.model_copy(update={"state_hash": self.compute_hash()})


class ShadowRunResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    run_id: str
    session_id: str
    status: ShadowRunStatus
    checkpoint_count: int = Field(ge=0)
    final_checkpoint_id: str | None = None
    error: str | None = None
    warnings: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_result_shape(self) -> "ShadowRunResult":
        if self.status == ShadowRunStatus.COMPLETED and not self.final_checkpoint_id:
            raise ValueError("completed result requires final_checkpoint_id")
        if self.status in {ShadowRunStatus.FAILED, ShadowRunStatus.CIRCUIT_OPEN} and not self.error:
            raise ValueError("failed/circuit_open result requires error")
        return self