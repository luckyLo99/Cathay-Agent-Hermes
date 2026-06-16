from __future__ import annotations

import json

from hermes_ext.assembly.contracts import (
    AssemblyInvariant,
    AssemblyInvariantSeverity,
    AssemblyInvariantStatus,
    AssemblyManifest,
    AssemblySummary,
)
from hermes_ext.assembly.release_gate import AssemblyReleaseGate
from hermes_ext.assembly.report import AssemblyReporter


def test_assembly_reporter_renders_manifest_and_gate() -> None:
    invariant = AssemblyInvariant(
        invariant_id="ok",
        status=AssemblyInvariantStatus.PASS,
        severity=AssemblyInvariantSeverity.INFO,
        message="ok",
    )
    manifest = AssemblyManifest(
        project_root=".",
        artifacts=[],
        invariants=[invariant],
        summary=AssemblySummary(
            total_artifacts=0,
            invariants_passed=1,
            invariants_warned=0,
            invariants_failed=0,
        ),
    ).with_hash()
    gate = AssemblyReleaseGate().evaluate(manifest)
    reporter = AssemblyReporter()

    manifest_md = reporter.render_manifest_markdown(manifest)
    gate_md = reporter.render_gate_markdown(gate)
    manifest_json = reporter.render_manifest_json(manifest)
    gate_json = reporter.render_gate_json(gate)

    assert "# Shadow Assembly Manifest" in manifest_md
    assert "# Assembly Release Gate Report" in gate_md
    assert json.loads(manifest_json)["manifest_hash"]
    assert json.loads(gate_json)["ok"] is True