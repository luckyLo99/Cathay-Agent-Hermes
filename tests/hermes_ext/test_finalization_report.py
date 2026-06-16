from __future__ import annotations

import json

from hermes_ext.finalization.contracts import (
    DocumentationPack,
    DocumentationSection,
    FinalizationBundle,
    FinalizationEvidence,
    FinalizationEvidenceKind,
    MergeReadinessReport,
    ReadinessInvariant,
    ReadinessInvariantSeverity,
    ReadinessInvariantStatus,
)
from hermes_ext.finalization.report import FinalizationReporter


def test_finalization_reporter_renders_outputs() -> None:
    pack = DocumentationPack(
        sections=[
            DocumentationSection(title="Rollback Index", body="rollback"),
            DocumentationSection(title="Maintenance Guide", body="maintenance"),
        ],
        evidence_paths=["reports/x.json"],
    ).with_hash()

    invariant = ReadinessInvariant(
        invariant_id="ok",
        status=ReadinessInvariantStatus.PASS,
        severity=ReadinessInvariantSeverity.INFO,
        message="ok",
    )
    readiness = MergeReadinessReport(
        ok=True,
        invariants=[invariant],
        evidence_count=1,
        passed=1,
        warned=0,
        failed=0,
    ).with_hash()

    bundle = FinalizationBundle(
        documentation_pack=pack,
        readiness_report=readiness,
        evidence=[
            FinalizationEvidence(
                relative_path="reports/x.json",
                kind=FinalizationEvidenceKind.JSON_REPORT,
                exists=True,
            )
        ],
    ).with_hash()

    reporter = FinalizationReporter()

    assert "# Final Stabilization Documentation Pack" in reporter.render_documentation_markdown(pack)
    assert "# Merge Readiness Report" in reporter.render_readiness_markdown(readiness)
    assert "# Phase 12 Rollback Index" in reporter.render_rollback_index_markdown(pack)
    assert "# Phase 12 Maintenance Guide" in reporter.render_maintenance_guide_markdown(pack)
    assert json.loads(reporter.render_bundle_json(bundle))["bundle_hash"]