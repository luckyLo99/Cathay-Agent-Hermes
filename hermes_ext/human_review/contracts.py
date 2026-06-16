"""Strict contracts for Phase 13 human review.

The models here are intentionally pure data contracts. They must not import
Hermes runtime, CLI, gateway, providers, tools, memory, state, or model SDK code.
"""

from __future__ import annotations

from enum import Enum
import hashlib
import json
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator


PASS = "pass"
FAIL = "fail"
WARN = "warn"

SEVERITY_INFO = "info"
SEVERITY_WARNING = "warning"
SEVERITY_ERROR = "error"
SEVERITY_CRITICAL = "critical"

DOCUMENT_ONLY_NOT_APPROVED = "document_only_not_approved"


def stable_json_dumps(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_assignment=True)


class HumanReviewDecision(str, Enum):
    PENDING = "pending_human_review"
    APPROVE_SHADOW_MERGE = "approve_shadow_merge"
    REQUEST_CHANGES = "request_changes"
    REJECT_SHADOW_MERGE = "reject_shadow_merge"


class EvidenceFile(StrictModel):
    name: str
    relative_path: str
    exists: bool
    sha256: str = ""
    size_bytes: int = 0
    json_data: dict[str, Any] | None = None
    text_excerpt: str = ""
    errors: tuple[str, ...] = Field(default_factory=tuple)

    @field_validator("name", "relative_path")
    @classmethod
    def non_empty_string(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("value must not be empty")
        return value

    @field_validator("relative_path")
    @classmethod
    def reject_absolute_or_escape_path(cls, value: str) -> str:
        normalized = value.replace("\\", "/")
        if normalized.startswith("/") or ":" in normalized:
            raise ValueError("relative_path must be project-relative")
        parts = [part for part in normalized.split("/") if part]
        if ".." in parts:
            raise ValueError("relative_path must not escape project root")
        return normalized

    @property
    def usable(self) -> bool:
        return self.exists and not self.errors

    @property
    def usable_json(self) -> bool:
        return self.usable and self.json_data is not None


class HumanReviewEvidence(StrictModel):
    project_root: str
    required: dict[str, EvidenceFile]

    @field_validator("required")
    @classmethod
    def required_must_not_be_empty(
        cls,
        value: dict[str, EvidenceFile],
    ) -> dict[str, EvidenceFile]:
        if not value:
            raise ValueError("required evidence must not be empty")
        return value

    @property
    def documents(self) -> tuple[EvidenceFile, ...]:
        return tuple(self.required.values())

    @property
    def missing_required_names(self) -> tuple[str, ...]:
        return tuple(doc.name for doc in self.documents if not doc.exists)

    @property
    def invalid_required_names(self) -> tuple[str, ...]:
        return tuple(doc.name for doc in self.documents if doc.errors)

    def document(self, name: str) -> EvidenceFile:
        return self.required[name]


class DecisionFinding(StrictModel):
    id: str
    status: str
    severity: str
    message: str
    evidence_refs: tuple[str, ...] = Field(default_factory=tuple)

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        if value not in {PASS, FAIL, WARN}:
            raise ValueError(f"invalid status: {value}")
        return value

    @field_validator("severity")
    @classmethod
    def validate_severity(cls, value: str) -> str:
        if value not in {
            SEVERITY_INFO,
            SEVERITY_WARNING,
            SEVERITY_ERROR,
            SEVERITY_CRITICAL,
        }:
            raise ValueError(f"invalid severity: {value}")
        return value

    @property
    def is_blocking(self) -> bool:
        return self.status == FAIL and self.severity in {
            SEVERITY_ERROR,
            SEVERITY_CRITICAL,
        }


class HumanReviewDossier(StrictModel):
    dossier_id: str
    phase: int = 13
    title: str
    sections: dict[str, str]
    source_evidence: tuple[str, ...]
    dossier_hash: str = ""

    @field_validator("sections")
    @classmethod
    def sections_required(cls, value: dict[str, str]) -> dict[str, str]:
        required = {
            "executive_summary",
            "scope",
            "architecture_review",
            "risk_register",
            "acceptance_criteria",
            "review_questions",
            "next_phase_policy",
        }
        missing = required - set(value)
        if missing:
            raise ValueError(f"missing dossier sections: {sorted(missing)}")
        for key, text in value.items():
            if not key.strip() or not text.strip():
                raise ValueError("section key and value must be non-empty")
        return value

    def model_post_init(self, __context: Any) -> None:
        if not self.dossier_hash:
            payload = self.model_dump(mode="json", exclude={"dossier_hash"})
            digest = sha256_text(stable_json_dumps(payload))
            object.__setattr__(self, "dossier_hash", digest)


class ColdStartValidationPlan(StrictModel):
    plan_id: str
    phase: int = 13
    title: str
    objective: str
    steps: tuple[str, ...]
    pass_criteria: tuple[str, ...]
    forbidden_actions: tuple[str, ...]
    plan_hash: str = ""

    @field_validator("steps", "pass_criteria", "forbidden_actions")
    @classmethod
    def tuple_must_not_be_empty(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        if not value:
            raise ValueError("tuple must not be empty")
        return value

    def model_post_init(self, __context: Any) -> None:
        if not self.plan_hash:
            payload = self.model_dump(mode="json", exclude={"plan_hash"})
            object.__setattr__(self, "plan_hash", sha256_text(stable_json_dumps(payload)))


class NativeExperimentProposal(StrictModel):
    proposal_id: str
    phase: int = 13
    candidate_next_phase: str
    status: str
    objective: str
    allowed_work: tuple[str, ...]
    forbidden_work: tuple[str, ...]
    required_preconditions: tuple[str, ...]
    rollback_requirements: tuple[str, ...]
    proposal_hash: str = ""

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        if value != DOCUMENT_ONLY_NOT_APPROVED:
            raise ValueError("native experiment proposal must remain document_only_not_approved")
        return value

    @field_validator(
        "allowed_work",
        "forbidden_work",
        "required_preconditions",
        "rollback_requirements",
    )
    @classmethod
    def tuples_required(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        if not value:
            raise ValueError("tuple must not be empty")
        return value

    def model_post_init(self, __context: Any) -> None:
        if not self.proposal_hash:
            payload = self.model_dump(mode="json", exclude={"proposal_hash"})
            object.__setattr__(
                self, "proposal_hash", sha256_text(stable_json_dumps(payload))
            )


class MergeDecisionReport(StrictModel):
    report_id: str
    phase: int = 13
    decision: HumanReviewDecision
    reviewer: str = ""
    ok: bool
    review_ready: bool
    decision_allowed: bool
    required_acknowledgements: tuple[str, ...]
    provided_acknowledgements: tuple[str, ...]
    missing_acknowledgements: tuple[str, ...]
    findings: tuple[DecisionFinding, ...]
    blocking_failures: tuple[str, ...]
    warnings: tuple[str, ...]
    recommendations: tuple[str, ...]
    report_hash: str = ""

    @field_validator("findings")
    @classmethod
    def findings_required(cls, value: tuple[DecisionFinding, ...]) -> tuple[DecisionFinding, ...]:
        if not value:
            raise ValueError("findings must not be empty")
        return value

    def model_post_init(self, __context: Any) -> None:
        expected_blocking = tuple(f.id for f in self.findings if f.is_blocking)
        if self.blocking_failures != expected_blocking:
            raise ValueError("blocking_failures does not match findings")

        expected_warnings = tuple(f.message for f in self.findings if f.status == WARN)
        if self.warnings != expected_warnings:
            raise ValueError("warnings does not match findings")

        if self.ok != (self.review_ready and self.decision_allowed):
            raise ValueError("ok must equal review_ready and decision_allowed")

        if not self.report_hash:
            payload = self.model_dump(mode="json", exclude={"report_hash"})
            object.__setattr__(self, "report_hash", sha256_text(stable_json_dumps(payload)))


class HumanReviewBundle(StrictModel):
    bundle_id: str
    phase: int = 13
    dossier: dict[str, Any]
    cold_start_validation_plan: dict[str, Any]
    native_experiment_proposal: dict[str, Any]
    merge_decision_report: dict[str, Any]
    output_artifacts: tuple[str, ...]
    bundle_hash: str = ""

    def model_post_init(self, __context: Any) -> None:
        if not self.bundle_hash:
            payload = self.model_dump(mode="json", exclude={"bundle_hash"})
            object.__setattr__(self, "bundle_hash", sha256_text(stable_json_dumps(payload)))