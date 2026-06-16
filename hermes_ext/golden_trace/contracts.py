from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stable_json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class GoldenTraceKind(str, Enum):
    DIAGNOSTIC = "diagnostic"
    SHADOW_TEXT = "shadow_text"
    SHADOW_TOOL_BLOCK = "shadow_tool_block"
    SHADOW_NO_CATHAY_NO_MEMORY = "shadow_no_cathay_no_memory"
    NATIVE_BOUNDARY_SPEC = "native_boundary_spec"


class GoldenTraceStatus(str, Enum):
    PASSED = "passed"
    FAILED = "failed"


class GoldenTraceCase(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    case_id: str
    name: str = Field(min_length=1)
    kind: GoldenTraceKind
    text: str = ""
    flags: dict[str, bool] = Field(default_factory=dict)
    tool_payload: dict[str, Any] | None = None
    expected_ok: bool = True
    expected_shadow_status: str | None = None
    expected_blocked: bool | None = None
    expected_native_violations: int | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("case_id", "name")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("golden trace text fields must not be empty")
        if "\x00" in value:
            raise ValueError("golden trace text fields must not contain null bytes")
        return value

    @field_validator("text")
    @classmethod
    def clean_optional_text(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("golden trace text must not contain null bytes")
        return value


class GoldenTracePack(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    pack_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str = "phase10-default-golden-trace-pack"
    version: str = "1"
    cases: list[GoldenTraceCase] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("name", "version")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("pack fields must not be empty")
        if "\x00" in value:
            raise ValueError("pack fields must not contain null bytes")
        return value

    @model_validator(mode="after")
    def must_have_cases(self) -> "GoldenTracePack":
        if not self.cases:
            raise ValueError("golden trace pack must contain at least one case")
        return self


class GoldenTraceRunConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    project_root: Path
    state_dir: Path
    repeat: int = Field(default=2, ge=1, le=10)
    spec_json: Path | None = None
    native_boundary_limit: int = Field(default=100, ge=1, le=10_000)
    fail_fast: bool = True

    @field_validator("project_root", "state_dir")
    @classmethod
    def normalize_path(cls, value: Path) -> Path:
        return value.resolve()

    @field_validator("spec_json")
    @classmethod
    def normalize_optional_path(cls, value: Path | None) -> Path | None:
        return value.resolve() if value is not None else None


class GoldenTraceCaseResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    case_id: str
    iteration: int = Field(ge=0)
    ok: bool
    status: GoldenTraceStatus
    canonical_hash: str
    normalized_output: dict[str, Any]
    error: str | None = None
    warnings: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)

    @field_validator("case_id", "canonical_hash")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("result fields must not be empty")
        if "\x00" in value:
            raise ValueError("result fields must not contain null bytes")
        return value


class GoldenTraceReplayReport(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    report_id: str = Field(default_factory=lambda: str(uuid4()))
    pack_id: str
    ok: bool
    repeat: int = Field(ge=1)
    case_count: int = Field(ge=0)
    result_count: int = Field(ge=0)
    passed: int = Field(ge=0)
    failed: int = Field(ge=0)
    stable_cases: int = Field(ge=0)
    unstable_cases: int = Field(ge=0)
    results: list[GoldenTraceCaseResult] = Field(default_factory=list)
    violations: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)
    report_hash: str = ""

    @model_validator(mode="after")
    def counts_must_match(self) -> "GoldenTraceReplayReport":
        if self.result_count != len(self.results):
            raise ValueError("result_count must match results length")
        if self.result_count != self.passed + self.failed:
            raise ValueError("result_count must equal passed + failed")
        if self.ok and self.failed != 0:
            raise ValueError("ok report cannot have failed results")
        if self.case_count != self.stable_cases + self.unstable_cases:
            raise ValueError("case_count must equal stable_cases + unstable_cases")
        return self

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"report_hash", "created_at"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "GoldenTraceReplayReport":
        return self.model_copy(update={"report_hash": self.compute_hash()})

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")