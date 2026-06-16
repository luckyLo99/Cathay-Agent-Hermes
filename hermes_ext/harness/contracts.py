from __future__ import annotations

import json
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ExtensionFlagName(str, Enum):
    ENABLED = "enabled"
    SHADOW_RUNNER = "shadow_runner"
    PRETOOL_GUARD = "pretool_guard"
    CATHAY = "cathay"
    MEMORYX = "memoryx"
    CHECKPOINT_REPLAY = "checkpoint_replay"
    DIAGNOSTICS = "diagnostics"
    KILL_SWITCH = "kill_switch"


class ExtensionHarnessMode(str, Enum):
    OFF = "off"
    DIAGNOSTIC = "diagnostic"
    SHADOW = "shadow"


class FeatureFlagSource(str, Enum):
    DEFAULT = "default"
    ENV = "env"
    JSON_FILE = "json_file"
    EXPLICIT = "explicit"


class FeatureFlagValue(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    name: ExtensionFlagName
    enabled: bool = False
    source: FeatureFlagSource = FeatureFlagSource.DEFAULT
    reason: str = "default false"

    @field_validator("reason")
    @classmethod
    def reason_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("reason must not be empty")
        if "\x00" in value:
            raise ValueError("reason must not contain null bytes")
        return value


class FeatureFlagSet(BaseModel):
    """
    Complete flag set.

    All flags default OFF. Kill switch wins over every feature flag.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    values: dict[ExtensionFlagName, FeatureFlagValue] = Field(default_factory=dict)

    @classmethod
    def default(cls) -> "FeatureFlagSet":
        values = {
            name: FeatureFlagValue(
                name=name,
                enabled=False,
                source=FeatureFlagSource.DEFAULT,
                reason="default false",
            )
            for name in ExtensionFlagName
        }
        return cls(values=values)

    def is_enabled(self, name: ExtensionFlagName) -> bool:
        if self.values.get(ExtensionFlagName.KILL_SWITCH, FeatureFlagValue(name=ExtensionFlagName.KILL_SWITCH)).enabled:
            if name != ExtensionFlagName.DIAGNOSTICS:
                return False

        value = self.values.get(name)
        if value is None:
            return False

        if name != ExtensionFlagName.DIAGNOSTICS:
            if not self.values.get(
                ExtensionFlagName.ENABLED,
                FeatureFlagValue(name=ExtensionFlagName.ENABLED),
            ).enabled:
                return False

        return value.enabled

    def with_value(
        self,
        name: ExtensionFlagName,
        enabled: bool,
        *,
        source: FeatureFlagSource,
        reason: str,
    ) -> "FeatureFlagSet":
        values = dict(self.values)
        values[name] = FeatureFlagValue(
            name=name,
            enabled=enabled,
            source=source,
            reason=reason,
        )
        return self.model_copy(update={"values": values})

    def to_audit_dict(self) -> dict[str, Any]:
        return {
            name.value: {
                "enabled": value.enabled,
                "effective_enabled": self.is_enabled(name),
                "source": value.source.value,
                "reason": value.reason,
            }
            for name, value in sorted(self.values.items(), key=lambda item: item[0].value)
        }


class HarnessRunRequest(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    request_id: str = Field(default_factory=lambda: str(uuid4()))
    mode: ExtensionHarnessMode = ExtensionHarnessMode.DIAGNOSTIC
    text: str = ""
    state_dir: Path
    flags: FeatureFlagSet = Field(default_factory=FeatureFlagSet.default)
    tool_payload: dict[str, Any] | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("request_id")
    @classmethod
    def request_id_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("request_id must not be empty")
        if "\x00" in value:
            raise ValueError("request_id must not contain null bytes")
        return value

    @field_validator("text")
    @classmethod
    def text_must_be_clean(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("text must not contain null bytes")
        return value

    @field_validator("state_dir")
    @classmethod
    def state_dir_must_be_path(cls, value: Path) -> Path:
        return value

    @model_validator(mode="after")
    def validate_shadow_mode_requires_text(self) -> "HarnessRunRequest":
        if self.mode == ExtensionHarnessMode.SHADOW and not self.text.strip():
            raise ValueError("shadow mode requires non-empty text")
        return self


class HarnessRunResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    request_id: str
    ok: bool
    mode: ExtensionHarnessMode
    flags: dict[str, Any]
    diagnostics: dict[str, Any] = Field(default_factory=dict)
    shadow_result: dict[str, Any] | None = None
    replay_result: dict[str, Any] | None = None
    error: str | None = None
    warnings: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)

    def to_json(self) -> str:
        return json.dumps(self.model_dump(mode="json"), ensure_ascii=False, indent=2, sort_keys=True)