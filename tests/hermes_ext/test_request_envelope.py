from __future__ import annotations

import pytest
from pydantic import ValidationError

from hermes_ext.runtime.request_envelope import (
    EnvelopeStatus,
    LLMRequestEnvelope,
    LLMResponse,
    PromptSegment,
)


def test_prompt_segment_computes_content_hash() -> None:
    segment = PromptSegment.from_message(
        "user",
        "hello",
        segment_type="conversation",
    )

    assert segment.content_hash
    assert len(segment.content_hash) == 64


def test_envelope_prepared_computes_stable_hash() -> None:
    envelope = LLMRequestEnvelope(
        messages=[
            PromptSegment.from_message("user", "hello", segment_type="conversation"),
        ],
        metadata={"phase": "1"},
    )

    prepared_a = envelope.prepared()
    prepared_b = envelope.prepared()

    assert prepared_a.input_hash
    assert prepared_a.input_hash == prepared_b.input_hash


def test_envelope_lifecycle_completed() -> None:
    envelope = LLMRequestEnvelope(
        messages=[
            PromptSegment.from_message("user", "hello", segment_type="conversation"),
        ]
    ).prepared()

    started = envelope.mark_started()
    response = LLMResponse(
        trace_id=started.trace_id,
        provider="mock",
        model="mock-offline-v1",
        content="ok",
    )
    completed = started.mark_completed(response)

    assert started.status == EnvelopeStatus.STARTED
    assert completed.status == EnvelopeStatus.COMPLETED
    assert completed.output_hash
    assert completed.error is None


def test_envelope_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        LLMRequestEnvelope(
            messages=[],
            unexpected=True,  # type: ignore[call-arg]
        )


def test_envelope_rejects_wrong_strict_type() -> None:
    with pytest.raises(ValidationError):
        LLMRequestEnvelope(
            trace_id=123,  # type: ignore[arg-type]
            messages=[],
        )