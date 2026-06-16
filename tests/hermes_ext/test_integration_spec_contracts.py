from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    RiskLevel,
)
from hermes_ext.integration_spec.contracts import (
    DesignMatrixEntry,
    IntegrationAdapterLayer,
    IntegrationMode,
    IntegrationSpecConfig,
    IntegrationSpecStatus,
)


def test_integration_spec_config_normalizes_paths(tmp_path: Path) -> None:
    scan_json = tmp_path / "scan.json"
    scan_json.write_text("{}", encoding="utf-8")

    config = IntegrationSpecConfig(project_root=tmp_path, phase7_scan_json=scan_json)

    assert config.project_root == tmp_path.resolve()
    assert config.phase7_scan_json == scan_json.resolve()


def test_forbidden_entry_must_remain_forbidden() -> None:
    with pytest.raises(ValidationError):
        DesignMatrixEntry(
            candidate_id="candidate",
            relative_path="cli.py",
            surface=AdapterSurfaceKind.CLI,
            adapter_layer=IntegrationAdapterLayer.CLI_BOUNDARY,
            source_posture=AdapterIntegrationPosture.FORBIDDEN,
            source_risk=RiskLevel.CRITICAL,
            integration_mode=IntegrationMode.EXTERNAL_WRAPPER,
            status=IntegrationSpecStatus.READY_FOR_SHADOW_HARNESS,
            rationale="bad",
            rollback_strategy="rollback",
        )


def test_matrix_entry_stable_id_is_deterministic() -> None:
    entry = DesignMatrixEntry(
        candidate_id="candidate",
        relative_path="agent/tool_executor.py",
        surface=AdapterSurfaceKind.TOOL_REGISTRY,
        adapter_layer=IntegrationAdapterLayer.TOOL_SAFETY_BOUNDARY,
        source_posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
        source_risk=RiskLevel.HIGH,
        integration_mode=IntegrationMode.FEATURE_FLAG_SHADOW,
        status=IntegrationSpecStatus.READY_FOR_SHADOW_HARNESS,
        rationale="tool safety",
        rollback_strategy="kill switch",
    ).stable_id()

    assert entry.entry_id
    assert entry.stable_id().entry_id == entry.entry_id


def test_contracts_reject_extra_fields(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        IntegrationSpecConfig(
            project_root=tmp_path,
            phase7_scan_json=tmp_path / "scan.json",
            unexpected=True,  # type: ignore[call-arg]
        )