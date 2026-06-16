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


class AdapterSurfaceKind(str, Enum):
    CLI = "cli"
    RUNTIME_LOOP = "runtime_loop"
    PROVIDER = "provider"
    TOOL_REGISTRY = "tool_registry"
    TOOL_ORCHESTRATION = "tool_orchestration"
    MEMORY = "memory"
    PROMPT = "prompt"
    CONTEXT = "context"
    STATE_DB = "state_db"
    SECURITY = "security"
    GATEWAY = "gateway"
    CRON = "cron"
    TEST = "test"
    EXTENSION = "extension"
    UNKNOWN = "unknown"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AdapterIntegrationPosture(str, Enum):
    FORBIDDEN = "forbidden"
    READ_ONLY = "read_only"
    WRAPPER_ONLY = "wrapper_only"
    FEATURE_FLAG_REQUIRED = "feature_flag_required"
    ADAPTER_CANDIDATE = "adapter_candidate"


class PythonImportRecord(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    module: str
    name: str | None = None
    alias: str | None = None
    line: int = Field(ge=0)

    @field_validator("module")
    @classmethod
    def module_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("module must not be empty")
        if "\x00" in value:
            raise ValueError("module must not contain null bytes")
        return value


class PythonSymbolRecord(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    kind: str
    name: str
    qualname: str
    line: int = Field(ge=0)

    @field_validator("kind", "name", "qualname")
    @classmethod
    def fields_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("symbol fields must not be empty")
        if "\x00" in value:
            raise ValueError("symbol fields must not contain null bytes")
        return value


class PythonCallRecord(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    name: str
    line: int = Field(ge=0)

    @field_validator("name")
    @classmethod
    def name_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("call name must not be empty")
        if "\x00" in value:
            raise ValueError("call name must not contain null bytes")
        return value


class SourceFileRecord(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    relative_path: str
    size_bytes: int = Field(ge=0)
    line_count: int = Field(ge=0)
    sha256: str
    is_lifeline: bool = False
    surface_guess: AdapterSurfaceKind = AdapterSurfaceKind.UNKNOWN
    imports: list[PythonImportRecord] = Field(default_factory=list)
    symbols: list[PythonSymbolRecord] = Field(default_factory=list)
    calls: list[PythonCallRecord] = Field(default_factory=list)
    parse_error: str | None = None

    @field_validator("relative_path", "sha256")
    @classmethod
    def fields_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("file fields must not be empty")
        if "\x00" in value:
            raise ValueError("file fields must not contain null bytes")
        return value


class ExtensionPointCandidate(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    candidate_id: str = Field(default_factory=lambda: str(uuid4()))
    relative_path: str
    surface: AdapterSurfaceKind
    posture: AdapterIntegrationPosture
    risk: RiskLevel
    symbol: str | None = None
    line: int = Field(default=0, ge=0)
    reason: str
    future_adapter_hint: str
    allowed_next_phase: str = "phase8_mapping_only"
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("relative_path", "reason", "future_adapter_hint", "allowed_next_phase")
    @classmethod
    def text_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("candidate text fields must not be empty")
        if "\x00" in value:
            raise ValueError("candidate text fields must not contain null bytes")
        return value

    def stable_id(self) -> "ExtensionPointCandidate":
        payload = {
            "relative_path": self.relative_path,
            "surface": self.surface.value,
            "posture": self.posture.value,
            "symbol": self.symbol,
            "line": self.line,
            "reason": self.reason,
        }
        return self.model_copy(update={"candidate_id": sha256_text(stable_json_dumps(payload))[:16]})


class AdapterScanConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    project_root: Path
    max_file_bytes: int = Field(default=2_000_000, ge=1)
    include_suffixes: tuple[str, ...] = (".py",)
    exclude_dirs: tuple[str, ...] = (
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "node_modules",
        "reports",
        "tests",
        "hermes_ext",
    )
    lifeline_files: tuple[str, ...] = (
        "hermes_bootstrap.py",
        "hermes_constants.py",
        "cli.py",
        "run_agent.py",
        "hermes_cli/main.py",
        "gateway/run.py",
        "tools/registry.py",
        "model_tools.py",
        "toolsets.py",
        "agent/memory_provider.py",
        "agent/memory_manager.py",
        "tools/memory_tool.py",
        "agent/system_prompt.py",
        "agent/prompt_builder.py",
        "agent/context_compressor.py",
        "hermes_state.py",
        "providers/__init__.py",
        "providers/base.py",
        "tools/threat_patterns.py",
        "agent/redact.py",
        "cron/jobs.py",
        "cron/scheduler.py",
        "gateway/platforms/base.py",
        "gateway/session.py",
    )

    @field_validator("project_root")
    @classmethod
    def normalize_root(cls, value: Path) -> Path:
        return value.resolve()


class AdapterScanSummary(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    files_scanned: int = 0
    lifeline_files_found: int = 0
    candidates_found: int = 0
    forbidden_candidates: int = 0
    wrapper_only_candidates: int = 0
    feature_flag_candidates: int = 0
    parse_errors: int = 0


class AdapterScanReport(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    report_id: str = Field(default_factory=lambda: str(uuid4()))
    project_root: str
    created_at: datetime = Field(default_factory=utc_now)
    summary: AdapterScanSummary
    files: list[SourceFileRecord] = Field(default_factory=list)
    candidates: list[ExtensionPointCandidate] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

    def to_audit_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")

    @model_validator(mode="after")
    def candidate_count_matches_summary(self) -> "AdapterScanReport":
        if self.summary.candidates_found != len(self.candidates):
            raise ValueError("summary.candidates_found must match candidates length")
        return self