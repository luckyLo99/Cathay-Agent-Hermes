from __future__ import annotations

from collections import defaultdict

from hermes_ext.adapter_scan.contracts import (
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
)
from hermes_ext.integration_spec.contracts import (
    DesignMatrixEntry,
    IntegrationDesignMatrix,
    IntegrationMode,
    IntegrationSurfacePlan,
)
from hermes_ext.integration_spec.guardrails import IntegrationGuardrailPolicy


class IntegrationMatrixBuilder:
    """
    Builds the zero-touch design matrix from Phase 7 candidates.
    """

    def __init__(self, policy: IntegrationGuardrailPolicy | None = None) -> None:
        self.policy = policy or IntegrationGuardrailPolicy()

    def build(self, candidates: list[ExtensionPointCandidate]) -> IntegrationDesignMatrix:
        entries = [self._entry_for_candidate(candidate) for candidate in candidates]
        entries = [entry.stable_id() for entry in entries]
        entries = sorted(
            entries,
            key=lambda item: (
                item.relative_path,
                item.surface.value,
                item.line,
                item.symbol or "",
                item.integration_mode.value,
            ),
        )
        return IntegrationDesignMatrix(
            entries=entries,
            surface_plans=self._surface_plans(entries),
        )

    def _entry_for_candidate(self, candidate: ExtensionPointCandidate) -> DesignMatrixEntry:
        mode = self.policy.mode_for_candidate(candidate)
        status = self.policy.status_for_mode(mode)

        return DesignMatrixEntry(
            candidate_id=candidate.candidate_id,
            relative_path=candidate.relative_path,
            symbol=candidate.symbol,
            line=candidate.line,
            surface=candidate.surface,
            adapter_layer=self.policy.adapter_layer_for_surface(candidate.surface),
            source_posture=candidate.posture,
            source_risk=candidate.risk,
            integration_mode=mode,
            status=status,
            rationale=self.policy.rationale_for_candidate(candidate, mode),
            required_flags=self.policy.flags_for_mode_and_surface(mode, candidate.surface),
            constraints=self.policy.constraints_for_candidate(candidate, mode),
            required_tests=self.policy.required_tests_for_candidate(candidate, mode),
            rollback_strategy=self.policy.rollback_strategy_for_mode(mode),
            next_phase_allowed_work="phase9_shadow_adapter_contract_only",
            metadata={
                "phase7_reason": candidate.reason,
                "phase7_hint": candidate.future_adapter_hint,
                "phase7_allowed_next_phase": candidate.allowed_next_phase,
                **candidate.metadata,
            },
        )

    def _surface_plans(self, entries: list[DesignMatrixEntry]) -> list[IntegrationSurfacePlan]:
        grouped: dict[AdapterSurfaceKind, list[DesignMatrixEntry]] = defaultdict(list)
        for entry in entries:
            grouped[entry.surface].append(entry)

        plans: list[IntegrationSurfacePlan] = []
        for surface, surface_entries in grouped.items():
            plans.append(
                IntegrationSurfacePlan(
                    surface=surface,
                    total_entries=len(surface_entries),
                    forbidden=sum(1 for item in surface_entries if item.integration_mode == IntegrationMode.FORBIDDEN),
                    external_wrapper=sum(1 for item in surface_entries if item.integration_mode == IntegrationMode.EXTERNAL_WRAPPER),
                    feature_flag_shadow=sum(1 for item in surface_entries if item.integration_mode == IntegrationMode.FEATURE_FLAG_SHADOW),
                    sidecar_observer=sum(1 for item in surface_entries if item.integration_mode == IntegrationMode.SIDE_CAR_OBSERVER),
                    no_touch=sum(1 for item in surface_entries if item.integration_mode == IntegrationMode.NO_TOUCH),
                    highest_risk=self._highest_risk(surface_entries),
                    recommendation=self._recommendation(surface, surface_entries),
                )
            )

        return sorted(plans, key=lambda item: item.surface.value)

    @staticmethod
    def _highest_risk(entries: list[DesignMatrixEntry]) -> RiskLevel:
        order = {
            RiskLevel.LOW: 0,
            RiskLevel.MEDIUM: 1,
            RiskLevel.HIGH: 2,
            RiskLevel.CRITICAL: 3,
        }
        return max((entry.source_risk for entry in entries), key=lambda item: order[item])

    @staticmethod
    def _recommendation(surface: AdapterSurfaceKind, entries: list[DesignMatrixEntry]) -> str:
        if any(entry.integration_mode == IntegrationMode.FORBIDDEN for entry in entries):
            return "Contains forbidden lifeline boundaries. Keep design-only until explicit later approval."

        if surface in {
            AdapterSurfaceKind.TOOL_REGISTRY,
            AdapterSurfaceKind.TOOL_ORCHESTRATION,
            AdapterSurfaceKind.SECURITY,
        }:
            return "Future work must remain feature-flagged and pass through PreToolGuard."

        if surface == AdapterSurfaceKind.MEMORY:
            return "Keep isolated shadow memory only; do not write Hermes native memory."

        if surface in {AdapterSurfaceKind.GATEWAY, AdapterSurfaceKind.CRON}:
            return "Use sidecar observer pattern before any native integration."

        if surface == AdapterSurfaceKind.PROVIDER:
            return "Prefer external provider wrapper; do not modify provider registry."

        return "Keep zero-touch and route through hermes_ext.harness first."