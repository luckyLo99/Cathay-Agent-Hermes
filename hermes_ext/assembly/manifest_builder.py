from __future__ import annotations

from hermes_ext.assembly.artifact_inventory import AssemblyArtifactInventory
from hermes_ext.assembly.contracts import (
    AssemblyArtifactKind,
    AssemblyInvariantStatus,
    AssemblyManifest,
    AssemblyManifestConfig,
    AssemblySummary,
)
from hermes_ext.assembly.invariant_suite import AssemblyInvariantSuite


class AssemblyManifestBuilder:
    """
    Builds the Phase 11 shadow assembly manifest.

    It is read-only with respect to Hermes core.
    """

    def __init__(self, config: AssemblyManifestConfig) -> None:
        self.config = config

    def build(self) -> AssemblyManifest:
        artifacts = AssemblyArtifactInventory(self.config).collect()
        invariants = AssemblyInvariantSuite(self.config).run(artifacts)

        summary = AssemblySummary(
            source_artifacts=sum(1 for item in artifacts if item.kind == AssemblyArtifactKind.SOURCE),
            test_artifacts=sum(1 for item in artifacts if item.kind == AssemblyArtifactKind.TEST),
            report_artifacts=sum(1 for item in artifacts if item.kind == AssemblyArtifactKind.REPORT),
            total_artifacts=len(artifacts),
            invariants_passed=sum(1 for item in invariants if item.status == AssemblyInvariantStatus.PASS),
            invariants_warned=sum(1 for item in invariants if item.status == AssemblyInvariantStatus.WARN),
            invariants_failed=sum(1 for item in invariants if item.status == AssemblyInvariantStatus.FAIL),
        )

        manifest = AssemblyManifest(
            project_root=str(self.config.project_root),
            artifacts=artifacts,
            invariants=invariants,
            summary=summary,
            metadata={
                "phase": 11,
                "assembly": "end-to-end-shadow-assembly",
                "source": "hermes_ext only",
            },
        ).with_hash()

        return manifest