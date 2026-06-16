"""
Final stabilization and merge-readiness package.

Phase 12 rules:
- Do not import Hermes core modules.
- Do not execute real tools.
- Do not call real providers or models.
- Do not write Hermes native memory.
- Do not mutate Hermes state.
- Do not generate patches.
"""

from __future__ import annotations

from hermes_ext.finalization.contracts import (
    DocumentationPack,
    FinalizationBundle,
    FinalizationConfig,
    FinalizationEvidence,
    MergeReadinessReport,
    ReadinessInvariant,
)
from hermes_ext.finalization.documentation_pack import FinalDocumentationPackBuilder
from hermes_ext.finalization.evidence_loader import FinalizationEvidenceLoader
from hermes_ext.finalization.merge_gate import MergeReadinessGate

__all__ = [
    "DocumentationPack",
    "FinalDocumentationPackBuilder",
    "FinalizationBundle",
    "FinalizationConfig",
    "FinalizationEvidence",
    "FinalizationEvidenceLoader",
    "MergeReadinessGate",
    "MergeReadinessReport",
    "ReadinessInvariant",
]