from __future__ import annotations

from hermes_ext.assembly.contracts import (
    AssemblyInvariant,
    AssemblyInvariantSeverity,
    AssemblyInvariantStatus,
    AssemblyManifest,
    AssemblySummary,
)
from hermes_ext.assembly.release_gate import AssemblyReleaseGate


def manifest_with_invariant(invariant: AssemblyInvariant) -> AssemblyManifest:
    return AssemblyManifest(
        project_root=".",
        artifacts=[],
        invariants=[invariant],
        summary=AssemblySummary(
            total_artifacts=0,
            invariants_passed=1 if invariant.status == AssemblyInvariantStatus.PASS else 0,
            invariants_warned=1 if invariant.status == AssemblyInvariantStatus.WARN else 0,
            invariants_failed=1 if invariant.status == AssemblyInvariantStatus.FAIL else 0,
        ),
    ).with_hash()


def test_release_gate_passes_without_failures() -> None:
    manifest = manifest_with_invariant(
        AssemblyInvariant(
            invariant_id="ok",
            status=AssemblyInvariantStatus.PASS,
            severity=AssemblyInvariantSeverity.INFO,
            message="ok",
        )
    )

    gate = AssemblyReleaseGate().evaluate(manifest)

    assert gate.ok


def test_release_gate_blocks_critical_failure() -> None:
    manifest = manifest_with_invariant(
        AssemblyInvariant(
            invariant_id="fail",
            status=AssemblyInvariantStatus.FAIL,
            severity=AssemblyInvariantSeverity.CRITICAL,
            message="bad",
        )
    )

    gate = AssemblyReleaseGate().evaluate(manifest)

    assert not gate.ok
    assert gate.blocking_failures


def test_release_gate_allows_warning() -> None:
    manifest = manifest_with_invariant(
        AssemblyInvariant(
            invariant_id="warn",
            status=AssemblyInvariantStatus.WARN,
            severity=AssemblyInvariantSeverity.WARNING,
            message="warn",
        )
    )

    gate = AssemblyReleaseGate().evaluate(manifest)

    assert gate.ok
    assert gate.warnings