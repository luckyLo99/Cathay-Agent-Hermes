from __future__ import annotations

import pytest
from pydantic import ValidationError

from hermes_ext.memoryx.contracts import (
    MemoryEdgeType,
    MemoryNodeKind,
    MemoryNodeStatus,
    MemoryPIILevel,
    ShadowMemoryEdge,
    ShadowMemoryNode,
    ShadowMemoryQuery,
)


def make_node(**kwargs) -> ShadowMemoryNode:
    base = {
        "trace_id": "trace",
        "session_id": "session",
        "turn_id": "turn",
        "kind": MemoryNodeKind.OBSERVATION,
        "title": "title",
        "content": "content",
    }
    base.update(kwargs)
    return ShadowMemoryNode(**base)


def test_shadow_memory_node_hash_is_stable() -> None:
    node = make_node().with_hash()

    assert node.content_hash
    assert len(node.content_hash) == 64
    assert node.with_hash().content_hash == node.content_hash


def test_high_pii_must_be_quarantined() -> None:
    with pytest.raises(ValidationError):
        make_node(pii_level=MemoryPIILevel.HIGH, status=MemoryNodeStatus.SHADOW)


def test_quarantined_high_pii_is_allowed() -> None:
    node = make_node(pii_level=MemoryPIILevel.HIGH, status=MemoryNodeStatus.QUARANTINED)

    assert node.status == MemoryNodeStatus.QUARANTINED


def test_edge_rejects_self_edge() -> None:
    with pytest.raises(ValidationError):
        ShadowMemoryEdge(
            source_node_id="a",
            target_node_id="a",
            edge_type=MemoryEdgeType.SUPPORTS,
            reason="self",
        )


def test_query_rejects_empty_string() -> None:
    with pytest.raises(ValidationError):
        ShadowMemoryQuery(query="")