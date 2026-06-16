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


class FinalizationEvidenceKind(str, Enum):
    PHASE_REPORT = "phase_report"
    JSON_REPORT = "json_report"
    MARKDOWN_REPORT = "markdown_report"
    CHECKLIST = "checklist"
    TEST_RESULT = "test_result"
    RELEASE_GATE = "release_gate"
    MANIFEST = "manifest"


class ReadinessInvariantStatus(str, Enum):
    PASS = "pass"
    WARN = "warn"
    FAIL = "fail"


class ReadinessInvariantSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class FinalizationConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    project_root: Path
    output_dir: Path = Path("reports/phase12")
    require_clean_phase11_gate: bool = True
    require_phase10_stability: bool = True
    require_phase9_no_side_effects: bool = True
    expected_total_tests: int = Field(default=241, ge=1)

    @field_validator("project_root", "output_dir")
    @classmethod
    def normalize_path(cls, value: Path) -> Path:
        return value.resolve()


class FinalizationEvidence(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    relative_path: str = Field(min_length=1)
    kind: FinalizationEvidenceKind
    exists: bool
    size_bytes: int = Field(default=0, ge=0)
    sha256: str | None = None
    text_excerpt: str = ""
    json_payload: dict[str, Any] | None = None

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


class DocumentationSection(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    title: str = Field(min_length=1)
    body: str = Field(min_length=1)
    priority: int = Field(default=100, ge=0)

    @field_validator("title", "body")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("documentation fields must not be empty")
        if "\x00" in value:
            raise ValueError("documentation fields must not contain null bytes")
        return value


class DocumentationPack(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    pack_id: str = Field(default_factory=lambda: str(uuid4()))
    phase: int = 12
    title: str = "Final Stabilization Documentation Pack"
    sections: list[DocumentationSection] = Field(default_factory=list)
    evidence_paths: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    pack_hash: str = ""

    @model_validator(mode="after")
    def must_have_sections(self) -> "DocumentationPack":
        if not self.sections:
            raise ValueError("documentation pack must contain sections")
        return self

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"pack_hash", "created_at"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "DocumentationPack":
        return self.model_copy(update={"pack_hash": self.compute_hash()})

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")


class ReadinessInvariant(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    invariant_id: str = Field(min_length=1)
    status: ReadinessInvariantStatus
    severity: ReadinessInvariantSeverity
    message: str = Field(min_length=1)
    evidence: dict[str, Any] = Field(default_factory=dict)

    @field_validator("invariant_id", "message")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("readiness invariant fields must not be empty")
        if "\x00" in value:
            raise ValueError("readiness invariant fields must not contain null bytes")
        return value


class MergeReadinessReport(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    report_id: str = Field(default_factory=lambda: str(uuid4()))
    phase: int = 12
    ok: bool
    invariants: list[ReadinessInvariant] = Field(default_factory=list)
    evidence_count: int = Field(ge=0)
    passed: int = Field(ge=0)
    warned: int = Field(ge=0)
    failed: int = Field(ge=0)
    created_at: datetime = Field(default_factory=utc_now)
    readiness_hash: str = ""

    @model_validator(mode="after")
    def counts_must_match(self) -> "MergeReadinessReport":
        if self.passed + self.warned + self.failed != len(self.invariants):
            raise ValueError("readiness invariant counts must match invariant length")
        if self.ok and self.failed != 0:
            raise ValueError("ok readiness report cannot contain failures")
        return self

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"readiness_hash", "created_at"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "MergeReadinessReport":
        return self.model_copy(update={"readiness_hash": self.compute_hash()})

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")


class FinalizationBundle(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    bundle_id: str = Field(default_factory=lambda: str(uuid4()))
    phase: int = 12
    documentation_pack: DocumentationPack
    readiness_report: MergeReadinessReport
    evidence: list[FinalizationEvidence] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    bundle_hash: str = ""

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"bundle_hash", "created_at"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "FinalizationBundle":
        return self.model_copy(update={"bundle_hash": self.compute_hash()})

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")