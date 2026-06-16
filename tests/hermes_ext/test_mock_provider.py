from __future__ import annotations

import pytest

from hermes_ext.runtime.mock_provider import MockProviderAdapter, MockProviderConfig
from hermes_ext.runtime.request_envelope import LLMRequestEnvelope, PromptSegment


def make_envelope(text: str = "hello") -> LLMRequestEnvelope:
    return LLMRequestEnvelope(
        messages=[
            PromptSegment.from_message("user", text, segment_type="conversation"),
        ]
    )


def test_mock_provider_echo_mode_is_deterministic() -> None:
    adapter = MockProviderAdapter()
    envelope = make_envelope("build the mock runtime")

    response_a = adapter.generate(envelope)
    response_b = adapter.generate(envelope)

    assert response_a.content == "MOCK_ECHO: build the mock runtime"
    assert response_b.content == response_a.content
    assert response_a.provider == "mock"
    assert response_a.model == "mock-offline-v1"
    assert response_a.usage.total_tokens > 0


def test_mock_provider_fixed_mode() -> None:
    adapter = MockProviderAdapter(
        MockProviderConfig(mode="fixed", fixed_response="STATIC_RESULT")
    )

    response = adapter.generate(make_envelope())

    assert response.content == "STATIC_RESULT"
    assert response.finish_reason == "stop"


def test_mock_provider_tool_call_mode() -> None:
    adapter = MockProviderAdapter(MockProviderConfig(mode="tool_call"))

    response = adapter.generate(make_envelope("call a tool"))

    assert response.finish_reason == "tool_calls"
    assert len(response.tool_calls) == 1
    assert response.tool_calls[0].name == "mock_tool"
    assert response.tool_calls[0].arguments == {"echo": "call a tool"}


def test_mock_provider_loop_mode() -> None:
    adapter = MockProviderAdapter(
        MockProviderConfig(mode="loop", max_loop_tokens=8)
    )

    response = adapter.generate(make_envelope())

    assert response.finish_reason == "length"
    assert response.content == " ".join(["LOOP"] * 8)


def test_mock_provider_error_mode() -> None:
    adapter = MockProviderAdapter(MockProviderConfig(mode="error"))

    with pytest.raises(RuntimeError):
        adapter.generate(make_envelope())


def test_mock_provider_timeout_mode() -> None:
    adapter = MockProviderAdapter(MockProviderConfig(mode="timeout"))

    with pytest.raises(TimeoutError):
        adapter.generate(make_envelope())