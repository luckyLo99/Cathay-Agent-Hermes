"""
Cathay read-only adapter layer.

Phase 3 rules:
- Do not import Cathay-Agent source code.
- Do not execute Cathay runtime.
- Do not write Hermes memory or skills.
- Normalize Cathay-like signals into portable DTOs only.
"""

from __future__ import annotations

from hermes_ext.cathay.adapter import CathayContractAdapter
from hermes_ext.cathay.contracts import (
    CathayAdapterInput,
    CathayAdapterOutput,
    CathayIntent,
    CathayLearningSignal,
    CathayProfileHypothesis,
    CathayProactiveSuggestion,
    CathaySafetySignal,
    CathaySignalBundle,
    CathaySignalSeverity,
    CathaySignalSource,
)
from hermes_ext.cathay.signal_fusion import CathaySignalFusion

__all__ = [
    "CathayAdapterInput",
    "CathayAdapterOutput",
    "CathayContractAdapter",
    "CathayIntent",
    "CathayLearningSignal",
    "CathayProfileHypothesis",
    "CathayProactiveSuggestion",
    "CathaySafetySignal",
    "CathaySignalBundle",
    "CathaySignalFusion",
    "CathaySignalSeverity",
    "CathaySignalSource",
]