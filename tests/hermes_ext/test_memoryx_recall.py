from __future__ import annotations

from pathlib import Path

from hermes_ext.memoryx.contracts import MemoryNodeKind, ShadowMemoryNode, ShadowMemoryWriteRequest
from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.memoryx.recall import ShadowRecallService


def test_recall_service_searches_provider(tmp_path: Path) -> None:
    provider = ShadowMemoryProvider(tmp_path / "shadow.db")
    provider.write(
        ShadowMemoryWriteRequest(
            node=ShadowMemoryNode(
                trace_id="trace",
                session_id="session",
                turn_id="turn",
                kind=MemoryNodeKind.LEARNING_SIGNAL,
                title="testing discipline",
                content="pytest regression discipline",
                confidence=0.8,
            )
        )
    )

    results = ShadowRecallService(provider).search("pytest", kinds=[MemoryNodeKind.LEARNING_SIGNAL])

    assert results
    assert results[0].node.kind == MemoryNodeKind.LEARNING_SIGNAL