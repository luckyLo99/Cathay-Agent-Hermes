from __future__ import annotations

from pathlib import Path

from hermes_ext.memoryx.contracts import (
    MemoryNodeKind,
    MemoryNodeStatus,
    MemoryPIILevel,
    ShadowMemoryNode,
    ShadowMemoryQuery,
    ShadowMemoryWriteRequest,
)
from hermes_ext.memoryx.provider import ShadowMemoryProvider


def make_provider(tmp_path: Path) -> ShadowMemoryProvider:
    return ShadowMemoryProvider(tmp_path / "shadow_memory.db")


def make_node(content: str = "Hermes phase four memory") -> ShadowMemoryNode:
    return ShadowMemoryNode(
        trace_id="trace",
        session_id="session",
        turn_id="turn",
        kind=MemoryNodeKind.OBSERVATION,
        title="phase four",
        content=content,
        confidence=0.8,
    )


def test_provider_writes_and_gets_node(tmp_path: Path) -> None:
    provider = make_provider(tmp_path)
    written = provider.write(ShadowMemoryWriteRequest(node=make_node()))

    loaded = provider.get(written.node_id)

    assert loaded is not None
    assert loaded.node_id == written.node_id
    assert loaded.content_hash


def test_provider_counts_nodes(tmp_path: Path) -> None:
    provider = make_provider(tmp_path)
    provider.write(ShadowMemoryWriteRequest(node=make_node("one")))
    provider.write(ShadowMemoryWriteRequest(node=make_node("two")))

    assert provider.count_nodes() == 2


def test_provider_quarantines_high_pii(tmp_path: Path) -> None:
    provider = make_provider(tmp_path)
    written = provider.write(
        ShadowMemoryWriteRequest(
            node=make_node("api_key=sk-abcdefghijklmnopqrstuvwxyz123456")
        )
    )

    assert written.status == MemoryNodeStatus.QUARANTINED
    assert written.pii_level == MemoryPIILevel.HIGH


def test_provider_recall_excludes_quarantined_by_default(tmp_path: Path) -> None:
    provider = make_provider(tmp_path)
    provider.write(ShadowMemoryWriteRequest(node=make_node("Hermes stable memory")))
    provider.write(
        ShadowMemoryWriteRequest(
            node=make_node("api_key=sk-abcdefghijklmnopqrstuvwxyz123456 Hermes")
        )
    )

    results = provider.recall(ShadowMemoryQuery(query="Hermes"))

    assert results
    assert all(result.node.status != MemoryNodeStatus.QUARANTINED for result in results)


def test_provider_recall_can_include_quarantined(tmp_path: Path) -> None:
    provider = make_provider(tmp_path)
    provider.write(
        ShadowMemoryWriteRequest(
            node=make_node("api_key=sk-abcdefghijklmnopqrstuvwxyz123456 Hermes")
        )
    )

    results = provider.recall(
        ShadowMemoryQuery(query="Hermes", include_quarantined=True)
    )

    assert results
    assert any(result.node.status == MemoryNodeStatus.QUARANTINED for result in results)