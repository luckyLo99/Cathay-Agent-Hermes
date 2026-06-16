from __future__ import annotations

import pytest
from pydantic import ValidationError

from hermes_ext.cathay.contracts import (
    CathayAdapterInput,
    CathayProfileHypothesis,
    CathayProactiveSuggestion,
    CathaySafetySignal,
    CathaySignalBundle,
    CathaySignalSeverity,
    CathaySignalSource,
    CathayTextObservation,
)


def test_text_observation_hash_is_stable() -> None:
    obs = CathayTextObservation(text="hello").with_hash()

    assert obs.content_hash
    assert len(obs.content_hash) == 64
    assert obs.with_hash().content_hash == obs.content_hash


def test_adapter_input_prepared_hashes_observations() -> None:
    adapter_input = CathayAdapterInput(
        observations=[CathayTextObservation(text="phase 3")]
    )

    prepared = adapter_input.prepared()

    assert prepared.observations[0].content_hash


def test_safety_high_requires_review_or_block() -> None:
    with pytest.raises(ValidationError):
        CathaySafetySignal(
            source=CathaySignalSource.SAFETY_BRIDGE,
            severity=CathaySignalSeverity.HIGH,
            confidence=0.8,
            reason="high risk",
            category="prompt_injection",
            should_block=False,
            requires_human_review=False,
        )


def test_sensitive_profile_must_be_write_forbidden() -> None:
    with pytest.raises(ValidationError):
        CathayProfileHypothesis(
            source=CathaySignalSource.PROFILE_BRIDGE,
            severity=CathaySignalSeverity.MEDIUM,
            confidence=0.7,
            reason="sensitive",
            key="email",
            value="user@example.com",
            hypothesis_type="working_context",
            is_sensitive=True,
            write_permission="requires_review",
        )


def test_proactive_suggestion_cannot_notify_in_phase3() -> None:
    with pytest.raises(ValidationError):
        CathayProactiveSuggestion(
            source=CathaySignalSource.PROACTIVE_BRIDGE,
            severity=CathaySignalSeverity.INFO,
            confidence=0.5,
            reason="notify",
            suggestion_type="task_checkpoint",
            message="hello",
            allowed_to_notify=True,
            requires_user_consent=True,
        )


def test_signal_bundle_hash_and_review() -> None:
    bundle = CathaySignalBundle(
        trace_id="t",
        session_id="s",
        turn_id="u",
        safety=[
            CathaySafetySignal(
                source=CathaySignalSource.SAFETY_BRIDGE,
                severity=CathaySignalSeverity.HIGH,
                confidence=0.7,
                reason="prompt injection",
                category="prompt_injection",
                should_block=False,
                requires_human_review=True,
            )
        ],
    ).with_hash()

    assert bundle.bundle_hash
    assert bundle.requires_review()
    assert not bundle.has_blocking_safety()


def test_contracts_reject_extra_fields() -> None:
    with pytest.raises(ValidationError):
        CathayAdapterInput(
            observations=[],
            unexpected=True,  # type: ignore[call-arg]
        )