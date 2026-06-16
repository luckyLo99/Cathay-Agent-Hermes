from __future__ import annotations

from hermes_ext.security.decisions import SecurityDecisionType
from hermes_ext.security.url_guard import URLGuard


def test_url_guard_allows_https_public_host() -> None:
    decision = URLGuard().evaluate("https://example.com/docs")

    assert decision.decision == SecurityDecisionType.ALLOW


def test_url_guard_asks_for_http() -> None:
    decision = URLGuard().evaluate("http://example.com")

    assert decision.decision == SecurityDecisionType.ASK


def test_url_guard_denies_file_scheme() -> None:
    decision = URLGuard().evaluate("file:///etc/passwd")

    assert decision.decision == SecurityDecisionType.DENY


def test_url_guard_denies_localhost() -> None:
    decision = URLGuard().evaluate("https://localhost/admin")

    assert decision.decision == SecurityDecisionType.DENY


def test_url_guard_denies_private_ip() -> None:
    decision = URLGuard().evaluate("https://127.0.0.1/status")

    assert decision.decision == SecurityDecisionType.DENY