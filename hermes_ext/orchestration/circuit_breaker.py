from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class CircuitState(str, Enum):
    CLOSED = "closed"
    OPEN = "open"


class CircuitBreakerDecision(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    allowed: bool
    state: CircuitState
    reason: str


class ShadowCircuitBreaker(BaseModel):
    """
    Minimal circuit breaker for shadow orchestration.

    It blocks repeated failures before they become loops.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    failure_threshold: int = Field(default=3, ge=1, le=20)
    failure_count: int = Field(default=0, ge=0)
    state: CircuitState = CircuitState.CLOSED

    def before_step(self) -> CircuitBreakerDecision:
        if self.state == CircuitState.OPEN:
            return CircuitBreakerDecision(
                allowed=False,
                state=self.state,
                reason="circuit is open",
            )
        return CircuitBreakerDecision(
            allowed=True,
            state=self.state,
            reason="circuit is closed",
        )

    def record_success(self) -> "ShadowCircuitBreaker":
        return self.model_copy(update={"failure_count": 0, "state": CircuitState.CLOSED})

    def record_failure(self) -> "ShadowCircuitBreaker":
        next_count = self.failure_count + 1
        next_state = CircuitState.OPEN if next_count >= self.failure_threshold else CircuitState.CLOSED
        return self.model_copy(update={"failure_count": next_count, "state": next_state})