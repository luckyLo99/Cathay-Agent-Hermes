from __future__ import annotations

import json
from collections import Counter

from hermes_ext.integration_spec.contracts import ZeroTouchIntegrationSpec


class IntegrationSpecReporter:
    """
    Pure renderer for zero-touch integration specs.
    """

    def render_json(self, spec: ZeroTouchIntegrationSpec) -> str:
        return json.dumps(spec.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_markdown(self, spec: ZeroTouchIntegrationSpec) -> str:
        mode_counts = Counter(entry.integration_mode.value for entry in spec.matrix.entries)
        status_counts = Counter(entry.status.value for entry in spec.matrix.entries)

        lines = [
            "# Zero-touch Hermes Integration Spec",
            "",
            f"- spec_id: `{spec.spec_id}`",
            f"- phase: `{spec.phase}`",
            f"- project_root: `{spec.project_root}`",
            f"- source_scan_report_id: `{spec.source_scan_report_id}`",
            f"- created_at: `{spec.created_at.isoformat()}`",
            f"- spec_hash: `{spec.spec_hash}`",
            "",
            "## Summary",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| total_entries | {len(spec.matrix.entries)} |",
            f"| forbidden | {mode_counts.get('forbidden', 0)} |",
            f"| no_touch | {mode_counts.get('no_touch', 0)} |",
            f"| external_wrapper | {mode_counts.get('external_wrapper', 0)} |",
            f"| feature_flag_shadow | {mode_counts.get('feature_flag_shadow', 0)} |",
            f"| sidecar_observer | {mode_counts.get('sidecar_observer', 0)} |",
            f"| external_harness | {mode_counts.get('external_harness', 0)} |",
            f"| blocked | {status_counts.get('blocked', 0)} |",
            f"| ready_for_shadow_harness | {status_counts.get('ready_for_shadow_harness', 0)} |",
            "",
            "## Global Constraints",
            "",
        ]

        for constraint in spec.global_constraints:
            lines.append(f"- `{constraint.rule_id}` ({constraint.severity.value}): {constraint.description}")

        lines.extend(["", "## Warnings", ""])
        if spec.warnings:
            lines.extend([f"- {warning}" for warning in spec.warnings])
        else:
            lines.append("- none")

        lines.extend(
            [
                "",
                "## Surface Plans",
                "",
                "| Surface | Total | Forbidden | Wrapper | Feature Flag Shadow | Sidecar | No-touch | Highest Risk | Recommendation |",
                "|---|---:|---:|---:|---:|---:|---:|---|---|",
            ]
        )

        for plan in spec.matrix.surface_plans:
            lines.append(
                "| "
                + " | ".join(
                    [
                        plan.surface.value,
                        str(plan.total_entries),
                        str(plan.forbidden),
                        str(plan.external_wrapper),
                        str(plan.feature_flag_shadow),
                        str(plan.sidecar_observer),
                        str(plan.no_touch),
                        plan.highest_risk.value,
                        self._escape(plan.recommendation),
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Design Matrix",
                "",
                "| Path | Symbol | Surface | Source Posture | Risk | Integration Mode | Status | Required Flags | Rationale |",
                "|---|---|---|---|---|---|---|---|---|",
            ]
        )

        for entry in spec.matrix.entries:
            flags = ", ".join(flag.value for flag in entry.required_flags) or "—"
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{entry.relative_path}`",
                        f"`{entry.symbol}`" if entry.symbol else "—",
                        entry.surface.value,
                        entry.source_posture.value,
                        entry.source_risk.value,
                        entry.integration_mode.value,
                        entry.status.value,
                        self._escape(flags),
                        self._escape(entry.rationale),
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Non-negotiable Rule",
                "",
                "This document is a design matrix only. It must not be interpreted as approval to patch Hermes core files.",
            ]
        )

        return "\n".join(lines)

    @staticmethod
    def _escape(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")