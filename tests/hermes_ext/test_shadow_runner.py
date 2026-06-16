from __future__ import annotations

from pathlib import Path

from hermes_ext.hooks.builtin_hooks import build_default_dispatcher
from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.contracts import ShadowRunConfig, ShadowRunStatus
from hermes_ext.orchestration.shadow_runner import ShadowRunner


def make_runner(tmp_path: Path) -> ShadowRunner:
    return ShadowRunner(
        checkpoint_store=CheckpointStore(tmp_path / "checkpoints.db"),
        shadow_memory_provider=ShadowMemoryProvider(tmp_path / "shadow_memory.db"),
        dispatcher=build_default_dispatcher(),
    )


def test_shadow_runner_completes_basic_text_run(tmp_path: Path) -> None:
    runner = make_runner(tmp_path)

    result = runner.run_text(
        "Phase 5 Hermes shadow orchestration with pytest stability",
        config=ShadowRunConfig(run_id="run-1", session_id="session-1"),
    )

    assert result.status == ShadowRunStatus.COMPLETED
    assert result.final_checkpoint_id
    assert result.checkpoint_count >= 6
    assert result.metadata["shadow_memory_count"] > 0


def test_shadow_runner_blocks_dangerous_tool_intent(tmp_path: Path) -> None:
    runner = make_runner(tmp_path)

    result = runner.run_text(
        "try dangerous delete",
        config=ShadowRunConfig(run_id="run-2", session_id="session-2"),
        tool_payload={"tool_name": "bash", "argv": ["rm", "-rf", "/"]},
    )

    assert result.status == ShadowRunStatus.COMPLETED
    assert result.metadata["blocked"] is True
    assert any("blocked" in warning for warning in result.warnings)


def test_shadow_runner_can_disable_cathay_and_memory(tmp_path: Path) -> None:
    runner = make_runner(tmp_path)

    result = runner.run_text(
        "minimal",
        config=ShadowRunConfig(
            run_id="run-3",
            session_id="session-3",
            enable_cathay=False,
            enable_shadow_memory=False,
        ),
    )

    assert result.status == ShadowRunStatus.COMPLETED
    assert result.metadata["shadow_memory_count"] == 0