"""
End-to-end shadow assembly manifest.

Phase 11 rules:
- Do not import Hermes core modules.
- Do not execute real tools.
- Do not call real providers or models.
- Do not write Hermes native memory.
- Do not mutate Hermes state.
- Do not generate patches.
"""

from __future__ import annotations

from hermes_ext.assembly.contracts import (
    AssemblyArtifact,
    AssemblyArtifactKind,
    AssemblyGateResult,
    AssemblyInvariant,
    AssemblyInvariantSeverity,
    AssemblyInvariantStatus,
    AssemblyManifest,
    AssemblyManifestConfig,
)
from hermes_ext.assembly.manifest_builder import AssemblyManifestBuilder
from hermes_ext.assembly.release_gate import AssemblyReleaseGate

__all__ = [
    "AssemblyArtifact",
    "AssemblyArtifactKind",
    "AssemblyGateResult",
    "AssemblyInvariant",
    "AssemblyInvariantSeverity",
    "AssemblyInvariantStatus",
    "AssemblyManifest",
    "AssemblyManifestBuilder",
    "AssemblyManifestConfig",
    "AssemblyReleaseGate",
]
