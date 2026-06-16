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


class AssemblyArtifactKind(str, Enum):
    SOURCE = "source"
    TEST = "test"
    REPORT = "report"
    GENERATED_MANIFEST = "generated_manifest"
    UNKNOWN = "unknown"


class AssemblyInvariantStatus(str, Enum):
    PASS = "pass"
    WARN = "warn"
    FAIL = "fail"


class AssemblyInvariantSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class AssemblyArtifact(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    relative_path: str = Field(min_length=1)
    kind: AssemblyArtifactKind
    exists: bool
    size_bytes: int = Field(default=0, ge=0)
    sha256: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("relative_path")
    @classmethod
    def clean_path(cls, value: str) -> str:
        value = value.strip().replace("\\", "/")
        if not value:
            raise ValueError("relative_path must not be empty")
        if "\x00" in value:
            raise ValueError("relative_path must not contain null bytes")
        if value.startswith("../") or value == "..":
            raise ValueError("relative_path must not escape project root")
        return value

    @field_validator("sha256")
    @classmethod
    def clean_sha(cls, value: str | None) -> str | None:
        if value is None:
            return None
        value = value.strip()
        if len(value) != 64:
            raise ValueError("sha256 must be 64 hex characters")
        int(value, 16)
        return value


class AssemblyInvariant(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    invariant_id: str = Field(min_length=1)
    status: AssemblyInvariantStatus
    severity: AssemblyInvariantSeverity
    message: str = Field(min_length=1)
    evidence: dict[str, Any] = Field(default_factory=dict)

    @field_validator("invariant_id", "message")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("invariant fields must not be empty")
        if "\x00" in value:
            raise ValueError("invariant fields must not contain null bytes")
        return value


class AssemblyManifestConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    project_root: Path
    include_reports: bool = True
    include_tests: bool = True
    require_phase10_golden_trace: bool = True
    require_phase9_native_boundary: bool = True
    max_artifacts: int = Field(default=50_000, ge=1)

    @field_validator("project_root")
    @classmethod
    def normalize_project_root(cls, value: Path) -> Path:
        return value.resolve()


class AssemblySummary(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    source_artifacts: int = Field(default=0, ge=0)
    test_artifacts: int = Field(default=0, ge=0)
    report_artifacts: int = Field(default=0, ge=0)
    total_artifacts: int = Field(default=0, ge=0)
    invariants_passed: int = Field(default=0, ge=0)
    invariants_warned: int = Field(default=0, ge=0)
    invariants_failed: int = Field(default=0, ge=0)


class AssemblyManifest(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    manifest_id: str = Field(default_factory=lambda: str(uuid4()))
    phase: int = 11
    project_root: str
    created_at: datetime = Field(default_factory=utc_now)
    artifacts: list[AssemblyArtifact] = Field(default_factory=list)
    invariants: list[AssemblyInvariant] = Field(default_factory=list)
    summary: AssemblySummary
    manifest_hash: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"manifest_hash", "created_at"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "AssemblyManifest":
        return self.model_copy(update={"manifest_hash": self.compute_hash()})

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")

    @model_validator(mode="after")
    def summary_must_match(self) -> "AssemblyManifest":
        if self.summary.total_artifacts != len(self.artifacts):
            raise ValueError("summary.total_artifacts must match artifacts length")
        if self.summary.invariants_passed + self.summary.invariants_warned + self.summary.invariants_failed != len(self.invariants):
            raise ValueError("invariant summary must match invariants length")
        return self


class AssemblyGateResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    gate_id: str = Field(default_factory=lambda: str(uuid4()))
    ok: bool
    manifest_hash: str
    blocking_failures: list[AssemblyInvariant] = Field(default_factory=list)
    warnings: list[AssemblyInvariant] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")
