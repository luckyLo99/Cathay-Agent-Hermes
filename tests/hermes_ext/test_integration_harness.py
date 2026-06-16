from __future__ import annotations

from pathlib import Path

from hermes_ext.harness.contracts import (
    ExtensionFlagName,
    ExtensionHarnessMode,
    FeatureFlagSet,
    FeatureFlagSource,
    HarnessRunRequest,
)
from hermes_ext.harness.integration_harness import IntegrationHarness


def enabled_flags(*names: ExtensionFlagName) -> FeatureFlagSet:
    flags = FeatureFlagSet.default()
    flags = flags.with_value(ExtensionFlagName.ENABLED, True, source=FeatureFlagSource.EXPLICIT, reason="test")
    for name in names:
        flags = flags.with_value(name, True, source=FeatureFlagSource.EXPLICIT, reason="test")
    return flags


def test_harness_diagnostic_mode(tmp_path: Path) -> None:
    result = IntegrationHarness(project_root=Path.cwd()).run(
        HarnessRunRequest(
            mode=ExtensionHarnessMode.DIAGNOSTIC,
            state_dir=tmp_path,
            flags=FeatureFlagSet.default(),
        )
    )

    assert result.ok
    assert result.shadow_result is None


def test_harness_shadow_mode_requires_flag(tmp_path: Path) -> None:
    result = IntegrationHarness(project_root=Path.cwd()).run(
        HarnessRunRequest(
            mode=ExtensionHarnessMode.SHADOW,
            text="hello",
            state_dir=tmp_path,
            flags=FeatureFlagSet.default(),
        )
    )

    assert not result.ok
    assert result.error == "shadow_runner flag is not effectively enabled"


def test_harness_shadow_run_enabled_without_memory(tmp_path: Path) -> None:
    flags = enabled_flags(ExtensionFlagName.SHADOW_RUNNER)

    result = IntegrationHarness(project_root=Path.cwd()).run(
        HarnessRunRequest(
            mode=ExtensionHarnessMode.SHADOW,
            text="Phase 6 harness shadow run",
            state_dir=tmp_path,
            flags=flags,
        )
    )

    assert result.ok
    assert result.shadow_result is not None
    assert result.shadow_result["status"] == "completed"
    assert "memoryx shadow memory disabled" in " ".join(result.warnings)


def test_harness_shadow_run_with_all_shadow_features(tmp_path: Path) -> None:
    flags = enabled_flags(
        ExtensionFlagName.SHADOW_RUNNER,
        ExtensionFlagName.PRETOOL_GUARD,
        ExtensionFlagName.CATHAY,
        ExtensionFlagName.MEMORYX,
        ExtensionFlagName.CHECKPOINT_REPLAY,
    )

    result = IntegrationHarness(project_root=Path.cwd()).run(
        HarnessRunRequest(
            mode=ExtensionHarnessMode.SHADOW,
            text="Phase 6 Hermes harness with Trae DeepSeek pytest stability",
            state_dir=tmp_path,
            flags=flags,
        )
    )

    assert result.ok
    assert result.shadow_result is not None
    assert result.shadow_result["checkpoint_count"] > 0
    assert result.replay_result is not None
    assert result.replay_result["ok"] is True


def test_harness_pretool_guard_blocks_dangerous_tool(tmp_path: Path) -> None:
    flags = enabled_flags(
        ExtensionFlagName.SHADOW_RUNNER,
        ExtensionFlagName.PRETOOL_GUARD,
    )

    result = IntegrationHarness(project_root=Path.cwd()).run(
        HarnessRunRequest(
            mode=ExtensionHarnessMode.SHADOW,
            text="danger test",
            state_dir=tmp_path,
            flags=flags,
            tool_payload={"tool_name": "bash", "argv": ["rm", "-rf", "/"]},
        )
    )

    assert result.ok
    assert result.shadow_result is not None
    assert result.shadow_result["metadata"]["blocked"] is True