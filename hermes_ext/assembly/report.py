from __future__ import annotations

import json

from hermes_ext.assembly.contracts import AssemblyGateResult, AssemblyManifest


class AssemblyReporter:
    """
    Pure renderer for assembly manifest and release gate reports.
    """

    def render_manifest_json(self, manifest: AssemblyManifest) -> str:
        return json.dumps(manifest.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_gate_json(self, gate: AssemblyGateResult) -> str:
        return json.dumps(gate.to_audit_dict(), ensure_ascii=False, indent=2, sort_keys=True)

    def render_manifest_markdown(self, manifest: AssemblyManifest) -> str:
        lines = [
            "# Shadow Assembly Manifest",
            "",
            f"- manifest_id: `{manifest.manifest_id}`",
            f"- phase: `{manifest.phase}`",
            f"- manifest_hash: `{manifest.manifest_hash}`",
            f"- project_root: `{manifest.project_root}`",
            f"- created_at: `{manifest.created_at.isoformat()}`",
            "",
            "## Summary",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| source_artifacts | {manifest.summary.source_artifacts} |",
            f"| test_artifacts | {manifest.summary.test_artifacts} |",
            f"| report_artifacts | {manifest.summary.report_artifacts} |",
            f"| total_artifacts | {manifest.summary.total_artifacts} |",
            f"| invariants_passed | {manifest.summary.invariants_passed} |",
            f"| invariants_warned | {manifest.summary.invariants_warned} |",
            f"| invariants_failed | {manifest.summary.invariants_failed} |",
            "",
            "## Invariants",
            "",
            "| ID | Status | Severity | Message |",
            "|---|---|---|---|",
        ]

        for invariant in manifest.invariants:
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
                "## Artifacts",
                "",
                "| Path | Kind | Exists | Size | SHA-256 |",
                "|---|---|---:|---:|---|",
            ]
        )

        for artifact in manifest.artifacts:
            sha = artifact.sha256 or "\u2014"
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{artifact.relative_path}`",
                        artifact.kind.value,
                        str(artifact.exists),
                        str(artifact.size_bytes),
                        f"`{sha}`",
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Non-negotiable Rule",
                "",
                "This manifest documents hermes_ext shadow assembly only. It is not approval to modify Hermes core files.",
            ]
        )

        return "\n".join(lines)

    def render_gate_markdown(self, gate: AssemblyGateResult) -> str:
        lines = [
            "# Assembly Release Gate Report",
            "",
            f"- gate_id: `{gate.gate_id}`",
            f"- ok: `{gate.ok}`",
            f"- manifest_hash: `{gate.manifest_hash}`",
            f"- created_at: `{gate.created_at.isoformat()}`",
            "",
            "## Blocking Failures",
            "",
        ]

        if gate.blocking_failures:
            for invariant in gate.blocking_failures:
                lines.append(
                    f"- `{invariant.invariant_id}` ({invariant.severity.value}): {invariant.message}"
                )
        else:
            lines.append("- none")

        lines.extend(["", "## Warnings", ""])
        if gate.warnings:
            for invariant in gate.warnings:
                lines.append(
                    f"- `{invariant.invariant_id}` ({invariant.severity.value}): {invariant.message}"
                )
        else:
            lines.append("- none")

        lines.extend(
            [
                "",
                "## Non-negotiable Rule",
                "",
                "Passing this gate only approves the shadow extension assembly state, not Hermes native integration.",
            ]
        )

        return "\n".join(lines)

    @staticmethod
    def _escape(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")