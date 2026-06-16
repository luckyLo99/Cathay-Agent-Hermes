from __future__ import annotations

from pathlib import Path

from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.contracts import ShadowRunConfig
from hermes_ext.orchestration.report import ShadowRunReporter
from hermes_ext.orchestration.shadow_runner import ShadowRunner


def test_shadow_run_reporter_renders_markdown(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.db")
    runner = ShadowRunner(
        checkpoint_store=store,
        shadow_memory_provider=ShadowMemoryProvider(tmp_path / "shadow.db"),
    )
    result = runner.run_text(
        "report generation",
        config=ShadowRunConfig(run_id="run-report", session_id="session"),
    )

    markdown = ShadowRunReporter(store).render_markdown(result)

    assert "# Shadow Run Report" in markdown
    assert "run-report" in markdown
    assert "## Checkpoints" in markdown