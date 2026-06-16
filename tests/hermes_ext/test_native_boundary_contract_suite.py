from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    RiskLevel,
)
from hermes_ext.integration_spec.contracts import (
    DesignMatrixEntry,
    IntegrationAdapterLayer,
    IntegrationDesignMatrix,
    IntegrationMode,
    IntegrationSpecStatus,
    ZeroTouchIntegrationSpec,
)
from hermes_ext.native_boundary.contract_suite import NoopNativeBoundaryContractSuite


def test_synthetic_contract_suite_passes() -> None:
    result = NoopNativeBoundaryContractSuite.synthetic().run()

    assert result.ok
    assert result.case_count >= 7
    assert result.failed == 0
    assert not result.violations


def test_contract_suite_from_phase8_spec_json(tmp_path: Path) -> None:
    spec = ZeroTouchIntegrationSpec(
        project_root=str(tmp_path),
        source_scan_report_id="scan",
        matrix=IntegrationDesignMatrix(
            entries=[
                DesignMatrixEntry(
                    candidate_id="tool",
                    relative_path="agent/tool_executor.py",
                    surface=AdapterSurfaceKind.TOOL_REGISTRY,
                    adapter_layer=IntegrationAdapterLayer.TOOL_SAFETY_BOUNDARY,
                    source_posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
                    source_risk=RiskLevel.HIGH,
                    integration_mode=IntegrationMode.FEATURE_FLAG_SHADOW,
                    status=IntegrationSpecStatus.READY_FOR_SHADOW_HARNESS,
                    rationale="tool shadow only",
                    rollback_strategy="kill switch",
                ).stable_id(),
                DesignMatrixEntry(
                    candidate_id="gateway",
                    relative_path="gateway/session.py",
                    surface=AdapterSurfaceKind.GATEWAY,
                    adapter_layer=IntegrationAdapterLayer.GATEWAY_SIDECAR_BOUNDARY,
                    source_posture=AdapterIntegrationPosture.WRAPPER_ONLY,
                    source_risk=RiskLevel.HIGH,
                    integration_mode=IntegrationMode.SIDE_CAR_OBSERVER,
                    status=IntegrationSpecStatus.READY_FOR_SHADOW_HARNESS,
                    rationale="sidecar only",
                    rollback_strategy="kill switch",
                ).stable_id(),
            ]
        ),
    ).with_hash()

    path = tmp_path / "spec.json"
    path.write_text(json.dumps(spec.model_dump(mode="json")), encoding="utf-8")

    result = NoopNativeBoundaryContractSuite.from_spec_json(path, limit=10).run()

    assert result.ok
    assert result.case_count == 2
    assert result.failed == 0