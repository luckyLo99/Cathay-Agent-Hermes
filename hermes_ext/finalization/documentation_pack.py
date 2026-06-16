from __future__ import annotations

from hermes_ext.finalization.contracts import (
    DocumentationPack,
    DocumentationSection,
    FinalizationEvidence,
)


class FinalDocumentationPackBuilder:
    """
    Builds a human-readable final documentation pack from prior evidence.

    This does not modify README, changelog, or Hermes core docs.
    It emits generated reports only.
    """

    def build(self, evidence: list[FinalizationEvidence]) -> DocumentationPack:
        evidence_paths = [item.relative_path for item in evidence if item.exists]
        evidence_by_path = {item.relative_path: item for item in evidence}

        sections = [
            self._executive_summary(evidence_by_path),
            self._architecture_summary(),
            self._safety_invariants(evidence_by_path),
            self._operator_commands(),
            self._rollback_index(),
            self._merge_readiness_notes(),
            self._maintenance_guide(),
        ]

        return DocumentationPack(
            sections=sections,
            evidence_paths=evidence_paths,
        ).with_hash()

    def _executive_summary(self, evidence: dict[str, FinalizationEvidence]) -> DocumentationSection:
        gate = evidence.get("reports/phase11/release_gate_report.json")
        manifest = evidence.get("reports/phase11/shadow_assembly_manifest.json")
        test_result = evidence.get("reports/phase11/phase11_test_result.md")

        gate_ok = (gate.json_payload or {}).get("ok") if gate else None
        manifest_hash = (manifest.json_payload or {}).get("manifest_hash") if manifest else None
        test_excerpt = test_result.text_excerpt if test_result else ""

        body = (
            "Phase 12 finalization packages the hermes_ext shadow architecture for merge-readiness review. "
            "It does not approve Hermes native integration and does not patch Hermes core.\n\n"
            f"- Phase 11 release gate ok: `{gate_ok}`\n"
            f"- Assembly manifest hash: `{manifest_hash}`\n"
            f"- Test evidence contains 241/241 PASS: `{('241/241' in test_excerpt) or ('总通过 | 241' in test_excerpt)}`"
        )

        return DocumentationSection(
            title="Executive Summary",
            body=body,
            priority=10,
        )

    def _architecture_summary(self) -> DocumentationSection:
        body = (
            "The shadow architecture remains isolated under hermes_ext:\n\n"
            "- runtime: request envelope, mock provider, agent doctor.\n"
            "- schema: portable schema validation.\n"
            "- hooks/security: hook dispatcher, PreToolGuard, path/url/command/exec policies.\n"
            "- cathay: read-only signal adapter.\n"
            "- memoryx: isolated shadow memory provider.\n"
            "- orchestration: checkpoint, replay, span log, circuit breaker.\n"
            "- harness: feature flags and explicit integration harness.\n"
            "- adapter_scan: read-only Hermes adapter mapping.\n"
            "- integration_spec: zero-touch integration design matrix.\n"
            "- native_boundary: no-op / blocked native boundary contract.\n"
            "- golden_trace: deterministic replay pack.\n"
            "- assembly: release-style manifest and invariant gate.\n"
            "- finalization: documentation pack, merge readiness gate, stabilization bundle."
        )

        return DocumentationSection(
            title="Architecture Summary",
            body=body,
            priority=20,
        )

    def _safety_invariants(self, evidence: dict[str, FinalizationEvidence]) -> DocumentationSection:
        manifest = evidence.get("reports/phase11/shadow_assembly_manifest.json")
        payload = manifest.json_payload if manifest else {}
        invariants = payload.get("invariants", []) if isinstance(payload, dict) else []

        lines = [
            "The following Phase 11 assembly invariants are treated as non-negotiable release gates:",
            "",
        ]

        if isinstance(invariants, list) and invariants:
            for item in invariants:
                if isinstance(item, dict):
                    lines.append(
                        f"- `{item.get('invariant_id')}` -> `{item.get('status')}` / `{item.get('severity')}`"
                    )
        else:
            lines.append("- No manifest invariants were loaded.")

        lines.extend(
            [
                "",
                "If any critical invariant fails, Phase 12 must not be treated as merge-ready.",
            ]
        )

        return DocumentationSection(
            title="Safety Invariants",
            body="\n".join(lines),
            priority=30,
        )

    def _operator_commands(self) -> DocumentationSection:
        body = (
            "Recommended final verification commands:\n\n"
            "```bash\n"
            ".venv\\Scripts\\python -m pytest tests\\hermes_ext -q\n"
            ".venv\\Scripts\\python -m hermes_ext.runtime.agent_doctor --json --project-root .\n"
            ".venv\\Scripts\\python -m hermes_ext.harness.cli doctor --project-root . --state-dir .hermes_ext_shadow --json\n"
            ".venv\\Scripts\\python -m hermes_ext.assembly.cli \\\n"
            "  --project-root . \\\n"
            "  --manifest-md reports\\phase11\\shadow_assembly_manifest.md \\\n"
            "  --manifest-json reports\\phase11\\shadow_assembly_manifest.json \\\n"
            "  --gate-md reports\\phase11\\release_gate_report.md \\\n"
            "  --gate-json reports\\phase11\\release_gate_report.json\n"
            ".venv\\Scripts\\python -m hermes_ext.finalization.cli \\\n"
            "  --project-root . \\\n"
            "  --output-dir reports\\phase12\n"
            ".venv\\Scripts\\python cli.py --help\n"
            ".venv\\Scripts\\hermes doctor\n"
            "```"
        )

        return DocumentationSection(
            title="Operator Commands",
            body=body,
            priority=40,
        )

    def _rollback_index(self) -> DocumentationSection:
        body = (
            "Rollback anchors:\n\n"
            "- Phase 11 rollback: `git reset --hard phase10-golden-trace-replay`\n"
            "- Phase 10 rollback: `git reset --hard phase9-noop-native-boundary-contracts`\n"
            "- Phase 9 rollback: `git reset --hard phase8-zero-touch-integration-spec`\n"
            "- Phase 8 rollback: `git reset --hard phase7-readonly-adapter-scan`\n"
            "- Phase 7 rollback: `git reset --hard phase6-feature-flag-harness`\n"
            "- Phase 6 rollback: `git reset --hard phase5-shadow-orchestration-replay`\n"
            "- Phase 5 rollback: `git reset --hard phase4-memoryx-shadow-provider`\n"
            "- Phase 4 rollback: `git reset --hard phase3-cathay-readonly-adapter`\n"
            "- Phase 3 rollback: `git reset --hard phase2-hook-pretool-policy`\n"
            "- Phase 2 rollback: `git reset --hard phase1-offline-runtime-skeleton`\n"
            "- Phase 1 rollback: `git reset --hard baseline-before-fusion`"
        )

        return DocumentationSection(
            title="Rollback Index",
            body=body,
            priority=50,
        )

    def _merge_readiness_notes(self) -> DocumentationSection:
        body = (
            "Merge readiness is limited to hermes_ext shadow extension artifacts.\n\n"
            "Merge-ready means:\n\n"
            "- tests pass;\n"
            "- release gate passes;\n"
            "- no critical invariant fails;\n"
            "- golden traces are stable;\n"
            "- no-op native boundary remains side-effect free;\n"
            "- feature flags are disabled by default;\n"
            "- Hermes native files remain untouched.\n\n"
            "Merge-ready does not mean:\n\n"
            "- Hermes core integration is approved;\n"
            "- native providers may be called;\n"
            "- tools may execute;\n"
            "- native memory may be written;\n"
            "- prompt/state/runtime files may be patched."
        )

        return DocumentationSection(
            title="Merge Readiness Notes",
            body=body,
            priority=60,
        )

    def _maintenance_guide(self) -> DocumentationSection:
        body = (
            "Maintenance rules after Phase 12:\n\n"
            "1. Any new hermes_ext module must include a no-import test.\n"
            "2. Any runnable behavior must be gated by HERMES_EXT_ENABLED and kill-switch compatible.\n"
            "3. Any tool-shaped behavior must pass through PreToolGuard.\n"
            "4. Any memory-shaped behavior must remain shadow-only unless a later explicit phase approves native integration.\n"
            "5. Any new trace-sensitive behavior must add or update golden trace cases.\n"
            "6. Any new report-producing module must include markdown and JSON output.\n"
            "7. Any future native boundary must remain no-op by default.\n"
            "8. Any attempt to touch Hermes lifeline files requires a new phase, explicit approval, and a rollback plan."
        )

        return DocumentationSection(
            title="Maintenance Guide",
            body=body,
            priority=70,
        )