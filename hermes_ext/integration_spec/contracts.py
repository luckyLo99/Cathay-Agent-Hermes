from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stable_json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class IntegrationMode(str, Enum):
    FORBIDDEN = "forbidden"
    NO_TOUCH = "no_touch"
    EXTERNAL_WRAPPER = "external_wrapper"
    FEATURE_FLAG_SHADOW = "feature_flag_shadow"
    SIDE_CAR_OBSERVER = "sidecar_observer"
    EXTERNAL_HARNESS = "external_harness"


class IntegrationSpecStatus(str, Enum):
    DESIGN_ONLY = "design_only"
    BLOCKED = "blocked"
    READY_FOR_SHADOW_HARNESS = "ready_for_shadow_harness"


class IntegrationAdapterLayer(str, Enum):
    CLI_BOUNDARY = "cli_boundary"
    RUNTIME_LOOP_BOUNDARY = "runtime_loop_boundary"
    PROVIDER_BOUNDARY = "provider_boundary"
    TOOL_SAFETY_BOUNDARY = "tool_safety_boundary"
    MEMORY_SHADOW_BOUNDARY = "memory_shadow_boundary"
    PROMPT_CONTEXT_BOUNDARY = "prompt_context_boundary"
    STATE_DB_BOUNDARY = "state_db_boundary"
    GATEWAY_SIDECAR_BOUNDARY = "gateway_sidecar_boundary"
    CRON_OBSERVER_BOUNDARY = "cron_observer_boundary"
    SECURITY_POLICY_BOUNDARY = "security_policy_boundary"
    UNKNOWN_BOUNDARY = "unknown_boundary"


class RequiredFeatureFlag(str, Enum):
    HERMES_EXT_ENABLED = "HERMES_EXT_ENABLED"
    HERMES_EXT_SHADOW_RUNNER = "HERMES_EXT_SHADOW_RUNNER"
    HERMES_EXT_PRETOOL_GUARD = "HERMES_EXT_PRETOOL_GUARD"
    HERMES_EXT_CATHAY = "HERMES_EXT_CATHAY"
    HERMES_EXT_MEMORYX = "HERMES_EXT_MEMORYX"
    HERMES_EXT_CHECKPOINT_REPLAY = "HERMES_EXT_CHECKPOINT_REPLAY"
    HERMES_EXT_DIAGNOSTICS = "HERMES_EXT_DIAGNOSTICS"
    HERMES_EXT_KILL_SWITCH = "HERMES_EXT_KILL_SWITCH"


class IntegrationSpecConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    project_root: Path
    phase7_scan_json: Path
    phase: int = Field(default=8, ge=8)
    max_entries: int = Field(default=10_000, ge=1)
    allow_forbidden_entries: bool = True

    @field_validator("project_root", "phase7_scan_json")
    @classmethod
    def normalize_path(cls, value: Path) -> Path:
        return value.resolve()


