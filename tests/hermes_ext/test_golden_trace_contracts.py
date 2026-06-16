from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from hermes_ext.golden_trace.contracts import (
    GoldenTraceCase,
    GoldenTraceKind,
    GoldenTracePack,
    GoldenTraceReplayReport,
    GoldenTraceRunConfig,
)


def test_golden_trace_pack_requires_cases() -> None:
    with pytest.raises(ValidationError):
        GoldenTracePack(cases=[])


def test_golden_trace_case_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        GoldenTraceCase(
            case_id="case",
            name="case",
            kind=GoldenTraceKind.DIAGNOSTIC,
            unexpected=True,  # type: ignore[call-arg]
        )


def test_run_config_normalizes_paths(tmp_path: Path) -> None:
    config = GoldenTraceRunConfig(project_root=tmp_path, state_dir=tmp_path / "state")

    assert config.project_root == tmp_path.resolve()
    assert config.state_dir == (tmp_path / "state").resolve()


def test_replay_report_count_validation() -> None:
    with pytest.raises(ValidationError):
        GoldenTraceReplayReport(
            pack_id="pack",
            ok=True,
            repeat=2,
            case_count=1,
            result_count=0,
            passed=0,
            failed=0,
            stable_cases=0,
            unstable_cases=0,
        )