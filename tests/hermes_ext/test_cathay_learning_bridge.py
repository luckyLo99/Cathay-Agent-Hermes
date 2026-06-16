from __future__ import annotations

from hermes_ext.cathay.learning_bridge import CathayLearningBridge


def test_learning_bridge_extracts_raw_learning_signal() -> None:
    signals = CathayLearningBridge().extract(
        {
            "learning": {
                "skill_area": "architecture",
                "learner_state": "practicing",
                "suggested_method": "worked_example",
                "confidence": 0.8,
            }
        },
        "",
    )

    assert len(signals) == 1
    assert signals[0].skill_area == "architecture"
    assert signals[0].skill_write_permission == "requires_review"


def test_learning_bridge_infers_refactor_and_testing() -> None:
    signals = CathayLearningBridge().extract(
        {},
        "我们要做架构重构，并用 pytest 测试。",
    )

    areas = {signal.skill_area for signal in signals}
    assert "software architecture" in areas
    assert "safe refactoring" in areas
    assert "testing discipline" in areas


def test_learning_bridge_infers_execution_grade_planning() -> None:
    signals = CathayLearningBridge().extract(
        {},
        "给我一次性执行到位的完整详细方案。",
    )

    assert any(signal.skill_area == "execution-grade software planning" for signal in signals)