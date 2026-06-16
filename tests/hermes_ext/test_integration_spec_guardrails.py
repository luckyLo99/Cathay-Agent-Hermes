from __future__ import annotations

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
)
from hermes_ext.integration_spec.contracts import IntegrationMode, RequiredFeatureFlag
from hermes_ext.integration_spec.guardrails import IntegrationGuardrailPolicy


def make_candidate(
    *,
    posture: AdapterIntegrationPosture,
    surface: AdapterSurfaceKind,
) -> ExtensionPointCandidate:
    return ExtensionPointCandidate(
        candidate_id="candidate",
        relative_path="agent/tool_executor.py",
        surface=surface,
        posture=posture,
        risk=RiskLevel.HIGH,
        reason="test",
        future_adapter_hint="test",
    )


def test_forbidden_candidate_maps_to_forbidden() -> None:
    candidate = make_candidate(
        posture=AdapterIntegrationPosture.FORBIDDEN,
        surface=AdapterSurfaceKind.CLI,
    )

    mode = IntegrationGuardrailPolicy().mode_for_candidate(candidate)

    assert mode == IntegrationMode.FORBIDDEN


def test_wrapper_gateway_maps_to_sidecar_observer() -> None:
    candidate = make_candidate(
        posture=AdapterIntegrationPosture.WRAPPER_ONLY,
        surface=AdapterSurfaceKind.GATEWAY,
    )

    mode = IntegrationGuardrailPolicy().mode_for_candidate(candidate)

    assert mode == IntegrationMode.SIDE_CAR_OBSERVER


def test_feature_flag_candidate_maps_to_feature_flag_shadow() -> None:
    candidate = make_candidate(
        posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
        surface=AdapterSurfaceKind.TOOL_REGISTRY,
    )

    mode = IntegrationGuardrailPolicy().mode_for_candidate(candidate)

    assert mode == IntegrationMode.FEATURE_FLAG_SHADOW


def test_tool_surface_requires_pretool_flag() -> None:
    flags = IntegrationGuardrailPolicy().flags_for_mode_and_surface(
        IntegrationMode.FEATURE_FLAG_SHADOW,
        AdapterSurfaceKind.TOOL_REGISTRY,
    )

    assert RequiredFeatureFlag.HERMES_EXT_ENABLED in flags
    assert RequiredFeatureFlag.HERMES_EXT_SHADOW_RUNNER in flags
    assert RequiredFeatureFlag.HERMES_EXT_PRETOOL_GUARD in flags


def test_memory_surface_requires_memoryx_flag() -> None:
    flags = IntegrationGuardrailPolicy().flags_for_mode_and_surface(
        IntegrationMode.EXTERNAL_WRAPPER,
        AdapterSurfaceKind.MEMORY,
    )

    assert RequiredFeatureFlag.HERMES_EXT_MEMORYX in flags