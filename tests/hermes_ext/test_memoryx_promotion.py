from __future__ import annotations

from hermes_ext.memoryx.contracts import (
    MemoryNodeKind,
    MemoryNodeStatus,
    MemoryPIILevel,
    ShadowMemoryNode,
)
from hermes_ext.memoryx.promotion import ShadowPromotionPolicy


def make_node(**kwargs) -> ShadowMemoryNode:
    base = {
        "trace_id": "trace",
        "session_id": "session",
        "turn_id": "turn",
        "kind": MemoryNodeKind.OBSERVATION,
        "title": "stable preference",
        "content": "User prioritizes stability",
        "confidence": 0.9,
    }
    base.update(kwargs)
    return ShadowMemoryNode(**base)


def test_promotion_policy_accepts_high_confidence_non_pii_shadow() -> None:
    node = make_node()
    decision = ShadowPromotionPolicy().evaluate(node)

    assert decision.eligible


def test_promotion_policy_rejects_low_confidence() -> None:
    node = make_node(confidence=0.5)
    decision = ShadowPromotionPolicy().evaluate(node)

    assert not decision.eligible


def test_promotion_policy_rejects_medium_pii() -> None:
    node = make_node(pii_level=MemoryPIILevel.MEDIUM)
    decision = ShadowPromotionPolicy().evaluate(node)

    assert not decision.eligible


def test_promotion_policy_marks_candidate_without_writing_hermes_memory() -> None:
    node = make_node()
    marked = ShadowPromotionPolicy().mark_candidate(node)

    assert marked.status == MemoryNodeStatus.PROMOTION_CANDIDATE
    assert marked.metadata["promotion_policy_reason"]