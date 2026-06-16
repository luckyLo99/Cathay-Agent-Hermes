from __future__ import annotations

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
)
from hermes_ext.integration_spec.contracts import IntegrationMode, IntegrationSpecStatus
from hermes_ext.integration_spec.matrix_builder import IntegrationMatrixBuilder


def candidate(
    path: str,
    *,
    posture: AdapterIntegrationPosture,
    surface: AdapterSurfaceKind,
    risk: RiskLevel = RiskLevel.HIGH,
) -> ExtensionPointCandidate:
    return ExtensionPointCandidate(
        candidate_id=path,
        relative_path=path,
        surface=surface,
        posture=posture,
        risk=risk,
        reason="test reason",
        future_adapter_hint="test hint",
    ).stable_id()


def test_matrix_builder_preserves_forbidden_as_blocked() -> None:
    matrix = IntegrationMatrixBuilder().build(
        [
            candidate(
                "cli.py",
                posture=AdapterIntegrationPosture.FORBIDDEN,
                surface=AdapterSurfaceKind.CLI,
                risk=RiskLevel.CRITICAL,
            )
        ]
    )

    assert len(matrix.entries) == 1
    assert matrix.entries[0].integration_mode == IntegrationMode.FORBIDDEN
    assert matrix.entries[0].status == IntegrationSpecStatus.BLOCKED


def test_matrix_builder_maps_tool_to_feature_flag_shadow() -> None:
    matrix = IntegrationMatrixBuilder().build(
        [
            candidate(
                "agent/tool_executor.py",
                posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
                surface=AdapterSurfaceKind.TOOL_REGISTRY,
            )
        ]
    )

    assert matrix.entries[0].integration_mode == IntegrationMode.FEATURE_FLAG_SHADOW
    assert matrix.entries[0].required_flags


def test_matrix_builder_creates_surface_plans() -> None:
    matrix = IntegrationMatrixBuilder().build(
        [
            candidate(
                "agent/tool_executor.py",
                posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
                surface=AdapterSurfaceKind.TOOL_REGISTRY,
            ),
            candidate(
                "agent/memory_shadow.py",
                posture=AdapterIntegrationPosture.WRAPPER_ONLY,
                surface=AdapterSurfaceKind.MEMORY,
                risk=RiskLevel.MEDIUM,
            ),
        ]
    )

    assert len(matrix.surface_plans) == 2
    assert sum(plan.total_entries for plan in matrix.surface_plans) == 2