from __future__ import annotations

from hermes_ext.golden_trace.normalizer import GoldenTraceNormalizer


def test_normalizer_removes_volatile_keys() -> None:
    value = {
        "run_id": "random",
        "created_at": "now",
        "ok": True,
        "shadow_result": {
            "checkpoint_count": 3,
            "final_checkpoint_id": "random",
        },
    }

    normalized = GoldenTraceNormalizer().normalize(value)

    assert "run_id" not in normalized
    assert "created_at" not in normalized
    assert "final_checkpoint_id" not in normalized["shadow_result"]
    assert normalized["ok"] is True


def test_normalizer_hash_is_stable_for_equivalent_outputs() -> None:
    normalizer = GoldenTraceNormalizer()

    one = {"run_id": "a", "ok": True, "created_at": "1"}
    two = {"run_id": "b", "ok": True, "created_at": "2"}

    assert normalizer.canonical_hash(one) == normalizer.canonical_hash(two)


def test_normalizer_summarizes_native_boundary_results() -> None:
    value = {
        "results": [
            {"result_id": "1", "verdict": "blocked"},
            {"result_id": "2", "verdict": "noop"},
            {"result_id": "3", "verdict": "blocked"},
        ]
    }

    normalized = GoldenTraceNormalizer().normalize(value)

    assert normalized["results"]["count"] == 3
    assert normalized["results"]["verdict_counts"]["blocked"] == 2