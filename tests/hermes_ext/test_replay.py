from __future__ import annotations

from pathlib import Path

from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.contracts import ReplayMode, ShadowRunConfig
from hermes_ext.orchestration.replay import ReplayService
from hermes_ext.orchestration.shadow_runner import ShadowRunner


def test_replay_run_reads_existing_checkpoints(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.db")
    runner = ShadowRunner(
        checkpoint_store=store,
        shadow_memory_provider=ShadowMemoryProvider(tmp_path / "shadow.db"),
    )
    result = runner.run_text(
        "Replay checkpoint test",
        config=ShadowRunConfig(run_id="run-replay", session_id="session"),
    )

    replay = ReplayService(store).replay_run(result.run_id)

    assert replay.ok
    assert replay.mode == ReplayMode.DRY_RUN
    assert replay.checkpoint_count == result.checkpoint_count
    assert replay.checkpoints[0].sequence == 0


def test_replay_from_checkpoint_returns_tail(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.db")
    runner = ShadowRunner(
        checkpoint_store=store,
        shadow_memory_provider=ShadowMemoryProvider(tmp_path / "shadow.db"),
    )
    result = runner.run_text(
        "Replay from checkpoint test",
        config=ShadowRunConfig(run_id="run-tail", session_id="session"),
    )
    checkpoints = store.list_run(result.run_id)
    middle = checkpoints[len(checkpoints) // 2]

    replay = ReplayService(store).replay_from_checkpoint(middle.checkpoint_id)

    assert replay.ok
    assert replay.mode == ReplayMode.FROM_CHECKPOINT
    assert replay.checkpoints[0].sequence == middle.sequence