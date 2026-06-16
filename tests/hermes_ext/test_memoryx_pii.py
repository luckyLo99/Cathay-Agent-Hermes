from __future__ import annotations

from hermes_ext.memoryx.contracts import MemoryPIILevel
from hermes_ext.memoryx.pii import ShadowPIIFilter


def test_pii_filter_detects_api_key() -> None:
    result = ShadowPIIFilter().detect("api_key=sk-abcdefghijklmnopqrstuvwxyz123456")

    assert result.level == MemoryPIILevel.HIGH
    assert "api_key_like" in result.reasons or "secret_assignment" in result.reasons


def test_pii_filter_detects_email() -> None:
    result = ShadowPIIFilter().detect("email me at user@example.com")

    assert result.level == MemoryPIILevel.MEDIUM
    assert "email" in result.reasons


def test_pii_filter_redacts() -> None:
    redacted = ShadowPIIFilter().redact("token=abcdef1234567890abcdef1234567890")

    assert "[REDACTED:" in redacted


def test_pii_filter_none() -> None:
    result = ShadowPIIFilter().detect("Hermes refactor phase 4")

    assert result.level == MemoryPIILevel.NONE