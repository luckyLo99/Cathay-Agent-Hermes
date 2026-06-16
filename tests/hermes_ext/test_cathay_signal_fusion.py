from __future__ import annotations

from hermes_ext.cathay.contracts import (
    CathayAdapterInput,
    CathaySafetySignal,
    CathaySignalBundle,
    CathaySignalSeverity,
    CathaySignalSource,
    CathayTextObservation,
)
from hermes_ext.cathay.signal_fusion import CathaySignalFusion
from hermes_ext.runtime.request_envelope import LLMRequestEnvelope, PromptSegment


def test_signal_fusion_infers_coding_intent() -> None:
    adapter_input = CathayAdapterInput(
        observations=[CathayTextObservation(text="please refactor this GitHub project")]
    )

    text = CathaySignalFusion.joined_observation_text(adapter_input)
    intent = CathaySignalFusion.infer_intent(text, {})

    assert intent.value == "coding"


def test_signal_fusion_attaches_metadata_only() -> None:
    envelope = LLMRequestEnvelope(
        messages=[PromptSegment.from_message("user", "hello", segment_type="conversation")]
    )
    bundle = CathaySignalBundle(
        trace_id=envelope.trace_id,
        session_id=envelope.session_id,
        turn_id=envelope.turn_id,
        safety=[
            CathaySafetySignal(
                source=CathaySignalSource.SAFETY_BRIDGE,
                severity=CathaySignalSeverity.HIGH,
                confidence=0.8,
                reason="review",
                category="prompt_injection",
                requires_human_review=True,
            )
        ],
    ).with_hash()

    updated = CathaySignalFusion.attach_to_envelope(envelope, bundle)

    assert updated.messages == envelope.messages
    assert updated.tools == envelope.tools
    assert updated.provider == envelope.provider
    assert updated.metadata["cathay"]["phase"] == 3
    assert updated.metadata["cathay"]["requires_review"] is True