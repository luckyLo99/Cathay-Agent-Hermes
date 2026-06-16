from __future__ import annotations

import json
from collections import Counter

from hermes_ext.native_boundary.contracts import NativeBoundaryContractRunResult


class NativeBoundaryContractReporter:
    """
    Pure renderer for no-op native boundary contract reports.
    """

    def render_json(self, result: NativeBoundaryContractRunResult) -> str:
        return json.dumps(result.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_markdown(self, result: NativeBoundaryContractRunResult) -> str:
        verdict_counts = Counter(item.verdict.value for item in result.results)

        lines = [
            "# No-op Native Boundary Contract Report",
            "",
            f"- run_id: `{result.run_id}`",
            f"- ok: `{result.ok}`",
            f"- case_count: `{result.case_count}`",
            f"- passed: `{result.passed}`",
            f"- failed: `{result.failed}`",
            f"- created_at: `{result.created_at.isoformat()}`",
            "",
            "## Summary",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| noop | {verdict_counts.get('noop', 0)} |",
            f"| blocked | {verdict_counts.get('blocked', 0)} |",
            f"| violations | {len(result.violations)} |",
            "",
            "## Boundary Results",
            "",
            "| Request | Verdict | Reason | Native Called | Tool Executed | Provider Called | Memory Written | State Mutated | Patch Generated |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]

        for item in result.results:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item.request_id}`",
                        item.verdict.value,
                        self._escape(item.reason),
                        str(item.native_called),
                        str(item.tool_executed),
                        str(item.provider_called),
                        str(item.memory_written),
                        str(item.state_mutated),
                        str(item.patch_generated),
                    ]
                )
                + " |"
            )

        lines.extend(["", "## Violations", ""])
        if result.violations:
            for violation in result.violations:
                lines.append(
                    f"- `{violation.rule_id}` ({violation.severity}) "
                    f"request=`{violation.request_id}`: {violation.message}"
                )
        else:
            lines.append("- none")

        lines.extend(
            [
                "",
                "## Non-negotiable Rule",
                "",
                "Passing this report does not approve Hermes core integration. It only proves the native boundary is no-op by default.",
            ]
        )

        return "\n".join(lines)

    @staticmethod
    def _escape(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")