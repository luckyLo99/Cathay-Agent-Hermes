from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from hermes_ext.harness.contracts import (
    ExtensionFlagName,
    ExtensionHarnessMode,
    FeatureFlagSet,
    FeatureFlagSource,
    HarnessRunRequest,
)


def test_feature_flags_default_off() -> None:
    flags = FeatureFlagSet.default()

    assert not flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)
    assert not flags.is_enabled(ExtensionFlagName.CATHAY)
    assert not flags.is_enabled(ExtensionFlagName.MEMORYX)


def test_feature_flags_require_global_enabled() -> None:
    flags = FeatureFlagSet.default().with_value(
        ExtensionFlagName.SHADOW_RUNNER,
        True,
        source=FeatureFlagSource.EXPLICIT,
        reason="test",
    )

    assert not flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)

    flags = flags.with_value(
        ExtensionFlagName.ENABLED,
        True,
        source=FeatureFlagSource.EXPLICIT,
        reason="test",
    )

    assert flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)


def test_kill_switch_disables_features() -> None:
    flags = FeatureFlagSet.default()
    flags = flags.with_value(ExtensionFlagName.ENABLED, True, source=FeatureFlagSource.EXPLICIT, reason="test")
    flags = flags.with_value(ExtensionFlagName.SHADOW_RUNNER, True, source=FeatureFlagSource.EXPLICIT, reason="test")
    flags = flags.with_value(ExtensionFlagName.KILL_SWITCH, True, source=FeatureFlagSource.EXPLICIT, reason="test")

    assert not flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER)


def test_shadow_request_requires_text(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        HarnessRunRequest(
            mode=ExtensionHarnessMode.SHADOW,
            text="",
            state_dir=tmp_path,
        )


def test_contracts_reject_extra_fields(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        HarnessRunRequest(
            mode=ExtensionHarnessMode.DIAGNOSTIC,
            state_dir=tmp_path,
            unexpected=True,  # type: ignore[call-arg]
        )