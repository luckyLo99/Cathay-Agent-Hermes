from __future__ import annotations

from typing import Any

from hermes_ext.golden_trace.contracts import sha256_text, stable_json_dumps


class GoldenTraceNormalizer:
    """
    Normalizes volatile shadow outputs into deterministic audit shape.

    UUIDs, timestamps, checkpoint IDs, run IDs, trace IDs and full checkpoint payloads
    are intentionally removed or summarized before hashing.
    """

    VOLATILE_KEYS = {
        "request_id",
        "run_id",
        "session_id",
        "trace_id",
        "turn_id",
        "checkpoint_id",
        "final_checkpoint_id",
        "node_id",
        "edge_id",
        "result_id",
        "report_id",
        "pack_id",
        "case_id",
        "created_at",
        "started_at",
        "ended_at",
        "state_hash",
        "content_hash",
        "spec_id",
        "spec_hash",
        "source_scan_report_id",
    }

    def normalize(self, value: Any) -> Any:
        if isinstance(value, dict):
            return self._normalize_dict(value)

        if isinstance(value, list):
            return [self.normalize(item) for item in value]

        return value

    def canonical_hash(self, value: Any) -> str:
        normalized = self.normalize(value)
        return sha256_text(stable_json_dumps(normalized))

    def _normalize_dict(self, value: dict[str, Any]) -> dict[str, Any]:
        output: dict[str, Any] = {}

        for key, item in sorted(value.items(), key=lambda pair: pair[0]):
            if key in self.VOLATILE_KEYS:
                continue

            if key == "results" and isinstance(item, list):
                output[key] = self._summarize_results(item)
                continue

            if key == "checkpoints" and isinstance(item, list):
                output[key] = self._summarize_checkpoints(item)
                continue

            if key == "normalized_output":
                output[key] = self.normalize(item)
                continue

            output[key] = self.normalize(item)

        return output

    def _summarize_results(self, value: list[Any]) -> dict[str, Any]:
        verdict_counts: dict[str, int] = {}
        for item in value:
            if isinstance(item, dict):
                verdict = str(item.get("verdict", "unknown"))
                verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
        return {
            "count": len(value),
            "verdict_counts": dict(sorted(verdict_counts.items())),
        }

    def _summarize_checkpoints(self, value: list[Any]) -> dict[str, Any]:
        kind_counts: dict[str, int] = {}
        step_counts: dict[str, int] = {}

        for item in value:
            if isinstance(item, dict):
                kind = str(item.get("kind", "unknown"))
                step = str(item.get("step_name", "unknown"))
                kind_counts[kind] = kind_counts.get(kind, 0) + 1
                step_counts[step] = step_counts.get(step, 0) + 1

        return {
            "count": len(value),
            "kind_counts": dict(sorted(kind_counts.items())),
            "step_counts": dict(sorted(step_counts.items())),
        }