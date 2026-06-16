from __future__ import annotations

import time
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.runtime.request_envelope import (
    LLMRequestEnvelope,
    LLMResponse,
    LLMUsage,
    PromptSegment,
    ToolPlan,
)


class MockProviderConfig(BaseModel):
    """
    Offline mock provider configuration.

    This adapter must never call a real model provider.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    provider_name: str = "mock"
    model_name: str = "mock-offline-v1"
    mode: Literal["echo", "fixed", "tool_call", "timeout", "error", "loop"] = "echo"
    fixed_response: str = "MOCK_RESPONSE"
    simulated_latency_ms: int = Field(default=0, ge=0, le=1000)
    max_loop_tokens: int = Field(default=32, ge=1, le=512)


class MockProviderAdapter:
    """
    Phase 1 mock provider.

    Guarantees:
    - no network
    - no API key
    - no .env
    - deterministic output
    """

    def __init__(self, config: MockProviderConfig | None = None) -> None:
        self.config = config or MockProviderConfig()

    def generate(self, envelope: LLMRequestEnvelope) -> LLMResponse:
        if self.config.simulated_latency_ms:
            time.sleep(self.config.simulated_latency_ms / 1000)

        started = envelope.prepared().mark_started()

        if self.config.mode == "timeout":
            raise TimeoutError("MockProviderAdapter simulated timeout")

        if self.config.mode == "error":
            raise RuntimeError("MockProviderAdapter simulated provider error")

        if self.config.mode == "fixed":
            content = self.config.fixed_response
            finish_reason: Literal["stop", "tool_calls", "length", "error"] = "stop"
            tool_calls: list[ToolPlan] = []

        elif self.config.mode == "tool_call":
            content = "MOCK_TOOL_CALL_REQUEST"
            finish_reason = "tool_calls"
            tool_calls = [
                ToolPlan(
                    name="mock_tool",
                    arguments={"echo": self._last_user_text(started.messages)},
                    risk="low",
                    requires_approval=False,
                )
            ]

        elif self.config.mode == "loop":
            content = " ".join(["LOOP"] * self.config.max_loop_tokens)
            finish_reason = "length"
            tool_calls = []

        else:
            content = f"MOCK_ECHO: {self._last_user_text(started.messages)}"
            finish_reason = "stop"
            tool_calls = []

        usage = self._estimate_usage(started.messages, content)

        return LLMResponse(
            trace_id=started.trace_id,
            provider=self.config.provider_name,
            model=self.config.model_name,
            content=content,
            tool_calls=tool_calls,
            usage=usage,
            finish_reason=finish_reason,
        )

    @staticmethod
    def _last_user_text(messages: list[PromptSegment]) -> str:
        for message in reversed(messages):
            if message.role == "user":
                return message.content
        if messages:
            return messages[-1].content
        return ""

    @staticmethod
    def _estimate_usage(messages: list[PromptSegment], content: str) -> LLMUsage:
        # Deterministic rough estimator for offline tests only.
        input_tokens = sum(max(1, len(message.content.split())) for message in messages)
        output_tokens = max(1, len(content.split()))
        return LLMUsage.from_counts(input_tokens=input_tokens, output_tokens=output_tokens)