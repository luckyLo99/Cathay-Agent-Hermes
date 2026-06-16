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


class NativeBoundaryKind(str, Enum):
    TOOL = "tool"
    MEMORY = "memory"
    PROVIDER = "provider"
    PROMPT = "prompt"
    CONTEXT = "context"
    GATEWAY = "gateway"
    STATE = "state"
    CRON = "cron"
    SECURITY = "security"
    UNKNOWN = "unknown"


class NativeBoundaryOperation(str, Enum):
    OBSERVE = "observe"
    READ = "read"
    ADAPT = "adapt"
    CALL = "call"
    EXECUTE = "execute"
    WRITE = "write"
    MUTATE = "mutate"
    REGISTER = "register"
    PATCH = "patch"


class NativeBoundaryVerdict(str, Enum):
    NOOP = "noop"
    BLOCKED = "blocked"


class NativeBoundaryEffect(str, Enum):
    AUDIT_ONLY = "audit_only"
    NO_NATIVE_CALL = "no_native_call"
    NO_TOOL_EXECUTION = "no_tool_execution"
    NO_PROVIDER_CALL = "no_provider_call"
    NO_MEMORY_WRITE = "no_memory_write"
    NO_STATE_MUTATION = "no_state_mutation"
    NO_PATCH_GENERATION = "no_patch_generation"
    NO_SECRET_READ = "no_secret_read"


class NativeBoundaryRequest(BaseModel):
    """
    Request for a conceptual native boundary.

    This object is a contract input only.
    It is not allowed to invoke Hermes native code.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    request_id: str = Field(default_factory=lambda: str(uuid4()))
    trace_id: str = Field(default_factory=lambda: str(uuid4()))
    session_id: str = Field(default_factory=lambda: str(uuid4()))
    turn_id: str = Field(default_factory=lambda: str(uuid4()))
    kind: NativeBoundaryKind
    operation: NativeBoundaryOperation
    target: str = Field(default="shadow-native-boundary", min_length=1)
    payload: dict[str, Any] = Field(default_factory=dict)
    source: str = "phase9"
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("request_id", "trace_id", "session_id", "turn_id", "target", "source")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("boundary request text fields must not be empty")
        if "\x00" in value:
            raise ValueError("boundary request text fields must not contain null bytes")
        return value

    def stable_fingerprint(self) -> str:
        payload = {
            "kind": self.kind.value,
            "operation": self.operation.value,
            "target": self.target,
            "payload": self.payload,
            "source": self.source,
            "metadata": self.metadata,
        }
        return sha256_text(stable_json_dumps(payload))


class NativeBoundaryResult(BaseModel):
    """
    Result returned by the no-op native boundary.

    The validator is the safety rail: any side effect flag set to True is invalid.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    result_id: str = Field(default_factory=lambda: str(uuid4()))
    request_id: str = Field(min_length=1)
    verdict: NativeBoundaryVerdict
    reason: str = Field(min_length=1)
    effects: list[NativeBoundaryEffect] = Field(default_factory=list)

    native_called: bool = False
    tool_executed: bool = False
    provider_called: bool = False
    memory_written: bool = False
    state_mutated: bool = False
    patch_generated: bool = False
    secret_read: bool = False

    created_at: datetime = Field(default_factory=utc_now)
    audit: dict[str, Any] = Field(default_factory=dict)

    @field_validator("result_id", "request_id", "reason")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("boundary result text fields must not be empty")
        if "\x00" in value:
            raise ValueError("boundary result text fields must not contain null bytes")
        return value

    @model_validator(mode="after")
    def assert_no_side_effects(self) -> "NativeBoundaryResult":
        side_effects = {
            "native_called": self.native_called,
            "tool_executed": self.tool_executed,
            "provider_called": self.provider_called,
            "memory_written": self.memory_written,
            "state_mutated": self.state_mutated,
            "patch_generated": self.patch_generated,
            "secret_read": self.secret_read,
        }
        active = [name for name, enabled in side_effects.items() if enabled]
        if active:
            raise ValueError(f"no-op boundary result cannot contain side effects: {active}")
        return self

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")


class NativeBoundaryContractViolation(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    violation_id: str = Field(default_factory=lambda: str(uuid4()))
    request_id: str = Field(min_length=1)
    rule_id: str = Field(min_length=1)
    message: str = Field(min_length=1)
    severity: str = "critical"

    @field_validator("request_id", "rule_id", "message", "severity")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("violation fields must not be empty")
        if "\x00" in value:
            raise ValueError("violation fields must not contain null bytes")
        return value


class NativeBoundaryContractCase(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    case_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str = Field(min_length=1)
    request: NativeBoundaryRequest
    expected_verdicts: list[NativeBoundaryVerdict] = Field(
        default_factory=lambda: [NativeBoundaryVerdict.NOOP, NativeBoundaryVerdict.BLOCKED]
    )

    @field_validator("name")
    @classmethod
    def clean_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("case name must not be empty")
        if "\x00" in value:
            raise ValueError("case name must not contain null bytes")
        return value


class NativeBoundaryContractRunResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    run_id: str = Field(default_factory=lambda: str(uuid4()))
    ok: bool
    case_count: int = Field(ge=0)
    passed: int = Field(ge=0)
    failed: int = Field(ge=0)
    results: list[NativeBoundaryResult] = Field(default_factory=list)
    violations: list[NativeBoundaryContractViolation] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def counts_must_match(self) -> "NativeBoundaryContractRunResult":
        if self.case_count != self.passed + self.failed:
            raise ValueError("case_count must equal passed + failed")
        if self.ok and self.failed != 0:
            raise ValueError("ok result cannot have failures")
        return self

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")