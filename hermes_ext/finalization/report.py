from __future__ import annotations

import json

from hermes_ext.finalization.contracts import (
    DocumentationPack,
    FinalizationBundle,
    MergeReadinessReport,
)


class FinalizationReporter:
    """
    Pure renderer for Phase 12 finalization outputs.
    """

    def render_documentation_json(self, pack: DocumentationPack) -> str:
        return json.dumps(pack.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_readiness_json(self, report: MergeReadinessReport) -> str:
        return json.dumps(report.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_bundle_json(self, bundle: FinalizationBundle) -> str:
        return json.dumps(bundle.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_documentation_markdown(self, pack: DocumentationPack) -> str:
        lines = [
            "# Final Stabilization Documentation Pack",
            "",
            f"- pack_id: `{pack.pack_id}`",
            f"- phase: `{pack.phase}`",
            f"- pack_hash: `{pack.pack_hash}`",
            f"- created_at: `{pack.created_at.isoformat()}`",
            "",
            "## Evidence Paths",
            "",
        ]

        for path in pack.evidence_paths:
            lines.append(f"- `{path}`")

        for section in sorted(pack.sections, key=lambda item: item.priority):
            lines.extend(["", f"## {section.title}", "", section.body])

        lines.extend(
            [
                "",
                "## Non-negotiable Rule",
                "",
                "This documentation pack only describes the hermes_ext shadow extension. It does not approve Hermes native integration.",
            ]
        )

        return "\n".join(lines)

    def render_readiness_markdown(self, report: MergeReadinessReport) -> str:
        lines = [
            "# Merge Readiness Report",
            "",
            f"- report_id: `{report.report_id}`",
            f"- phase: `{report.phase}`",
            f"- ok: `{report.ok}`",
            f"- readiness_hash: `{report.readiness_hash}`",
            f"- evidence_count: `{report.evidence_count}`",
            f"- passed: `{report.passed}`",
            f"- warned: `{report.warned}`",
            f"- failed: `{report.failed}`",
            f"- created_at: `{report.created_at.isoformat()}`",
            "",
            "## Invariants",
            "",
            "| ID | Status | Severity | Message |",
            "|---|---|---|---|",
        ]

        for invariant in report.invariants:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{invariant.invariant_id}`",
                        invariant.status.value,
                        invariant.severity.value,
                        self._escape(invariant.message),
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Blocking Interpretation",
                "",
                "- `ok=true` means the shadow extension documentation and evidence are merge-ready.",
                "- It does not mean Hermes native integration is approved.",
                "- Any future native experiment must start from a new explicitly approved phase.",
            ]
        )

        return "\n".join(lines)

    def render_rollback_index_markdown(self, pack: DocumentationPack) -> str:
        section = next(
            (item for item in pack.sections if item.title == "Rollback Index"),
            None,
        )
        body = section.body if section else "Rollback index section missing."

        return "\n".join(
            [
                "# Phase 12 Rollback Index",
                "",
                body,
                "",
                "## Rule",
                "",
                "Rollback must target the last known safe phase tag and must not partially delete Hermes native files.",
            ]
        )

    def render_maintenance_guide_markdown(self, pack: DocumentationPack) -> str:
        section = next(
            (item for item in pack.sections if item.title == "Maintenance Guide"),
            None,
        )
        body = section.body if section else "Maintenance guide section missing."

        return "\n".join(
            [
                "# Phase 12 Maintenance Guide",
                "",
                body,
                "",
                "## Rule",
                "",
                "Maintenance is allowed only inside hermes_ext unless a later phase explicitly approves native integration.",
            ]
        )

    @staticmethod
    def _escape(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")