from __future__ import annotations

from hermes_ext.assembly.contracts import (
    AssemblyGateResult,
    AssemblyInvariantSeverity,
    AssemblyInvariantStatus,
    AssemblyManifest,
)


class AssemblyReleaseGate:
    """
    Release-style gate over the assembly manifest.

    Critical/error failures block. Warnings are reported but do not block.
    """

    def evaluate(self, manifest: AssemblyManifest) -> AssemblyGateResult:
        blocking = [
            invariant
            for invariant in manifest.invariants
            if invariant.status == AssemblyInvariantStatus.FAIL
            and invariant.severity in {
                AssemblyInvariantSeverity.ERROR,
                AssemblyInvariantSeverity.CRITICAL,
            }
        ]

        warnings = [
            invariant
            for invariant in manifest.invariants
            if invariant.status == AssemblyInvariantStatus.WARN
        ]

        return AssemblyGateResult(
            ok=not blocking,
            manifest_hash=manifest.manifest_hash,
            blocking_failures=blocking,
            warnings=warnings,
        )