from __future__ import annotations

from pathlib import Path

from hermes_ext.golden_trace.contracts import GoldenTraceRunConfig
from hermes_ext.golden_trace.runner import GoldenTraceRunner


def test_golden_trace_runner_replays_default_pack(tmp_path: Path) -> None:
    report = GoldenTraceRunner(
        GoldenTraceRunConfig(
            project_root=Path.cwd(),
            state_dir=tmp_path / "state",
            repeat=2,
            native_boundary_limit=10,
        )
    ).run_default_pack()

    assert report.ok
    assert report.repeat == 2
    assert report.case_count >= 5
    assert report.failed == 0
    assert report.unstable_cases == 0
    assert report.report_hash


def test_golden_trace_runner_uses_spec_json_when_present(tmp_path: Path) -> None:
    spec_json = Path("reports/phase8/zero_touch_integration_spec.json")
    if not spec_json.exists():
        return

    report = GoldenTraceRunner(
        GoldenTraceRunConfig(
            project_root=Path.cwd(),
            state_dir=tmp_path / "state",
            repeat=1,
            spec_json=spec_json,
            native_boundary_limit=5,
        )
    ).run_default_pack()

    assert report.ok
    assert report.failed == 0