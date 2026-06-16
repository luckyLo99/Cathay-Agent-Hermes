from __future__ import annotations

import re

from pydantic import BaseModel, ConfigDict

from hermes_ext.memoryx.contracts import MemoryPIILevel


class PIIDetectionResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    level: MemoryPIILevel
    reasons: list[str]


class ShadowPIIFilter:
    """
    Deterministic PII detector for shadow memory.

    It is intentionally conservative:
    - API keys and bearer tokens => HIGH
    - email / phone / id-like strings => MEDIUM
    - no findings => NONE
    """

    _patterns: list[tuple[str, MemoryPIILevel, str]] = [
        (r"sk-[A-Za-z0-9_\-]{16,}", MemoryPIILevel.HIGH, "api_key_like"),
        (r"Bearer\s+[A-Za-z0-9_\-\.]{16,}", MemoryPIILevel.HIGH, "bearer_token_like"),
        (r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*\S+", MemoryPIILevel.HIGH, "secret_assignment"),
        (r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", MemoryPIILevel.MEDIUM, "email"),
        (r"\b(?:\+?\d[\d\-\s]{8,}\d)\b", MemoryPIILevel.MEDIUM, "phone_like"),
        (r"\b\d{15,18}[0-9Xx]\b", MemoryPIILevel.MEDIUM, "id_like"),
    ]

    def detect(self, text: str) -> PIIDetectionResult:
        reasons: list[str] = []
        highest = MemoryPIILevel.NONE

        order = {
            MemoryPIILevel.NONE: 0,
            MemoryPIILevel.LOW: 1,
            MemoryPIILevel.MEDIUM: 2,
            MemoryPIILevel.HIGH: 3,
        }

        for pattern, level, reason in self._patterns:
            if re.search(pattern, text):
                reasons.append(reason)
                if order[level] > order[highest]:
                    highest = level

        return PIIDetectionResult(level=highest, reasons=reasons)

    def redact(self, text: str) -> str:
        redacted = text
        for pattern, _level, reason in self._patterns:
            redacted = re.sub(pattern, f"[REDACTED:{reason}]", redacted)
        return redacted