from __future__ import annotations

from hermes_ext.cathay.proactive_bridge import CathayProactiveBridge


def test_proactive_bridge_extracts_raw_suggestion_but_never_notifies() -> None:
    signals = CathayProactiveBridge().extract(
        {
            "proactive": {
                "suggestion_type": "task_checkpoint",
                "message": "checkpoint before next phase",
                "confidence": 0.8,
            }
        },
        "",
    )

    assert len(signals) == 1
    assert signals[0].message == "checkpoint before next phase"
    assert not signals[0].allowed_to_notify
    assert signals[0].requires_user_consent


def test_proactive_bridge_infers_phase_checkpoint() -> None:
    signals = CathayProactiveBridge().extract({}, "进入 Phase 3 阶段")

    assert any(signal.suggestion_type == "task_checkpoint" for signal in signals)
    assert all(not signal.allowed_to_notify for signal in signals)


def test_proactive_bridge_infers_test_checkpoint() -> None:
    signals = CathayProactiveBridge().extract({}, "运行 pytest 测试")

    assert any("regression tests" in signal.message for signal in signals)