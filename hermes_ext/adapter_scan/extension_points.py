from __future__ import annotations

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
    SourceFileRecord,
)


class ExtensionPointMapper:
    """
    Maps static source records to future adapter candidates.

    Phase 7 does not modify these files. It only classifies risk and posture.
    """

    LIFELINE_HINTS: dict[str, tuple[AdapterSurfaceKind, RiskLevel, str]] = {
        "cli.py": (
            AdapterSurfaceKind.CLI,
            RiskLevel.CRITICAL,
            "Interactive CLI is a lifeline entrypoint; do not patch directly.",
        ),
        "run_agent.py": (
            AdapterSurfaceKind.RUNTIME_LOOP,
            RiskLevel.CRITICAL,
            "AIAgent runtime loop is the core execution path; direct edits are forbidden.",
        ),
        "hermes_cli/main.py": (
            AdapterSurfaceKind.CLI,
            RiskLevel.CRITICAL,
            "Command dispatcher is a CLI lifeline; future integration must remain external.",
        ),
        "tools/registry.py": (
            AdapterSurfaceKind.TOOL_REGISTRY,
            RiskLevel.CRITICAL,
            "Tool registry controls discovery and invocation surface; direct edits are forbidden.",
        ),
        "model_tools.py": (
            AdapterSurfaceKind.TOOL_ORCHESTRATION,
            RiskLevel.CRITICAL,
            "Tool orchestration layer is high blast-radius; direct edits are forbidden.",
        ),
        "toolsets.py": (
            AdapterSurfaceKind.TOOL_ORCHESTRATION,
            RiskLevel.HIGH,
            "Toolset definition affects available capabilities; direct edits are forbidden.",
        ),
        "agent/memory_provider.py": (
            AdapterSurfaceKind.MEMORY,
            RiskLevel.CRITICAL,
            "MemoryProvider ABC is a native memory boundary; do not replace in Phase 7.",
        ),
        "agent/memory_manager.py": (
            AdapterSurfaceKind.MEMORY,
            RiskLevel.CRITICAL,
            "MemoryManager coordinates native memory; do not patch directly.",
        ),
        "tools/memory_tool.py": (
            AdapterSurfaceKind.MEMORY,
            RiskLevel.CRITICAL,
            "Memory tool writes native memory; direct edits are forbidden.",
        ),
        "agent/system_prompt.py": (
            AdapterSurfaceKind.PROMPT,
            RiskLevel.CRITICAL,
            "System prompt affects behavior and cache stability; direct edits are forbidden.",
        ),
        "agent/prompt_builder.py": (
            AdapterSurfaceKind.PROMPT,
            RiskLevel.CRITICAL,
            "Prompt builder affects all model inputs; direct edits are forbidden.",
        ),
        "agent/context_compressor.py": (
            AdapterSurfaceKind.CONTEXT,
            RiskLevel.HIGH,
            "Context compression mutates conversation context; direct edits are forbidden.",
        ),
        "hermes_state.py": (
            AdapterSurfaceKind.STATE_DB,
            RiskLevel.CRITICAL,
            "SessionDB / SQLite / FTS state is a persistence lifeline; direct edits are forbidden.",
        ),
        "providers/__init__.py": (
            AdapterSurfaceKind.PROVIDER,
            RiskLevel.CRITICAL,
            "Provider registration controls model backends; direct edits are forbidden.",
        ),
        "providers/base.py": (
            AdapterSurfaceKind.PROVIDER,
            RiskLevel.HIGH,
            "Provider base contracts affect all providers; direct edits are forbidden.",
        ),
        "gateway/run.py": (
            AdapterSurfaceKind.GATEWAY,
            RiskLevel.HIGH,
            "Gateway runner touches platform delivery; direct edits are forbidden.",
        ),
        "gateway/platforms/base.py": (
            AdapterSurfaceKind.GATEWAY,
            RiskLevel.HIGH,
            "Gateway platform base affects all adapters; direct edits are forbidden.",
        ),
        "gateway/session.py": (
            AdapterSurfaceKind.GATEWAY,
            RiskLevel.HIGH,
            "Gateway session management is stateful; direct edits are forbidden.",
        ),
        "cron/jobs.py": (
            AdapterSurfaceKind.CRON,
            RiskLevel.HIGH,
            "Cron jobs are persistent scheduled work; direct edits are forbidden.",
        ),
        "cron/scheduler.py": (
            AdapterSurfaceKind.CRON,
            RiskLevel.HIGH,
            "Cron scheduler can trigger autonomous work; direct edits are forbidden.",
        ),
        "tools/threat_patterns.py": (
            AdapterSurfaceKind.SECURITY,
            RiskLevel.CRITICAL,
            "Threat pattern library is safety-sensitive; direct edits are forbidden.",
        ),
        "agent/redact.py": (
            AdapterSurfaceKind.SECURITY,
            RiskLevel.CRITICAL,
            "Redaction is safety-sensitive; direct edits are forbidden.",
        ),
    }

    def map_records(self, records: list[SourceFileRecord]) -> list[ExtensionPointCandidate]:
        candidates: list[ExtensionPointCandidate] = []

        for record in records:
            candidates.extend(self._map_lifeline(record))
            candidates.extend(self._map_symbols(record))

        deduped: dict[str, ExtensionPointCandidate] = {}
        for candidate in candidates:
            stable = candidate.stable_id()
            deduped[stable.candidate_id] = stable

        return sorted(
            deduped.values(),
            key=lambda item: (item.relative_path, item.surface.value, item.line, item.symbol or ""),
        )

    def _map_lifeline(self, record: SourceFileRecord) -> list[ExtensionPointCandidate]:
        hint = self.LIFELINE_HINTS.get(record.relative_path)
        if hint is None:
            return []

        surface, risk, reason = hint
        return [
            ExtensionPointCandidate(
                relative_path=record.relative_path,
                surface=surface,
                posture=AdapterIntegrationPosture.FORBIDDEN,
                risk=risk,
                symbol=None,
                line=0,
                reason=reason,
                future_adapter_hint=(
                    "Use hermes_ext.harness or an external wrapper first. "
                    "Do not edit this file until a later phase explicitly approves a minimal patch."
                ),
                allowed_next_phase="phase8_adapter_design_only",
                metadata={"lifeline": True, "sha256": record.sha256},
            )
        ]

    def _map_symbols(self, record: SourceFileRecord) -> list[ExtensionPointCandidate]:
        candidates: list[ExtensionPointCandidate] = []

        for symbol in record.symbols:
            lowered = symbol.name.lower()

            if "provider" in lowered:
                candidates.append(
                    self._symbol_candidate(
                        record,
                        symbol_name=symbol.qualname,
                        line=symbol.line,
                        surface=AdapterSurfaceKind.PROVIDER,
                        posture=AdapterIntegrationPosture.WRAPPER_ONLY,
                        risk=RiskLevel.HIGH if record.is_lifeline else RiskLevel.MEDIUM,
                        reason="Provider-like symbol detected by static AST scan.",
                        hint="Future integration should prefer external provider wrapper or feature-flagged sidecar.",
                    )
                )

            if "memory" in lowered:
                candidates.append(
                    self._symbol_candidate(
                        record,
                        symbol_name=symbol.qualname,
                        line=symbol.line,
                        surface=AdapterSurfaceKind.MEMORY,
                        posture=AdapterIntegrationPosture.WRAPPER_ONLY,
                        risk=RiskLevel.HIGH if record.is_lifeline else RiskLevel.MEDIUM,
                        reason="Memory-like symbol detected by static AST scan.",
                        hint="Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved.",
                    )
                )

            if "tool" in lowered or "registry" in lowered:
                candidates.append(
                    self._symbol_candidate(
                        record,
                        symbol_name=symbol.qualname,
                        line=symbol.line,
                        surface=AdapterSurfaceKind.TOOL_REGISTRY,
                        posture=AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED,
                        risk=RiskLevel.HIGH,
                        reason="Tool/registry-like symbol detected by static AST scan.",
                        hint="Future integration must pass through PreToolGuard and feature flags.",
                    )
                )

            if "gateway" in lowered or "session" in lowered:
                candidates.append(
                    self._symbol_candidate(
                        record,
                        symbol_name=symbol.qualname,
                        line=symbol.line,
                        surface=AdapterSurfaceKind.GATEWAY,
                        posture=AdapterIntegrationPosture.WRAPPER_ONLY,
                        risk=RiskLevel.HIGH,
                        reason="Gateway/session-like symbol detected by static AST scan.",
                        hint="Future integration should remain gateway-sidecar before any native gateway change.",
                    )
                )

        return candidates

    def _symbol_candidate(
        self,
        record: SourceFileRecord,
        *,
        symbol_name: str,
        line: int,
        surface: AdapterSurfaceKind,
        posture: AdapterIntegrationPosture,
        risk: RiskLevel,
        reason: str,
        hint: str,
    ) -> ExtensionPointCandidate:
        if record.is_lifeline:
            posture = AdapterIntegrationPosture.FORBIDDEN
            risk = RiskLevel.CRITICAL if risk == RiskLevel.HIGH else risk
            hint = "Lifeline file: classification only. Do not patch directly."

        return ExtensionPointCandidate(
            relative_path=record.relative_path,
            surface=surface,
            posture=posture,
            risk=risk,
            symbol=symbol_name,
            line=line,
            reason=reason,
            future_adapter_hint=hint,
            allowed_next_phase="phase8_adapter_design_only",
            metadata={"lifeline": record.is_lifeline},
        )