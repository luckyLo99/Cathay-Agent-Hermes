"""
Runtime primitives for the Hermes extension layer.

These primitives are intentionally offline-first:
- no real provider call
- no network call
- no mutation of Hermes core state
"""

from __future__ import annotations

from hermes_ext.runtime.mock_provider import MockProviderAdapter, MockProviderConfig
from hermes_ext.runtime.request_envelope import (
    EnvelopeStatus,
    LLMRequestEnvelope,
    LLMResponse,
    LLMUsage,
    PromptSegment,
    ToolPlan,
)

__all__ = [
    "EnvelopeStatus",
    "LLMRequestEnvelope",
    "LLMResponse",
    "LLMUsage",
    "MockProviderAdapter",
    "MockProviderConfig",
    "PromptSegment",
    "ToolPlan",
]