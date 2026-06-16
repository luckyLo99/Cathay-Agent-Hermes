from __future__ import annotations

from hermes_ext.memoryx.contracts import (
    MemoryNodeKind,
    ShadowMemoryQuery,
    ShadowMemoryRecallResult,
)
from hermes_ext.memoryx.provider import ShadowMemoryProvider


class ShadowRecallService:
    """
    Thin recall facade.

    Keeps provider details out of future orchestration code.
    """

    def __init__(self, provider: ShadowMemoryProvider) -> None:
        self.provider = provider

    def search(
        self,
        text: str,
        *,
        limit: int = 10,
        include_quarantined: bool = False,
        kinds: list[MemoryNodeKind] | None = None,
    ) -> list[ShadowMemoryRecallResult]:
        return self.provider.recall(
            ShadowMemoryQuery(
                query=text,
                limit=limit,
                include_quarantined=include_quarantined,
                kinds=kinds or [],
            )
        )