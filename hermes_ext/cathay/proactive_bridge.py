from __future__ import annotations

from typing import Any

from hermes_ext.cathay.contracts import (
    CathayProactiveSuggestion,
    CathaySignalSeverity,
    CathaySignalSource,
)


class CathayProactiveBridge:
    """
    Produces non-notifying proactive suggestions.

    Phase 3 does not schedule, send, or persist notifications.
    """

    def extract(self, raw_payload: dict[str, Any], text: str) -> list[CathayProactiveSuggestion]:
        suggestions: list[CathayProactiveSuggestion] = []

        suggestions.extend(self._from_raw_payload(raw_payload))
        suggestions.extend(self._from_text(text))

        return self._dedupe(suggestions)

    def _from_raw_payload(self, raw_payload: dict[str, Any]) -> list[CathayProactiveSuggestion]:
        proactive = raw_payload.get("proactive")
        if not isinstance(proactive, dict):
            return []

        message = str(proactive.get("message", "")).strip()
        if not message:
            return []

        return [
            CathayProactiveSuggestion(
                source=CathaySignalSource.PROACTIVE_BRIDGE,
                severity=CathaySignalSeverity.LOW,
                confidence=float(proactive.get("confidence", 0.6)),
                reason=str(proactive.get("reason", "Cathay proactive suggestion extracted")),
                evidence=[str(item) for item in proactive.get("evidence", []) if isinstance(item, str)],
                suggestion_type=self._coerce_suggestion_type(proactive.get("suggestion_type")),
                message=message,
                allowed_to_notify=False,
                requires_user_consent=True,
                metadata={"from_raw_payload": True},
            )
        ]

    def _from_text(self, text: str) -> list[CathayProactiveSuggestion]:
        output: list[CathayProactiveSuggestion] = []

        if "phase" in text.lower() or "阶段" in text:
            output.append(
                CathayProactiveSuggestion(
                    source=CathaySignalSource.PROACTIVE_BRIDGE,
                    severity=CathaySignalSeverity.INFO,
                    confidence=0.55,
                    reason="Phase-based workflow may benefit from checkpoint reminder",
                    evidence=["phase/阶段"],
                    suggestion_type="task_checkpoint",
                    message="Create a checkpoint report before entering the next phase.",
                    allowed_to_notify=False,
                    requires_user_consent=True,
                )
            )

        if "测试" in text or "pytest" in text.lower():
            output.append(
                CathayProactiveSuggestion(
                    source=CathaySignalSource.PROACTIVE_BRIDGE,
                    severity=CathaySignalSeverity.INFO,
                    confidence=0.55,
                    reason="Testing workflow detected",
                    evidence=["测试/pytest"],
                    suggestion_type="task_checkpoint",
                    message="Run regression tests before merging the current phase.",
                    allowed_to_notify=False,
                    requires_user_consent=True,
                )
            )

        return output

    @staticmethod
    def _coerce_suggestion_type(value: Any) -> str:
        allowed = {
            "none",
            "follow_up_question",
            "learning_review",
            "task_checkpoint",
            "safety_reminder",
            "reflection_prompt",
        }
        normalized = str(value).strip().lower()
        return normalized if normalized in allowed else "none"

    @staticmethod
    def _dedupe(signals: list[CathayProactiveSuggestion]) -> list[CathayProactiveSuggestion]:
        seen: set[str] = set()
        output: list[CathayProactiveSuggestion] = []

        for signal in signals:
            if signal.message in seen:
                continue
            seen.add(signal.message)
            output.append(signal)

        return output