"""Read-only Phase 12 evidence loader for Phase 13."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from hermes_ext.human_review.contracts import EvidenceFile, HumanReviewEvidence


class HumanReviewEvidenceLoader:
    """Load Phase 12 evidence without importing Hermes native modules."""

    REQUIRED_EVIDENCE: dict[str, str] = {
        "phase12_merge_readiness_report": "reports/phase12/merge_readiness_report.json",
        "phase12_final_documentation_pack": "reports/phase12/final_documentation_pack.json",
        "phase12_final_stabilization_bundle": "reports/phase12/final_stabilization_bundle.json",
        "phase12_test_result": "reports/phase12/phase12_test_result.md",
        "phase12_exit_checklist": "reports/phase12/phase12_exit_checklist.md",
        "phase12_maintenance_guide": "reports/phase12/maintenance_guide.md",
        "phase12_rollback_index": "reports/phase12/rollback_index.md",
    }

    def __init__(self, project_root: str | Path) -> None:
        self.project_root = Path(project_root).resolve()

    def load(self) -> HumanReviewEvidence:
        required = {
            name: self._load_file(name, relative_path)
            for name, relative_path in self.REQUIRED_EVIDENCE.items()
        }
        return HumanReviewEvidence(
            project_root=str(self.project_root),
            required=required,
        )

    def _load_file(self, name: str, relative_path: str) -> EvidenceFile:
        errors: list[str] = []

        try:
            path = (self.project_root / relative_path).resolve()
            path.relative_to(self.project_root)
        except ValueError:
            return EvidenceFile(
                name=name,
                relative_path=relative_path,
                exists=False,
                errors=("path_escape",),
            )

        if not path.exists():
            return EvidenceFile(
                name=name,
                relative_path=relative_path,
                exists=False,
                errors=("missing",),
            )

        if not path.is_file():
            return EvidenceFile(
                name=name,
                relative_path=relative_path,
                exists=False,
                errors=("not_a_file",),
            )

        raw = path.read_bytes()
        text = raw.decode("utf-8", errors="replace")
        digest = hashlib.sha256(raw).hexdigest()
        json_data: dict[str, Any] | None = None

        if relative_path.endswith(".json"):
            try:
                loaded = json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"json_decode_error:{exc.msg}")
            else:
                if isinstance(loaded, dict):
                    json_data = loaded
                else:
                    errors.append("json_root_not_object")

        return EvidenceFile(
            name=name,
            relative_path=relative_path,
            exists=True,
            sha256=digest,
            size_bytes=len(raw),
            json_data=json_data,
            text_excerpt=text[:4096],
            errors=tuple(errors),
        )


def load_human_review_evidence(project_root: str | Path) -> HumanReviewEvidence:
    return HumanReviewEvidenceLoader(project_root).load()