class IntegrationConstraint(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    rule_id: str = Field(min_length=1)
    description: str = Field(min_length=1)
    severity: RiskLevel = RiskLevel.HIGH

    @field_validator("rule_id", "description")
    @classmethod
    def text_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("constraint fields must not be empty")
        if "\x00" in value:
            raise ValueError("constraint fields must not contain null bytes")
        return value


class DesignMatrixEntry(BaseModel):
    """
    One zero-touch design decision for one scanned candidate.

    This is not a patch plan.
    It is a guardrailed design matrix entry.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    entry_id: str = Field(default_factory=lambda: str(uuid4()))
    candidate_id: str = Field(min_length=1)
    relative_path: str = Field(min_length=1)
    symbol: str | None = None
    line: int = Field(default=0, ge=0)
    surface: AdapterSurfaceKind
    adapter_layer: IntegrationAdapterLayer
    source_posture: AdapterIntegrationPosture
    source_risk: RiskLevel
    integration_mode: IntegrationMode
    status: IntegrationSpecStatus
    rationale: str = Field(min_length=1)
    required_flags: list[RequiredFeatureFlag] = Field(default_factory=list)
    constraints: list[IntegrationConstraint] = Field(default_factory=list)
    required_tests: list[str] = Field(default_factory=list)
    rollback_strategy: str = Field(min_length=1)
    next_phase_allowed_work: str = Field(default="design_review_only", min_length=1)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("candidate_id", "relative_path", "rationale", "rollback_strategy", "next_phase_allowed_work")
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("matrix text fields must not be empty")
        if "\x00" in value:
            raise ValueError("matrix text fields must not contain null bytes")
        return value

    @model_validator(mode="after")
    def validate_forbidden_mode(self) -> "DesignMatrixEntry":
        if self.source_posture == AdapterIntegrationPosture.FORBIDDEN:
            if self.integration_mode != IntegrationMode.FORBIDDEN:
                raise ValueError("forbidden source posture must remain forbidden")
            if self.status != IntegrationSpecStatus.BLOCKED:
                raise ValueError("forbidden entries must be blocked")
        return self

    def stable_id(self) -> "DesignMatrixEntry":
        payload = {
            "candidate_id": self.candidate_id,
            "relative_path": self.relative_path,
            "symbol": self.symbol,
            "surface": self.surface.value,
            "source_posture": self.source_posture.value,
            "integration_mode": self.integration_mode.value,
        }
        return self.model_copy(update={"entry_id": sha256_text(stable_json_dumps(payload))[:16]})


class IntegrationSurfacePlan(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    surface: AdapterSurfaceKind
    total_entries: int = Field(ge=0)
    forbidden: int = Field(ge=0)
    external_wrapper: int = Field(ge=0)
    feature_flag_shadow: int = Field(ge=0)
    sidecar_observer: int = Field(ge=0)
    no_touch: int = Field(ge=0)
    highest_risk: RiskLevel = RiskLevel.LOW
    recommendation: str = Field(min_length=1)

    @field_validator("recommendation")
    @classmethod
    def recommendation_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("recommendation must not be empty")
        if "\x00" in value:
            raise ValueError("recommendation must not contain null bytes")
        return value


class IntegrationDesignMatrix(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    entries: list[DesignMatrixEntry] = Field(default_factory=list)
    surface_plans: list[IntegrationSurfacePlan] = Field(default_factory=list)

    def count_by_mode(self, mode: IntegrationMode) -> int:
        return sum(1 for entry in self.entries if entry.integration_mode == mode)

    def count_by_status(self, status: IntegrationSpecStatus) -> int:
        return sum(1 for entry in self.entries if entry.status == status)


class ZeroTouchIntegrationSpec(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    spec_id: str = Field(default_factory=lambda: str(uuid4()))
    phase: int = 8
    project_root: str
    source_scan_report_id: str
    created_at: datetime = Field(default_factory=utc_now)
    matrix: IntegrationDesignMatrix
    global_constraints: list[IntegrationConstraint] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    spec_hash: str = ""

    def compute_hash(self) -> str:
        payload = self.model_dump(mode="json", exclude={"spec_hash"})
        return sha256_text(stable_json_dumps(payload))

    def with_hash(self) -> "ZeroTouchIntegrationSpec":
        return self.model_copy(update={"spec_hash": self.compute_hash()})

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")

    @model_validator(mode="after")
    def forbidden_entries_are_blocked(self) -> "ZeroTouchIntegrationSpec":
        for entry in self.matrix.entries:
            if entry.source_posture == AdapterIntegrationPosture.FORBIDDEN:
                if entry.status != IntegrationSpecStatus.BLOCKED:
                    raise ValueError("all forbidden entries must be blocked")
        return self


def candidate_from_dict(value: dict[str, Any]) -> ExtensionPointCandidate:
    return ExtensionPointCandidate.model_validate(value, strict=False)