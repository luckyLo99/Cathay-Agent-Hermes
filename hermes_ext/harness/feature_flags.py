from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from hermes_ext.harness.contracts import (
    ExtensionFlagName,
    FeatureFlagSet,
    FeatureFlagSource,
)


class FeatureFlagResolver:
    """
    Local feature flag resolver.

    It intentionally does not import OpenFeature.
    It borrows the provider/evaluation-context idea while remaining dependency-free.
    """

    ENV_PREFIX = "HERMES_EXT_"

    ENV_MAP: dict[ExtensionFlagName, str] = {
        ExtensionFlagName.ENABLED: "HERMES_EXT_ENABLED",
        ExtensionFlagName.SHADOW_RUNNER: "HERMES_EXT_SHADOW_RUNNER",
        ExtensionFlagName.PRETOOL_GUARD: "HERMES_EXT_PRETOOL_GUARD",
        ExtensionFlagName.CATHAY: "HERMES_EXT_CATHAY",
        ExtensionFlagName.MEMORYX: "HERMES_EXT_MEMORYX",
        ExtensionFlagName.CHECKPOINT_REPLAY: "HERMES_EXT_CHECKPOINT_REPLAY",
        ExtensionFlagName.DIAGNOSTICS: "HERMES_EXT_DIAGNOSTICS",
        ExtensionFlagName.KILL_SWITCH: "HERMES_EXT_KILL_SWITCH",
    }

    TRUE_VALUES = {"1", "true", "yes", "on", "enabled"}
    FALSE_VALUES = {"0", "false", "no", "off", "disabled"}

    def __init__(
        self,
        *,
        env: dict[str, str] | None = None,
        json_path: Path | None = None,
        explicit: dict[str, bool] | None = None,
    ) -> None:
        self.env = env if env is not None else dict(os.environ)
        self.json_path = json_path
        self.explicit = explicit or {}

    def resolve(self) -> FeatureFlagSet:
        flags = FeatureFlagSet.default()

        if self.json_path is not None:
            flags = self._apply_json_file(flags, self.json_path)

        flags = self._apply_env(flags)

        if self.explicit:
            flags = self._apply_explicit(flags, self.explicit)

        return flags

    def _apply_json_file(self, flags: FeatureFlagSet, path: Path) -> FeatureFlagSet:
        if not path.exists():
            return flags

        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("feature flag json must be an object")

        for raw_key, raw_value in data.items():
            name = self._coerce_name(raw_key)
            if name is None:
                continue
            enabled = self._coerce_bool(raw_value)
            flags = flags.with_value(
                name,
                enabled,
                source=FeatureFlagSource.JSON_FILE,
                reason=f"json file {path.name}",
            )

        return flags

    def _apply_env(self, flags: FeatureFlagSet) -> FeatureFlagSet:
        for name, env_name in self.ENV_MAP.items():
            if env_name not in self.env:
                continue
            enabled = self._coerce_bool(self.env[env_name])
            flags = flags.with_value(
                name,
                enabled,
                source=FeatureFlagSource.ENV,
                reason=f"env {env_name}",
            )

        return flags

    def _apply_explicit(self, flags: FeatureFlagSet, explicit: dict[str, bool]) -> FeatureFlagSet:
        for raw_key, raw_value in explicit.items():
            name = self._coerce_name(raw_key)
            if name is None:
                continue
            flags = flags.with_value(
                name,
                bool(raw_value),
                source=FeatureFlagSource.EXPLICIT,
                reason="explicit argument",
            )

        return flags

    def _coerce_name(self, raw_key: str) -> ExtensionFlagName | None:
        normalized = raw_key.strip().lower()
        normalized = normalized.removeprefix("hermes_ext_")
        try:
            return ExtensionFlagName(normalized)
        except ValueError:
            return None

    def _coerce_bool(self, value: Any) -> bool:
        if isinstance(value, bool):
            return value

        if isinstance(value, int):
            return value != 0

        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in self.TRUE_VALUES:
                return True
            if normalized in self.FALSE_VALUES:
                return False

        raise ValueError(f"cannot coerce feature flag value to bool: {value!r}")