from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from hermes_ext.finalization.contracts import (
    FinalizationConfig,
    FinalizationEvidence,
    FinalizationEvidenceKind,
)


class FinalizationEvidenceLoader:
    """
    Read-only evidence loader for Phase 12.

    It reads prior reports and manifests only. It never imports Hermes core and never writes.
    """

    EXPECTED_EVIDENCE: tuple[tuple[str, FinalizationEvidenceKind], ...] = (
        ("reports/phase11/shadow_assembly_manifest.json", FinalizationEvidenceKind.MANIFEST),
        ("reports/phase11/release_gate_report.json", FinalizationEvidenceKind.RELEASE_GATE),
        ("reports/phase11/phase11_test_result.md", FinalizationEvidenceKind.TEST_RESULT),
        ("reports/phase11/phase11_exit_checklist.md", FinalizationEvidenceKind.CHECKLIST),
        ("reports/phase11/phase11_execution_log.md", FinalizationEvidenceKind.PHASE_REPORT),
        ("reports/phase10/golden_trace_replay_report.json", FinalizationEvidenceKind.JSON_REPORT),
        ("reports/phase9/native_boundary_contract_report.json", FinalizationEvidenceKind.JSON_REPORT),
    )

    def __init__(self, config: FinalizationConfig) -> None:
        self.config = config

    def load(self) -> list[FinalizationEvidence]:
        return [
            self._load_one(relative_path, kind)
            for relative_path, kind in self.EXPECTED_EVIDENCE
        ]

    def by_path(self, evidence: list[FinalizationEvidence]) -> dict[str, FinalizationEvidence]:
        return {item.relative_path: item for item in evidence}

    def _load_one(self, relative_path: str, kind: FinalizationEvidenceKind) -> FinalizationEvidence:
        path = self.config.project_root / relative_path
        if not path.exists():
            return FinalizationEvidence(
                relative_path=relative_path,
                kind=kind,
                exists=False,
                text_excerpt="",
                json_payload=None,
            )

        content = path.read_bytes()
        text = content.decode("utf-8", errors="replace")
        payload = self._maybe_json(path, text)

        return FinalizationEvidence(
            relative_path=relative_path,
            kind=kind,
            exists=True,
            size_bytes=len(content),
            sha256=hashlib.sha256(content).hexdigest(),
            text_excerpt=self._excerpt(text),
            json_payload=payload,
        )

    @staticmethod
    def _maybe_json(path: Path, text: str) -> dict[str, Any] | None:
        if path.suffix.lower() != ".json":
            return None
        data = json.loads(text)
        if not isinstance(data, dict):
            raise ValueError(f"expected JSON object: {path}")
        return data

    @staticmethod
    def _excerpt(text: str, *, limit: int = 4000) -> str:
        if len(text) <= limit:
            return text
        return text[:limit] + "\n...[truncated]"