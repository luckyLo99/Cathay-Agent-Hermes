from __future__ import annotations

import json

from hermes_ext.adapter_scan.contracts import AdapterScanReport


class AdapterScanReporter:
    """
    Render adapter scan reports.

    The renderer is pure: it returns strings and does not write files.
    """

    def render_markdown(self, report: AdapterScanReport) -> str:
        lines = [
            "# Hermes Adapter Scan Report",
            "",
            f"- report_id: `{report.report_id}`",
            f"- project_root: `{report.project_root}`",
            f"- created_at: `{report.created_at.isoformat()}`",
            "",
            "## Summary",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| files_scanned | {report.summary.files_scanned} |",
            f"| lifeline_files_found | {report.summary.lifeline_files_found} |",
            f"| candidates_found | {report.summary.candidates_found} |",
            f"| forbidden_candidates | {report.summary.forbidden_candidates} |",
            f"| wrapper_only_candidates | {report.summary.wrapper_only_candidates} |",
            f"| feature_flag_candidates | {report.summary.feature_flag_candidates} |",
            f"| parse_errors | {report.summary.parse_errors} |",
            "",
            "## Warnings",
            "",
        ]

        if report.warnings:
            lines.extend([f"- {warning}" for warning in report.warnings])
        else:
            lines.append("- none")

        lines.extend(
            [
                "",
                "## Extension Point Candidates",
                "",
                "| Path | Surface | Posture | Risk | Symbol | Line | Reason | Future Hint |",
                "|---|---|---|---|---|---:|---|---|",
            ]
        )

        for candidate in report.candidates:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{candidate.relative_path}`",
                        candidate.surface.value,
                        candidate.posture.value,
                        candidate.risk.value,
                        f"`{candidate.symbol}`" if candidate.symbol else "—",
                        str(candidate.line),
                        self._escape(candidate.reason),
                        self._escape(candidate.future_adapter_hint),
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Files Scanned",
                "",
                "| Path | Surface Guess | Lifeline | Lines | Imports | Symbols | Parse Error |",
                "|---|---|---:|---:|---:|---:|---|",
            ]
        )

        for record in report.files:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{record.relative_path}`",
                        record.surface_guess.value,
                        "yes" if record.is_lifeline else "no",
                        str(record.line_count),
                        str(len(record.imports)),
                        str(len(record.symbols)),
                        self._escape(record.parse_error or "—"),
                    ]
                )
                + " |"
            )

        return "\n".join(lines)

    def render_json(self, report: AdapterScanReport) -> str:
        return json.dumps(report.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    @staticmethod
    def _escape(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")