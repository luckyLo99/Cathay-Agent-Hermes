from __future__ import annotations

import re
from typing import Any

from hermes_ext.cathay.contracts import (
    CathayProfileHypothesis,
    CathaySignalSeverity,
    CathaySignalSource,
)


class CathayProfileBridge:
    """
    Converts Cathay-like profile data into read-only hypotheses.

    Phase 3 never writes profile hypotheses to Hermes memory.
    """

    _sensitive_keys = {
        "email",
        "phone",
        "address",
        "id",
        "passport",
        "api_key",
        "token",
        "password",
        "secret",
        "身份证",
        "手机号",
        "住址",
        "邮箱",
    }

    _coding_patterns = [
        (r"\btrae\b", "working_context", "Uses Trae IDE"),
        (r"\bdeepseek\b", "working_context", "Uses DeepSeek model"),
        (r"\bhermes\b", "goal", "Working on Hermes Agent refactor"),
        (r"\bcathay\b", "goal", "Interested in Cathay-style cognitive agent features"),
        (r"\bmemoryx\b", "goal", "Interested in memoryx integration"),
    ]

    def extract(self, raw_payload: dict[str, Any], text: str) -> list[CathayProfileHypothesis]:
        signals: list[CathayProfileHypothesis] = []
        signals.extend(self._from_raw_payload(raw_payload))
        signals.extend(self._from_text(text))
        return self._dedupe(signals)

    def _from_raw_payload(self, raw_payload: dict[str, Any]) -> list[CathayProfileHypothesis]:
        profile = raw_payload.get("profile")
        if not isinstance(profile, dict):
            return []

        output: list[CathayProfileHypothesis] = []

        for key, value in profile.items():
            key_text = str(key).strip()
            value_text = str(value).strip()

            if not key_text or not value_text:
                continue

            sensitive = self._is_sensitive(key_text) or self._looks_like_secret(value_text)
            output.append(
                CathayProfileHypothesis(
                    source=CathaySignalSource.PROFILE_BRIDGE,
                    severity=CathaySignalSeverity.LOW if not sensitive else CathaySignalSeverity.MEDIUM,
                    confidence=0.65,
                    reason=f"Profile hypothesis extracted from Cathay raw payload: {key_text}",
                    evidence=[key_text],
                    key=key_text,
                    value=value_text,
                    hypothesis_type=self._infer_hypothesis_type(key_text),
                    is_sensitive=sensitive,
                    write_permission="forbidden" if sensitive else "requires_review",
                    metadata={"from_raw_payload": True},
                )
            )

        return output

    def _from_text(self, text: str) -> list[CathayProfileHypothesis]:
        output: list[CathayProfileHypothesis] = []
        lowered = text.lower()

        for pattern, hypothesis_type, value in self._coding_patterns:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                # Coerce hypothesis_type to Literal type
                valid_types = {"preference", "skill_level", "communication_style", "goal", "constraint", "working_context", "unknown"}
                htype = hypothesis_type if hypothesis_type in valid_types else "unknown"
                output.append(
                    CathayProfileHypothesis(
                        source=CathaySignalSource.PROFILE_BRIDGE,
                        severity=CathaySignalSeverity.LOW,
                        confidence=0.6,
                        reason=f"Profile hypothesis inferred from text pattern: {pattern}",
                        evidence=[pattern],
                        key=hypothesis_type,
                        value=value,
                        hypothesis_type=htype,  # type: ignore[arg-type]
                        is_sensitive=False,
                        write_permission="requires_review",
                    )
                )

        if "稳定" in text or "stable" in lowered:
            output.append(
                CathayProfileHypothesis(
                    source=CathaySignalSource.PROFILE_BRIDGE,
                    severity=CathaySignalSeverity.LOW,
                    confidence=0.7,
                    reason="User repeatedly emphasizes stability",
                    evidence=["稳定/stable"],
                    key="preference",
                    value="Prioritizes stability and operational safety",
                    hypothesis_type="preference",
                    is_sensitive=False,
                    write_permission="requires_review",
                )
            )

        return output

    def _dedupe(self, signals: list[CathayProfileHypothesis]) -> list[CathayProfileHypothesis]:
        seen: set[tuple[str, str, str]] = set()
        output: list[CathayProfileHypothesis] = []

        for signal in signals:
            key = (signal.key, signal.value, signal.hypothesis_type)
            if key in seen:
                continue
            seen.add(key)
            output.append(signal)

        return output

    def _is_sensitive(self, key: str) -> bool:
        lowered = key.lower()
        return any(item in lowered for item in self._sensitive_keys)

    @staticmethod
    def _looks_like_secret(value: str) -> bool:
        lowered = value.lower()
        if "sk-" in lowered:
            return True
        if "bearer " in lowered:
            return True
        if len(value) >= 32 and re.search(r"[A-Za-z0-9_\-]{32,}", value):
            return True
        return False

    @staticmethod
    def _infer_hypothesis_type(key: str) -> str:
        lowered = key.lower()
        if "goal" in lowered or "目标" in lowered:
            return "goal"
        if "style" in lowered or "沟通" in lowered:
            return "communication_style"
        if "skill" in lowered or "level" in lowered or "能力" in lowered:
            return "skill_level"
        if "constraint" in lowered or "限制" in lowered:
            return "constraint"
        if "preference" in lowered or "偏好" in lowered:
            return "preference"
        return "unknown"