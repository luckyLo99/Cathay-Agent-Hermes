from __future__ import annotations

from hermes_ext.cathay.profile_bridge import CathayProfileBridge


def test_profile_bridge_extracts_raw_profile() -> None:
    signals = CathayProfileBridge().extract(
        {"profile": {"goal": "refactor Hermes safely"}},
        "",
    )

    assert len(signals) == 1
    assert signals[0].key == "goal"
    assert signals[0].write_permission == "requires_review"


def test_profile_bridge_marks_secret_as_sensitive() -> None:
    signals = CathayProfileBridge().extract(
        {"profile": {"api_key": "sk-abcdefghijklmnopqrstuvwxyz123456"}},
        "",
    )

    assert len(signals) == 1
    assert signals[0].is_sensitive
    assert signals[0].write_permission == "forbidden"


def test_profile_bridge_infers_trae_deepseek_context() -> None:
    signals = CathayProfileBridge().extract(
        {},
        "I use Trae IDE with DeepSeek for Hermes refactor.",
    )

    values = {signal.value for signal in signals}
    assert "Uses Trae IDE" in values
    assert "Uses DeepSeek model" in values
    assert "Working on Hermes Agent refactor" in values


def test_profile_bridge_infers_stability_preference() -> None:
    signals = CathayProfileBridge().extract({}, "稳定性第一，stable first")

    assert any("Prioritizes stability" in signal.value for signal in signals)