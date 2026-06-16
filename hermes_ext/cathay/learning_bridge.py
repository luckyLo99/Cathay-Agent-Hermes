from __future__ import annotations

import re
from typing import Any

from hermes_ext.cathay.contracts import (
    CathayLearningSignal,
    CathaySignalSeverity,
    CathaySignalSource,
)


class CathayLearningBridge:
    """
    Converts Cathay-style learning outcomes into advisory learning signals.

    It must not create Hermes skills directly.
    """

    _skill_patterns = [
        (r"\barchitecture\b|架构", "software architecture"),
        (r"\brefactor\b|重构", "safe refactoring"),
        (r"\bpytest\b|测试", "testing discipline"),
        (r"\bsecurity\b|安全", "agent safety"),
        (r"\bmemory\b|记忆", "agent memory systems"),
        (r"\bhook\b|钩子", "agent hook lifecycle"),
    ]

    def extract(self, raw_payload: dict[str, Any], text: str) -> list[CathayLearningSignal]:
        signals: list[CathayLearningSignal] = []
        signals.extend(self._from_raw_payload(raw_payload))
        signals.extend(self._from_text(text))
        return self._dedupe(signals)

    def _from_raw_payload(self, raw_payload: dict[str, Any]) -> list[CathayLearningSignal]:
        learning = raw_payload.get("learning")
        if not isinstance(learning, dict):
            return []

        skill_area = str(learning.get("skill_area", "unknown")).strip()
        if not skill_area:
            skill_area = "unknown"

        return [
            CathayLearningSignal(
                source=CathaySignalSource.LEARNING_BRIDGE,
                severity=CathaySignalSeverity.LOW,
                confidence=float(learning.get("confidence", 0.65)),
                reason=str(learning.get("reason", f"Learning signal extracted for {skill_area}")),
                evidence=[str(item) for item in learning.get("evidence", []) if isinstance(item, str)],
                skill_area=skill_area,
                learner_state=self._coerce_learner_state(learning.get("learner_state")),
                suggested_method=self._coerce_method(learning.get("suggested_method")),
                should_create_skill=bool(learning.get("should_create_skill", False)),
                skill_write_permission="requires_review",
                metadata={"from_raw_payload": True},
            )
        ]

    def _from_text(self, text: str) -> list[CathayLearningSignal]:
        lowered = text.lower()
        output: list[CathayLearningSignal] = []

        for pattern, skill_area in self._skill_patterns:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                output.append(
                    CathayLearningSignal(
                        source=CathaySignalSource.LEARNING_BRIDGE,
                        severity=CathaySignalSeverity.LOW,
                        confidence=0.6,
                        reason=f"Learning area inferred from text: {skill_area}",
                        evidence=[pattern],
                        skill_area=skill_area,
                        learner_state="practicing",
                        suggested_method="project_based",
                        should_create_skill=False,
                        skill_write_permission="requires_review",
                    )
                )

        if "一次性执行" in text or "完整详细" in text:
            output.append(
                CathayLearningSignal(
                    source=CathaySignalSource.LEARNING_BRIDGE,
                    severity=CathaySignalSeverity.LOW,
                    confidence=0.7,
                    reason="User wants executable, complete implementation plans",
                    evidence=["一次性执行/完整详细"],
                    skill_area="execution-grade software planning",
                    learner_state="ready_for_challenge",
                    suggested_method="worked_example",
                    should_create_skill=False,
                    skill_write_permission="requires_review",
                )
            )

        return output

    @staticmethod
    def _coerce_learner_state(value: Any) -> str:
        allowed = {
            "unknown",
            "novice",
            "practicing",
            "blocked",
            "ready_for_challenge",
            "mastery_candidate",
        }
        normalized = str(value).strip().lower()
        return normalized if normalized in allowed else "unknown"

    @staticmethod
    def _coerce_method(value: Any) -> str:
        allowed = {
            "none",
            "socratic_question",
            "retrieval_practice",
            "worked_example",
            "spaced_repetition",
            "project_based",
        }
        normalized = str(value).strip().lower()
        return normalized if normalized in allowed else "none"

    @staticmethod
    def _dedupe(signals: list[CathayLearningSignal]) -> list[CathayLearningSignal]:
        seen: set[str] = set()
        output: list[CathayLearningSignal] = []

        for signal in signals:
            if signal.skill_area in seen:
                continue
            seen.add(signal.skill_area)
            output.append(signal)

        return output