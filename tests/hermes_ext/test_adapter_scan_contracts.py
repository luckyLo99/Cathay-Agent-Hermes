from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterScanConfig,
    AdapterScanReport,
    AdapterScanSummary,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
    SourceFileRecord,
)


def test_scan_config_normalizes_project_root(tmp_path: Path) -> None:
    config = AdapterScanConfig(project_root=tmp_path)

    assert config.project_root == tmp_path.resolve()


def test_source_file_record_rejects_empty_path() -> None:
    with pytest.raises(ValidationError):
        SourceFileRecord(
            relative_path="",
            size_bytes=0,
            line_count=0,
            sha256="abc",
        )


def test_candidate_stable_id_is_deterministic() -> None:
    candidate = ExtensionPointCandidate(
        relative_path="cli.py",
        surface=AdapterSurfaceKind.CLI,
        posture=AdapterIntegrationPosture.FORBIDDEN,
        risk=RiskLevel.CRITICAL,
        reason="entrypoint",
        future_adapter_hint="do not patch",
    ).stable_id()

    assert candidate.candidate_id
    assert candidate.stable_id().candidate_id == candidate.candidate_id


def test_report_requires_candidate_count_match() -> None:
    with pytest.raises(ValidationError):
        AdapterScanReport(
            project_root=".",
            summary=AdapterScanSummary(candidates_found=1),
            candidates=[],
        )


def test_contracts_reject_extra_fields(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        AdapterScanConfig(
            project_root=tmp_path,
            unexpected=True,  # type: ignore[call-arg]
        )