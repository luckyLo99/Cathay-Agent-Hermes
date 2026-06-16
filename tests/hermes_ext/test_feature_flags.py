from __future__ import annotations

import json
from pathlib import Path

import pytest

from hermes_ext.harness.contracts import ExtensionFlagName
from hermes_ext.harness.feature_flags import FeatureFlagResolver


def test_env_flags_are_resolved() -> None:
    flags = FeatureFlagResolver(
        env={
            "HERMES_EXT_ENABLED": "true",
            "HERMES_EXT_SHADOW_RUNNER": "1",
            "HERMES_EXT_CATHAY": "yes",
        }
    ).resolve()

    assert flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)
    assert flags.is_enabled(ExtensionFlagName.CATHAY)
    assert not flags.is_enabled(ExtensionFlagName.MEMORYX)


def test_json_flags_are_resolved(tmp_path: Path) -> None:
    path = tmp_path / "flags.json"
    path.write_text(
        json.dumps(
            {
                "enabled": True,
                "shadow_runner": True,
                "memoryx": True,
            }
        ),
        encoding="utf-8",
    )

    flags = FeatureFlagResolver(env={}, json_path=path).resolve()

    assert flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)
    assert flags.is_enabled(ExtensionFlagName.MEMORYX)


def test_explicit_flags_override_json_and_env(tmp_path: Path) -> None:
    path = tmp_path / "flags.json"
    path.write_text(json.dumps({"enabled": True, "shadow_runner": False}), encoding="utf-8")

    flags = FeatureFlagResolver(
        env={"HERMES_EXT_SHADOW_RUNNER": "false"},
        json_path=path,
        explicit={"shadow_runner": True},
    ).resolve()

    assert flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)


def test_kill_switch_from_env_wins() -> None:
    flags = FeatureFlagResolver(
        env={
            "HERMES_EXT_ENABLED": "true",
            "HERMES_EXT_SHADOW_RUNNER": "true",
            "HERMES_EXT_KILL_SWITCH": "true",
        }
    ).resolve()

    assert not flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)


def test_invalid_bool_raises() -> None:
    with pytest.raises(ValueError):
        FeatureFlagResolver(env={"HERMES_EXT_ENABLED": "maybe"}).resolve()