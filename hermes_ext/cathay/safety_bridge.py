from __future__ import annotations

import re
from typing import Any

from hermes_ext.cathay.contracts import (
    CathaySafetySignal,
    CathaySignalSeverity,
    CathaySignalSource,
)


class CathaySafetyBridge:
    """
    Read-only safety bridge.

    It accepts Cathay-like safety payloads or falls back to deterministic
    text heuristics. It never blocks Hermes directly; it emits signals.
    """

    _prompt_injection_patterns = [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"disregard\s+(all\s+)?previous\s+instructions",
        r"system\s+prompt",
        r"developer\s+message",
        r"reveal\s+.*(secret|token|api\s*key)",
        r"bypass\s+.*(safety|policy|guard)",
    ]

    _crisis_patterns = [
        r"\bkill myself\b",
        r"\bsuicide\b",
        r"\bself[- ]harm\b",
        r"不想活",
        r"自杀",
        r"伤害自己",
    ]

    _dependency_patterns = [
        r"你必须一直陪着我",
        r"不能离开我",
        r"只有你理解我",
        r"without you i can't",
    ]

    def extract(self, raw_payload: dict[str, Any], text: str) -> list[CathaySafetySignal]:
        signals: list[CathaySafetySignal] = []

        signals.extend(self._from_raw_payload(raw_payload))
        signals.extend(self._from_text(text))

        if not signals:
            signals.append(
                CathaySafetySignal(
                    source=CathaySignalSource.SAFETY_BRIDGE,
                    severity=CathaySignalSeverity.INFO,
                    confidence=0.4,
                    reason="No Cathay safety risk detected",
                    category="allow",
                    should_block=False,
                    requires_human_review=False,
                )
            )

        return signals

    def _from_raw_payload(self, raw_payload: dict[str, Any]) -> list[CathaySafetySignal]:
        safety = raw_payload.get("safety")
        if not isinstance(safety, dict):
            return []

        category = str(safety.get("category", "unknown"))
        severity = self._coerce_severity(safety.get("severity"))
        should_block = bool(safety.get("should_block", False))
        requires_review = bool(safety.get("requires_human_review", False))

        if category in {"crisis", "prompt_injection", "privacy"}:
            requires_review = True

        if severity in {CathaySignalSeverity.HIGH, CathaySignalSeverity.CRITICAL}:
            requires_review = True

        reason = str(safety.get("reason", f"Cathay raw safety category: {category}"))

        return [
            CathaySafetySignal(
                source=CathaySignalSource.SAFETY_BRIDGE,
                severity=severity,
                confidence=float(safety.get("confidence", 0.7)),
                reason=reason,
                evidence=[str(item) for item in safety.get("evidence", []) if isinstance(item, str)],
                category=self._coerce_category(category),
                should_block=should_block,
                requires_human_review=requires_review,
                metadata={"from_raw_payload": True},
            )
        ]

    def _from_text(self, text: str) -> list[CathaySafetySignal]:
        lowered = text.lower()
        signals: list[CathaySafetySignal] = []

        for pattern in self._prompt_injection_patterns:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                signals.append(
                    CathaySafetySignal(
                        source=CathaySignalSource.SAFETY_BRIDGE,
                        severity=CathaySignalSeverity.HIGH,
                        confidence=0.75,
                        reason="Prompt injection pattern detected",
                        evidence=[pattern],
                        category="prompt_injection",
                        should_block=False,
                        requires_human_review=True,
                    )
                )
                break

        for pattern in self._crisis_patterns:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                signals.append(
                    CathaySafetySignal(
                        source=CathaySignalSource.SAFETY_BRIDGE,
                        severity=CathaySignalSeverity.CRITICAL,
                        confidence=0.8,
                        reason="Potential crisis/self-harm expression detected",
                        evidence=[pattern],
                        category="crisis",
                        should_block=False,
                        requires_human_review=True,
                    )
                )
                break

        for pattern in self._dependency_patterns:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                signals.append(
                    CathaySafetySignal(
                        source=CathaySignalSource.SAFETY_BRIDGE,
                        severity=CathaySignalSeverity.MEDIUM,
                        confidence=0.65,
                        reason="Potential dependency risk detected",
                        evidence=[pattern],
                        category="dependency",
                        should_block=False,
                        requires_human_review=True,
                    )
                )
                break

        return signals

    @staticmethod
    def _coerce_severity(value: Any) -> CathaySignalSeverity:
        try:
            return CathaySignalSeverity(str(value).lower())
        except ValueError:
            return CathaySignalSeverity.INFO

    @staticmethod
    def _coerce_category(value: str) -> str:
        allowed = {
            "allow",
            "crisis",
            "diagnosis",
            "dependency",
            "prompt_injection",
            "tool_risk",
            "privacy",
            "unknown",
        }
        normalized = value.lower().strip()
        return normalized if normalized in allowed else "unknown"