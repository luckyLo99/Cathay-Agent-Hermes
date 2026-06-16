from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from hermes_ext.memoryx.contracts import (
    MemoryNodeStatus,
    MemoryPIILevel,
    ShadowMemoryNode,
)


class PromotionDecision(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    eligible: bool
    reason: str


class ShadowPromotionPolicy:
    """
    Determines whether a shadow node can become a promotion candidate.

    Phase 4 does not promote into Hermes memory. It only labels eligibility.
    """

    def evaluate(self, node: ShadowMemoryNode) -> PromotionDecision:
        if node.status == MemoryNodeStatus.QUARANTINED:
            return PromotionDecision(eligible=False, reason="quarantined nodes are not eligible")

        if node.pii_level in {MemoryPIILevel.MEDIUM, MemoryPIILevel.HIGH}:
            return PromotionDecision(eligible=False, reason="PII-bearing nodes are not eligible")

        if node.confidence < 0.75:
            return PromotionDecision(eligible=False, reason="confidence below 0.75")

        return PromotionDecision(eligible=True, reason="eligible as shadow promotion candidate")

    def mark_candidate(self, node: ShadowMemoryNode) -> ShadowMemoryNode:
        decision = self.evaluate(node)
        if not decision.eligible:
            return node
        return node.model_copy(
            update={
                "status": MemoryNodeStatus.PROMOTION_CANDIDATE,
                "metadata": {
                    **node.metadata,
                    "promotion_policy_reason": decision.reason,
                },
            }
        )