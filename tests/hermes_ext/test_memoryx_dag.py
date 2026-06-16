from __future__ import annotations

import pytest

from hermes_ext.memoryx.contracts import (
    MemoryEdgeType,
    MemoryNodeKind,
    ShadowMemoryEdge,
    ShadowMemoryNode,
)
from hermes_ext.memoryx.dag import ShadowMemoryDAG


def make_node(node_id: str) -> ShadowMemoryNode:
    return ShadowMemoryNode(
        node_id=node_id,
        trace_id="trace",
        session_id="session",
        turn_id="turn",
        kind=MemoryNodeKind.OBSERVATION,
        title=f"node {node_id}",
        content=f"content {node_id}",
    )


def make_edge(source: str, target: str) -> ShadowMemoryEdge:
    return ShadowMemoryEdge(
        source_node_id=source,
        target_node_id=target,
        edge_type=MemoryEdgeType.DEPENDS_ON,
        reason="test edge",
    )


def test_dag_accepts_acyclic_edges() -> None:
    dag = ShadowMemoryDAG()
    dag = dag.add_node(make_node("a"))
    dag = dag.add_node(make_node("b"))
    dag = dag.add_edge(make_edge("a", "b"))

    assert not dag.has_cycle()
    assert dag.children_of("a") == ["b"]
    assert dag.parents_of("b") == ["a"]


def test_dag_rejects_missing_node() -> None:
    dag = ShadowMemoryDAG().add_node(make_node("a"))

    with pytest.raises(ValueError):
        dag.add_edge(make_edge("a", "b"))


def test_dag_rejects_cycle() -> None:
    dag = ShadowMemoryDAG()
    dag = dag.add_node(make_node("a"))
    dag = dag.add_node(make_node("b"))
    dag = dag.add_edge(make_edge("a", "b"))

    with pytest.raises(ValueError):
        dag.add_edge(make_edge("b", "a"))