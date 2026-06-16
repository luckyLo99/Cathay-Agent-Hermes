from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from hermes_ext.finalization.contracts import (
    DocumentationPack,
    DocumentationSection,
    FinalizationConfig,
    FinalizationEvidence,
    FinalizationEvidenceKind,
    MergeReadinessReport,
    ReadinessInvariant,
    ReadinessInvariantSeverity,
    ReadinessInvariantStatus,
)


def test_finalization_config_normalizes_paths(tmp_path: Path) -> None:
    config = FinalizationConfig(project_root=tmp_path, output_dir=tmp_path / "out")

    assert config.project_root == tmp_path.resolve()
    assert config.output_dir == (tmp_path / "out").resolve()


def test_evidence_rejects_path_escape() -> None:
    with pytest.raises(ValidationError):
        FinalizationEvidence(
            relative_path="../secret.json",
            kind=FinalizationEvidenceKind.JSON_REPORT,
            exists=True,
        )


def test_documentation_pack_requires_sections() -> None:
    with pytest.raises(ValidationError):
        DocumentationPack(sections=[])


def test_documentation_pack_hash_is_stable() -> None:
    pack = DocumentationPack(
        sections=[DocumentationSection(title="A", body="B")]
    ).with_hash()

    assert pack.pack_hash
    assert pack.with_hash().pack_hash == pack.pack_hash


def test_readiness_report_counts_must_match() -> None:
    invariant = ReadinessInvariant(
        invariant_id="x",
        status=ReadinessInvariantStatus.PASS,
        severity=ReadinessInvariantSeverity.INFO,
        message="ok",
    )

    with pytest.raises(ValidationError):
        MergeReadinessReport(
            ok=True,
            invariants=[invariant],
            evidence_count=1,
            passed=0,
            warned=0,
            failed=0,
        )