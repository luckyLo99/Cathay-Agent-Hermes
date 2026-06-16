"""
memoryx-style shadow memory layer.

Phase 4 rules:
- Do not import memoryx.
- Do not import Cathay-Agent.
- Do not write Hermes native memory.
- Do not write Hermes skills.
- Store only shadow memory nodes in an isolated database.
"""

from __future__ import annotations

from hermes_ext.memoryx.contracts import (
    MemoryEdgeType,
    MemoryNodeKind,
    MemoryNodeStatus,
    MemoryPIILevel,
    ShadowMemoryEdge,
    ShadowMemoryNode,
    ShadowMemoryQuery,
    ShadowMemoryRecallResult,
    ShadowMemoryWriteRequest,
)
from hermes_ext.memoryx.provider import ShadowMemoryProvider

__all__ = [
    "MemoryEdgeType",
    "MemoryNodeKind",
    "MemoryNodeStatus",
    "MemoryPIILevel",
    "ShadowMemoryEdge",
    "ShadowMemoryNode",
    "ShadowMemoryProvider",
    "ShadowMemoryQuery",
    "ShadowMemoryRecallResult",
    "ShadowMemoryWriteRequest",
]