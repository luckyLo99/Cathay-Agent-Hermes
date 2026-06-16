from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.golden_trace.contracts import GoldenTraceRunConfig
from hermes_ext.golden_trace.report import GoldenTraceReporter
from hermes_ext.golden_trace.runner import GoldenTraceRunner


def test_golden_trace_reporter_renders_markdown_and_json(tmp_path: Path) -> None:
    report = GoldenTraceRunner(
        GoldenTraceRunConfig(
            project_root=Path.cwd(),
            state_dir=tmp_path / "state",
            repeat=1,
            native_boundary_limit=5,
        )
    ).run_default_pack()

    renderer = GoldenTraceReporter()
    markdown = renderer.render_markdown(report)
    json_text = renderer.render_json(report)
    parsed = json.loads(json_text)

    assert "# Golden Trace Replay Report" in markdown
    assert "Non-negotiable Rule" in markdown
    assert parsed["ok"] is True