from __future__ import annotations

from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.contracts import ReplayMode, ShadowCheckpoint
from pydantic import BaseModel, ConfigDict, Field


class ReplayResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    ok: bool
    mode: ReplayMode
    run_id: str
    checkpoint_count: int = Field(ge=0)
    checkpoints: list[ShadowCheckpoint] = Field(default_factory=list)
    error: str | None = None


class ReplayService:
    """
    Checkpoint replay service.

    Phase 5 replay reads checkpoints only.
    It does not re-execute tools, models, or Hermes core.
    """

    def __init__(self, store: CheckpointStore) -> None:
        self.store = store

    def replay_run(self, run_id: str, *, mode: ReplayMode = ReplayMode.DRY_RUN) -> ReplayResult:
        checkpoints = self.store.list_run(run_id)
        if not checkpoints:
            return ReplayResult(
                ok=False,
                mode=mode,
                run_id=run_id,
                checkpoint_count=0,
                error="run has no checkpoints",
            )

        return ReplayResult(
            ok=True,
            mode=mode,
            run_id=run_id,
            checkpoint_count=len(checkpoints),
            checkpoints=checkpoints,
        )

    def replay_from_checkpoint(self, checkpoint_id: str) -> ReplayResult:
        checkpoint = self.store.get(checkpoint_id)
        if checkpoint is None:
            return ReplayResult(
                ok=False,
                mode=ReplayMode.FROM_CHECKPOINT,
                run_id="unknown",
                checkpoint_count=0,
                error="checkpoint not found",
            )

        checkpoints = self.store.list_run(checkpoint.run_id)
        tail = [item for item in checkpoints if item.sequence >= checkpoint.sequence]

        return ReplayResult(
            ok=True,
            mode=ReplayMode.FROM_CHECKPOINT,
            run_id=checkpoint.run_id,
            checkpoint_count=len(tail),
            checkpoints=tail,
        )