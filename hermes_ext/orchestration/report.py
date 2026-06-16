from __future__ import annotations

from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.contracts import ShadowRunResult


class ShadowRunReporter:
    """
    Markdown report renderer for shadow runs.
    """

    def __init__(self, store: CheckpointStore) -> None:
        self.store = store

    def render_markdown(self, result: ShadowRunResult) -> str:
        checkpoints = self.store.list_run(result.run_id)
        lines = [
            "# Shadow Run Report",
            "",
            f"- run_id: `{result.run_id}`",
            f"- session_id: `{result.session_id}`",
            f"- status: `{result.status.value}`",
            f"- checkpoint_count: `{result.checkpoint_count}`",
            f"- final_checkpoint_id: `{result.final_checkpoint_id}`",
            "",
            "## Warnings",
            "",
        ]

        if result.warnings:
            lines.extend([f"- {warning}" for warning in result.warnings])
        else:
            lines.append("- none")

        lines.extend(["", "## Checkpoints", ""])

        for checkpoint in checkpoints:
            lines.append(
                f"- `{checkpoint.sequence}` `{checkpoint.kind.value}` "
                f"`{checkpoint.step_name.value}` `{checkpoint.checkpoint_id}`"
            )

        if result.error:
            lines.extend(["", "## Error", "", result.error])

        return "\n".join(lines)