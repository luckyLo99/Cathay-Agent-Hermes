from __future__ import annotations

from hermes_ext.orchestration.circuit_breaker import CircuitState, ShadowCircuitBreaker


def test_circuit_breaker_starts_closed() -> None:
    breaker = ShadowCircuitBreaker()

    decision = breaker.before_step()

    assert decision.allowed
    assert decision.state == CircuitState.CLOSED


def test_circuit_breaker_opens_after_threshold() -> None:
    breaker = ShadowCircuitBreaker(failure_threshold=2)

    breaker = breaker.record_failure()
    assert breaker.before_step().allowed

    breaker = breaker.record_failure()
    decision = breaker.before_step()

    assert not decision.allowed
    assert decision.state == CircuitState.OPEN


def test_circuit_breaker_resets_on_success() -> None:
    breaker = ShadowCircuitBreaker(failure_threshold=1).record_failure()
    assert not breaker.before_step().allowed

    breaker = breaker.record_success()
    assert breaker.before_step().allowed