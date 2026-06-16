from __future__ import annotations

from hermes_ext.cathay.contracts import (
    CathayLearningSignal,
    CathayProfileHypothesis,
    CathayProactiveSuggestion,
    CathaySafetySignal,
    CathaySignalBundle,
)
from hermes_ext.memoryx.contracts import (
    MemoryNodeKind,
    MemoryNodeStatus,
    ShadowMemoryNode,
    ShadowMemoryWriteRequest,
)
from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.runtime.request_envelope import LLMRequestEnvelope


class ShadowMemoryFusion:
    """
    Converts advisory signals into shadow memory nodes.

    It does not write Hermes native memory.
    """

    def __init__(self, provider: ShadowMemoryProvider) -> None:
        self.provider = provider

    def write_bundle(self, bundle: CathaySignalBundle) -> list[ShadowMemoryNode]:
        nodes: list[ShadowMemoryNode] = []

        for signal in bundle.safety:
            nodes.append(self._write_safety(bundle, signal))

        for signal in bundle.profile:
            nodes.append(self._write_profile(bundle, signal))

        for signal in bundle.learning:
            nodes.append(self._write_learning(bundle, signal))

        for signal in bundle.proactive:
            nodes.append(self._write_proactive(bundle, signal))

        return nodes

    def write_envelope_metadata(self, envelope: LLMRequestEnvelope) -> ShadowMemoryNode:
        node = ShadowMemoryNode(
            trace_id=envelope.trace_id,
            session_id=envelope.session_id,
            turn_id=envelope.turn_id,
            kind=MemoryNodeKind.ENVELOPE_METADATA,
            status=MemoryNodeStatus.SHADOW,
            title="Envelope metadata snapshot",
            content=envelope.model_dump_json(),
            source="llm_request_envelope",
            confidence=0.5,
            metadata={"phase": 4, "shadow_only": True},
        )
        return self.provider.write(ShadowMemoryWriteRequest(node=node))

    def _write_safety(self, bundle: CathaySignalBundle, signal: CathaySafetySignal) -> ShadowMemoryNode:
        node = ShadowMemoryNode(
            trace_id=bundle.trace_id,
            session_id=bundle.session_id,
            turn_id=bundle.turn_id,
            kind=MemoryNodeKind.SAFETY_SIGNAL,
            status=MemoryNodeStatus.SHADOW,
            title=f"Safety signal: {signal.category}",
            content=signal.reason,
            source=signal.source.value,
            confidence=signal.confidence,
            metadata={
                "severity": signal.severity.value,
                "category": signal.category,
                "requires_human_review": signal.requires_human_review,
                "should_block": signal.should_block,
                "shadow_only": True,
            },
        )
        return self.provider.write(ShadowMemoryWriteRequest(node=node))

    def _write_profile(self, bundle: CathaySignalBundle, signal: CathayProfileHypothesis) -> ShadowMemoryNode:
        status = MemoryNodeStatus.QUARANTINED if signal.is_sensitive else MemoryNodeStatus.SHADOW
        node = ShadowMemoryNode(
            trace_id=bundle.trace_id,
            session_id=bundle.session_id,
            turn_id=bundle.turn_id,
            kind=MemoryNodeKind.PROFILE_HYPOTHESIS,
            status=status,
            title=f"Profile hypothesis: {signal.key}",
            content=f"{signal.key}: {signal.value}",
            source=signal.source.value,
            confidence=signal.confidence,
            metadata={
                "hypothesis_type": signal.hypothesis_type,
                "is_sensitive": signal.is_sensitive,
                "write_permission": signal.write_permission,
                "shadow_only": True,
            },
        )
        return self.provider.write(ShadowMemoryWriteRequest(node=node))

    def _write_learning(self, bundle: CathaySignalBundle, signal: CathayLearningSignal) -> ShadowMemoryNode:
        node = ShadowMemoryNode(
            trace_id=bundle.trace_id,
            session_id=bundle.session_id,
            turn_id=bundle.turn_id,
            kind=MemoryNodeKind.LEARNING_SIGNAL,
            status=MemoryNodeStatus.SHADOW,
            title=f"Learning signal: {signal.skill_area}",
            content=f"{signal.skill_area}: {signal.reason}",
            source=signal.source.value,
            confidence=signal.confidence,
            metadata={
                "learner_state": signal.learner_state,
                "suggested_method": signal.suggested_method,
                "should_create_skill": signal.should_create_skill,
                "skill_write_permission": signal.skill_write_permission,
                "shadow_only": True,
            },
        )
        return self.provider.write(ShadowMemoryWriteRequest(node=node))

    def _write_proactive(self, bundle: CathaySignalBundle, signal: CathayProactiveSuggestion) -> ShadowMemoryNode:
        node = ShadowMemoryNode(
            trace_id=bundle.trace_id,
            session_id=bundle.session_id,
            turn_id=bundle.turn_id,
            kind=MemoryNodeKind.PROACTIVE_SUGGESTION,
            status=MemoryNodeStatus.SHADOW,
            title=f"Proactive suggestion: {signal.suggestion_type}",
            content=signal.message,
            source=signal.source.value,
            confidence=signal.confidence,
            metadata={
                "allowed_to_notify": signal.allowed_to_notify,
                "requires_user_consent": signal.requires_user_consent,
                "shadow_only": True,
            },
        )
        return self.provider.write(ShadowMemoryWriteRequest(node=node))