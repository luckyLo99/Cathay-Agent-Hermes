from __future__ import annotations

import json
from collections import defaultdict

from hermes_ext.golden_trace.contracts import GoldenTraceReplayReport


class GoldenTraceReporter:
    """
    Pure renderer for golden trace replay reports.
    """

    def render_json(self, report: GoldenTraceReplayReport) -> str:
        return json.dumps(report.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_markdown(self, report: GoldenTraceReplayReport) -> str:
        grouped: dict[str, list[str]] = defaultdict(list)
        for result in report.results:
            grouped[result.case_id].append(result.canonical_hash)

        lines = [
            "# Golden Trace Replay Report",
            "",
            f"- report_id: `{report.report_id}`",
            f"- ok: `{report.ok}`",
            f"- repeat: `{report.repeat}`",
            f"- case_count: `{report.case_count}`",
            f"- result_count: `{report.result_count}`",
            f"- passed: `{report.passed}`",
            f"- failed: `{report.failed}`",
            f"- stable_cases: `{report.stable_cases}`",
            f"- unstable_cases: `{report.unstable_cases}`",
            f"- report_hash: `{report.report_hash}`",
            f"- created_at: `{report.created_at.isoformat()}`",
            "",
            "## Case Hash Stability",
            "",
            "| Case | Iterations | Unique Hashes | Stable |",
            "|---|---:|---:|---:|",
        ]

        for case_id, hashes in sorted(grouped.items()):
            unique_hashes = set(hashes)
            lines.append(
                f"| `{case_id}` | {len(hashes)} | {len(unique_hashes)} | {len(unique_hashes) == 1} |"
            )

        lines.extend(["", "## Violations", ""])
        if report.violations:
            lines.extend([f"- {self._escape(item)}" for item in report.violations])
        else:
            lines.append("- none")

        lines.extend(
            [
                "",
                "## Results",
                "",
                "| Case | Iteration | Status | OK | Canonical Hash | Error |",
                "|---|---:|---|---:|---|---|",
            ]
        )

        for result in report.results:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{result.case_id}`",
                        str(result.iteration),
                        result.status.value,
                        str(result.ok),
                        f"`{result.canonical_hash}`",
                        self._escape(result.error or "—"),
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Non-negotiable Rule",
                "",
                "Passing golden trace replay proves deterministic shadow behavior only. It does not approve Hermes core integration.",
            ]
        )

        return "\n".join(lines)

    @staticmethod
    def _escape(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")