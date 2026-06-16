"""
Hook bus for Hermes extension layer.

Phase 2 rules:
- no Hermes core mutation
- no real tool execution
- no network calls
- no API key reads
- pure contracts + deterministic decisions only
"""

from __future__ import annotations

from hermes_ext.hooks.contracts import (
    HookDecision,
    HookDecisionType,
    HookEvent,
    HookEventName,
    HookResult,
)
from hermes_ext.hooks.dispatcher import HookDispatcher, HookHandler

__all__ = [
    "HookDecision",
    "HookDecisionType",
    "HookDispatcher",
    "HookEvent",
    "HookEventName",
    "HookHandler",
    "HookResult",
]