from __future__ import annotations

from hermes_ext.finalization.contracts import (
    FinalizationEvidence,
    FinalizationEvidenceKind,
)
from hermes_ext.finalization.documentation_pack import FinalDocumentationPackBuilder


def test_documentation_pack_builder_creates_required_sections() -> None:
    evidence = [
        FinalizationEvidence(
            relative_path="reports/phase11/release_gate_report.json",
            kind=FinalizationEvidenceKind.RELEASE_GATE,
            exists=True,
            json_payload={"ok": True},
        ),
        FinalizationEvidence(
            relative_path="reports/phase11/shadow_assembly_manifest.json",
            kind=FinalizationEvidenceKind.MANIFEST,
            exists=True,
            json_payload={"manifest_hash": "abc", "invariants": []},
        ),
        FinalizationEvidence(
            relative_path="reports/phase11/phase11_test_result.md",
            kind=FinalizationEvidenceKind.TEST_RESULT,
            exists=True,
            text_excerpt="总通过 | 241\n失败 | 0\n",
        ),
    ]

    pack = FinalDocumentationPackBuilder().build(evidence)

    titles = {section.title for section in pack.sections}

    assert pack.pack_hash
    assert "Executive Summary" in titles
    assert "Rollback Index" in titles
    assert "Maintenance Guide" in titles