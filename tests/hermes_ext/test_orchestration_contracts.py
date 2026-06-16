from __future__ import annotations

import pytest
from pydantic import ValidationError

from hermes_ext.orchestration.contracts import (
    CheckpointKind,
    ShadowCheckpoint,
    ShadowRunConfig,
    ShadowRunResult,
    ShadowRunStatus,
    ShadowStepName,
)


def test_checkpoint_hash_is_stable() -> None:
    checkpoint = ShadowCheckpoint(
        run_id="run",
        session_id="session",
        step_name=ShadowStepName.PREPARE_ENVELOPE,
        kind=CheckpointKind.INPUT,
        sequence=0,
        state={"x": 1},
    ).with_hash()

    assert checkpoint.state_hash
    assert checkpoint.with_hash().state_hash == checkpoint.state_hash


def test_config_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        ShadowRunConfig(
            unexpected=True,  # type: ignore[call-arg]
        )


def test_completed_result_requires_final_checkpoint() -> None:
    with pytest.raises(ValidationError):
        ShadowRunResult(
            run_id="run",
            session_id="session",
            status=ShadowRunStatus.COMPLETED,
            checkpoint_count=1,
        )


def test_failed_result_requires_error() -> None:
    with pytest.raises(ValidationError):
        ShadowRunResult(
            run_id="run",
            session_id="session",
            status=ShadowRunStatus.FAILED,
            checkpoint_count=1,
        )