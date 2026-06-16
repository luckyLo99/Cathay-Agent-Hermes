from __future__ import annotations

from pathlib import Path

from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.contracts import (
    CheckpointKind,
    ShadowCheckpoint,
    ShadowStepName,
)


def make_checkpoint(sequence: int) -> ShadowCheckpoint:
    return ShadowCheckpoint(
        run_id="run",
        session_id="session",
        step_name=ShadowStepName.PREPARE_ENVELOPE,
        kind=CheckpointKind.AFTER_STEP,
        sequence=sequence,
        state={"sequence": sequence},
    )


def test_checkpoint_store_write_get_count(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.db")
    written = store.write(make_checkpoint(0))

    loaded = store.get(written.checkpoint_id)

    assert loaded is not None
    assert loaded.checkpoint_id == written.checkpoint_id
    assert loaded.state_hash
    assert store.count("run") == 1


def test_checkpoint_store_lists_run_in_sequence_order(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.db")
    store.write(make_checkpoint(2))
    store.write(make_checkpoint(1))
    store.write(make_checkpoint(3))

    checkpoints = store.list_run("run")

    assert [item.sequence for item in checkpoints] == [1, 2, 3]


def test_checkpoint_store_latest_for_run(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.db")
    store.write(make_checkpoint(0))
    store.write(make_checkpoint(5))

    latest = store.latest_for_run("run")

    assert latest is not None
    assert latest.sequence == 5


def test_checkpoint_store_uses_shadow_tables_only(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.db")

    assert store.assert_shadow_tables_only()