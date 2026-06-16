from __future__ import annotations

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
)
from hermes_ext.integration_spec.contracts import (
    IntegrationAdapterLayer,
    IntegrationConstraint,
    IntegrationMode,
    IntegrationSpecStatus,
    RequiredFeatureFlag,
)


class IntegrationGuardrailPolicy:
    """
    Converts Phase 7 adapter scan posture into zero-touch Phase 8 design posture.

    This policy is intentionally conservative.
    """

    def mode_for_candidate(self, candidate: ExtensionPointCandidate) -> IntegrationMode:
        if candidate.posture == AdapterIntegrationPosture.FORBIDDEN:
            return IntegrationMode.FORBIDDEN

        if candidate.posture == AdapterIntegrationPosture.READ_ONLY:
            return IntegrationMode.NO_TOUCH

        if candidate.posture == AdapterIntegrationPosture.WRAPPER_ONLY:
            if candidate.surface in {
                AdapterSurfaceKind.GATEWAY,
                AdapterSurfaceKind.CRON,
            }:
                return IntegrationMode.SIDE_CAR_OBSERVER
            return IntegrationMode.EXTERNAL_WRAPPER

        if candidate.posture == AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED:
            return IntegrationMode.FEATURE_FLAG_SHADOW

        if candidate.posture == AdapterIntegrationPosture.ADAPTER_CANDIDATE:
            return IntegrationMode.EXTERNAL_HARNESS

        return IntegrationMode.NO_TOUCH

    def status_for_mode(self, mode: IntegrationMode) -> IntegrationSpecStatus:
        if mode == IntegrationMode.FORBIDDEN:
            return IntegrationSpecStatus.BLOCKED

        if mode in {
            IntegrationMode.EXTERNAL_WRAPPER,
            IntegrationMode.FEATURE_FLAG_SHADOW,
            IntegrationMode.SIDE_CAR_OBSERVER,
            IntegrationMode.EXTERNAL_HARNESS,
        }:
            return IntegrationSpecStatus.READY_FOR_SHADOW_HARNESS

        return IntegrationSpecStatus.DESIGN_ONLY

    def adapter_layer_for_surface(self, surface: AdapterSurfaceKind) -> IntegrationAdapterLayer:
        mapping = {
            AdapterSurfaceKind.CLI: IntegrationAdapterLayer.CLI_BOUNDARY,
            AdapterSurfaceKind.RUNTIME_LOOP: IntegrationAdapterLayer.RUNTIME_LOOP_BOUNDARY,
            AdapterSurfaceKind.PROVIDER: IntegrationAdapterLayer.PROVIDER_BOUNDARY,
            AdapterSurfaceKind.TOOL_REGISTRY: IntegrationAdapterLayer.TOOL_SAFETY_BOUNDARY,
            AdapterSurfaceKind.TOOL_ORCHESTRATION: IntegrationAdapterLayer.TOOL_SAFETY_BOUNDARY,
            AdapterSurfaceKind.MEMORY: IntegrationAdapterLayer.MEMORY_SHADOW_BOUNDARY,
            AdapterSurfaceKind.PROMPT: IntegrationAdapterLayer.PROMPT_CONTEXT_BOUNDARY,
            AdapterSurfaceKind.CONTEXT: IntegrationAdapterLayer.PROMPT_CONTEXT_BOUNDARY,
            AdapterSurfaceKind.STATE_DB: IntegrationAdapterLayer.STATE_DB_BOUNDARY,
            AdapterSurfaceKind.GATEWAY: IntegrationAdapterLayer.GATEWAY_SIDECAR_BOUNDARY,
            AdapterSurfaceKind.CRON: IntegrationAdapterLayer.CRON_OBSERVER_BOUNDARY,
            AdapterSurfaceKind.SECURITY: IntegrationAdapterLayer.SECURITY_POLICY_BOUNDARY,
        }
        return mapping.get(surface, IntegrationAdapterLayer.UNKNOWN_BOUNDARY)

    def flags_for_mode_and_surface(
        self,
        mode: IntegrationMode,
        surface: AdapterSurfaceKind,
    ) -> list[RequiredFeatureFlag]:
        if mode in {IntegrationMode.FORBIDDEN, IntegrationMode.NO_TOUCH}:
            return []

        flags = [
            RequiredFeatureFlag.HERMES_EXT_ENABLED,
            RequiredFeatureFlag.HERMES_EXT_SHADOW_RUNNER,
        ]

        if mode == IntegrationMode.FEATURE_FLAG_SHADOW:
            flags.append(RequiredFeatureFlag.HERMES_EXT_PRETOOL_GUARD)

        if surface == AdapterSurfaceKind.MEMORY:
            flags.append(RequiredFeatureFlag.HERMES_EXT_MEMORYX)

        if surface in {
            AdapterSurfaceKind.PROMPT,
            AdapterSurfaceKind.CONTEXT,
            AdapterSurfaceKind.RUNTIME_LOOP,
        }:
            flags.append(RequiredFeatureFlag.HERMES_EXT_CATHAY)

        if surface in {
            AdapterSurfaceKind.TOOL_REGISTRY,
            AdapterSurfaceKind.TOOL_ORCHESTRATION,
            AdapterSurfaceKind.SECURITY,
        }:
            flags.append(RequiredFeatureFlag.HERMES_EXT_PRETOOL_GUARD)

        return self._dedupe(flags)

    def constraints_for_candidate(
        self,
        candidate: ExtensionPointCandidate,
        mode: IntegrationMode,
    ) -> list[IntegrationConstraint]:
        constraints = [
            IntegrationConstraint(
                rule_id="zero_touch.no_core_patch",
                description="Do not modify Hermes core source files.",
                severity=RiskLevel.CRITICAL,
            ),
            IntegrationConstraint(
                rule_id="zero_touch.no_runtime_import",
                description="Do not import or execute Hermes runtime from integration spec.",
                severity=RiskLevel.CRITICAL,
            ),
            IntegrationConstraint(
                rule_id="zero_touch.no_secret_read",
                description="Do not read .env, API keys, tokens, or provider credentials.",
                severity=RiskLevel.CRITICAL,
            ),
        ]

        if mode == IntegrationMode.FORBIDDEN:
            constraints.append(
                IntegrationConstraint(
                    rule_id="zero_touch.forbidden_means_blocked",
                    description="Forbidden scan candidates are blocked from integration design.",
                    severity=RiskLevel.CRITICAL,
                )
            )

        if mode == IntegrationMode.FEATURE_FLAG_SHADOW:
            constraints.append(
                IntegrationConstraint(
                    rule_id="zero_touch.feature_flag_required",
                    description="Future shadow integration must be gated by HERMES_EXT_* feature flags.",
                    severity=RiskLevel.HIGH,
                )
            )

        if candidate.surface in {
            AdapterSurfaceKind.TOOL_REGISTRY,
            AdapterSurfaceKind.TOOL_ORCHESTRATION,
        }:
            constraints.append(
                IntegrationConstraint(
                    rule_id="zero_touch.pretool_guard_required",
                    description="Any future tool-related integration must pass through PreToolGuard.",
                    severity=RiskLevel.CRITICAL,
                )
            )

        if candidate.surface == AdapterSurfaceKind.MEMORY:
            constraints.append(
                IntegrationConstraint(
                    rule_id="zero_touch.shadow_memory_only",
                    description="Memory integrations must remain shadow-only until native adapter approval.",
                    severity=RiskLevel.CRITICAL,
                )
            )

        if candidate.surface in {
            AdapterSurfaceKind.PROMPT,
            AdapterSurfaceKind.CONTEXT,
            AdapterSurfaceKind.STATE_DB,
            AdapterSurfaceKind.RUNTIME_LOOP,
            AdapterSurfaceKind.CLI,
        }:
            constraints.append(
                IntegrationConstraint(
                    rule_id="zero_touch.lifeline_boundary",
                    description="Prompt, context, state, CLI, and runtime-loop boundaries require explicit later approval.",
                    severity=RiskLevel.CRITICAL,
                )
            )

        return self._dedupe_constraints(constraints)

    def required_tests_for_candidate(
        self,
        candidate: ExtensionPointCandidate,
        mode: IntegrationMode,
    ) -> list[str]:
        tests = [
            "pytest tests/hermes_ext -q",
            "python -m hermes_ext.runtime.agent_doctor --json --project-root .",
            "python -m hermes_ext.harness.cli doctor --project-root . --state-dir .hermes_ext_shadow --json",
            "python cli.py --help",
            "hermes doctor",
        ]

        if mode == IntegrationMode.FEATURE_FLAG_SHADOW:
            tests.append("shadow-run with explicit flags-json")
            tests.append("kill_switch=true disables integration")

        if candidate.surface in {
            AdapterSurfaceKind.TOOL_REGISTRY,
            AdapterSurfaceKind.TOOL_ORCHESTRATION,
            AdapterSurfaceKind.SECURITY,
        }:
            tests.append("dangerous tool intent is blocked by PreToolGuard")

        if candidate.surface == AdapterSurfaceKind.MEMORY:
            tests.append("shadow memory write does not touch Hermes native memory")
            tests.append("HIGH PII is quarantined")

        if mode == IntegrationMode.FORBIDDEN:
            tests.append("no generated patch references forbidden file")

        return self._dedupe_text(tests)

    def rollback_strategy_for_mode(self, mode: IntegrationMode) -> str:
        if mode == IntegrationMode.FORBIDDEN:
            return "No integration permitted. Rollback is no-op because no patch may be produced."

        return (
            "Disable HERMES_EXT_ENABLED or enable HERMES_EXT_KILL_SWITCH; "
            "delete only hermes_ext-generated shadow state; never modify Hermes native state."
        )

    def rationale_for_candidate(
        self,
        candidate: ExtensionPointCandidate,
        mode: IntegrationMode,
    ) -> str:
        if mode == IntegrationMode.FORBIDDEN:
            return (
                f"{candidate.relative_path} is classified as forbidden by Phase 7 scan. "
                "Phase 8 preserves that decision and blocks direct integration."
            )

        if mode == IntegrationMode.EXTERNAL_WRAPPER:
            return (
                "Candidate may be represented by an external wrapper, but the source file remains untouched."
            )

        if mode == IntegrationMode.FEATURE_FLAG_SHADOW:
            return (
                "Candidate is tool or orchestration sensitive; only shadow execution behind explicit flags is allowed."
            )

        if mode == IntegrationMode.SIDE_CAR_OBSERVER:
            return (
                "Candidate is gateway/session/cron sensitive; future work must stay as sidecar observer first."
            )

        if mode == IntegrationMode.EXTERNAL_HARNESS:
            return (
                "Candidate can be explored only through hermes_ext.harness without modifying Hermes core."
            )

        return "Candidate remains design-only and no-touch."

    @staticmethod
    def _dedupe(flags: list[RequiredFeatureFlag]) -> list[RequiredFeatureFlag]:
        seen: set[RequiredFeatureFlag] = set()
        output: list[RequiredFeatureFlag] = []
        for flag in flags:
            if flag not in seen:
                output.append(flag)
                seen.add(flag)
        return output

    @staticmethod
    def _dedupe_text(values: list[str]) -> list[str]:
        seen: set[str] = set()
        output: list[str] = []
        for value in values:
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output

    @staticmethod
    def _dedupe_constraints(values: list[IntegrationConstraint]) -> list[IntegrationConstraint]:
        seen: set[str] = set()
        output: list[IntegrationConstraint] = []
        for value in values:
            if value.rule_id not in seen:
                output.append(value)
                seen.add(value.rule_id)
        return output