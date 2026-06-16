from __future__ import annotations

from pathlib import Path
from typing import Any

from hermes_ext.cathay.adapter import CathayContractAdapter
from hermes_ext.cathay.contracts import CathayAdapterInput, CathayTextObservation
from hermes_ext.hooks.contracts import HookDecisionType, HookEvent
from hermes_ext.hooks.dispatcher import HookDispatcher
from hermes_ext.memoryx.fusion import ShadowMemoryFusion
from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.circuit_breaker import ShadowCircuitBreaker
from hermes_ext.orchestration.contracts import (
    CheckpointKind,
    ShadowCheckpoint,
    ShadowRunConfig,
    ShadowRunResult,
    ShadowRunStatus,
    ShadowStepName,
)
from hermes_ext.orchestration.span_log import ShadowSpanLog
from hermes_ext.runtime.mock_provider import MockProviderAdapter, MockProviderConfig
from hermes_ext.runtime.request_envelope import LLMRequestEnvelope, PromptSegment


class ShadowRunner:
    """
    Runs the Phase 1-4 pipeline as a shadow workflow.

    It does not execute real tools and does not call real models.
    """

    def __init__(
        self,
        *,
        checkpoint_store: CheckpointStore,
        shadow_memory_provider: ShadowMemoryProvider,
        dispatcher: HookDispatcher | None = None,
        mock_provider: MockProviderAdapter | None = None,
        cathay_adapter: CathayContractAdapter | None = None,
        circuit_breaker: ShadowCircuitBreaker | None = None,
    ) -> None:
        self.checkpoint_store = checkpoint_store
        self.shadow_memory_provider = shadow_memory_provider
        self.dispatcher = dispatcher or HookDispatcher()
        self.mock_provider = mock_provider or MockProviderAdapter(MockProviderConfig(mode="echo"))
        self.cathay_adapter = cathay_adapter or CathayContractAdapter()
        self.circuit_breaker = circuit_breaker or ShadowCircuitBreaker()

    @classmethod
    def from_paths(cls, *, checkpoint_db: Path, shadow_memory_db: Path) -> "ShadowRunner":
        return cls(
            checkpoint_store=CheckpointStore(checkpoint_db),
            shadow_memory_provider=ShadowMemoryProvider(shadow_memory_db),
        )

    def run_text(
        self,
        text: str,
        *,
        config: ShadowRunConfig | None = None,
        tool_payload: dict[str, Any] | None = None,
    ) -> ShadowRunResult:
        config = config or ShadowRunConfig()
        span_log = ShadowSpanLog(trace_id=config.run_id)
        sequence = 0
        warnings: list[str] = []

        def checkpoint(
            step: ShadowStepName,
            kind: CheckpointKind,
            state: dict[str, Any],
            error: str | None = None,
        ) -> ShadowCheckpoint:
            nonlocal sequence
            cp = ShadowCheckpoint(
                run_id=config.run_id,
                session_id=config.session_id,
                step_name=step,
                kind=kind,
                sequence=sequence,
                state=state,
                error=error,
            )
            sequence += 1
            return self.checkpoint_store.write(cp)

        try:
            checkpoint(
                ShadowStepName.PREPARE_ENVELOPE,
                CheckpointKind.INPUT,
                {"text": text, "config": config.model_dump(mode="json")},
            )

            breaker_decision = self.circuit_breaker.before_step()
            if not breaker_decision.allowed:
                final = checkpoint(
                    ShadowStepName.FINALIZE,
                    CheckpointKind.ERROR,
                    {"reason": breaker_decision.reason},
                    error=breaker_decision.reason,
                )
                return ShadowRunResult(
                    run_id=config.run_id,
                    session_id=config.session_id,
                    status=ShadowRunStatus.CIRCUIT_OPEN,
                    checkpoint_count=self.checkpoint_store.count(config.run_id),
                    final_checkpoint_id=final.checkpoint_id,
                    error=breaker_decision.reason,
                    warnings=warnings,
                )

            envelope = LLMRequestEnvelope(
                session_id=config.session_id,
                messages=[
                    PromptSegment.from_message(
                        "user",
                        text,
                        segment_type="conversation",
                    )
                ],
                metadata={"shadow_run_id": config.run_id, **config.metadata},
            ).prepared()

            checkpoint(
                ShadowStepName.PREPARE_ENVELOPE,
                CheckpointKind.AFTER_STEP,
                {"envelope": envelope.model_dump(mode="json")},
            )

            if config.enable_pretool_guard and tool_payload is not None:
                span = span_log.start_span("pretool_guard")
                event = HookEvent.pre_tool_use(
                    trace_id=envelope.trace_id,
                    session_id=envelope.session_id,
                    turn_id=envelope.turn_id,
                    tool_name=str(tool_payload.get("tool_name", "")),
                    payload=tool_payload,
                )
                checkpoint(
                    ShadowStepName.PRETOOL_GUARD,
                    CheckpointKind.BEFORE_STEP,
                    {"event": event.model_dump(mode="json")},
                )
                result = self.dispatcher.dispatch(event)
                span_log = span_log.record(
                    span.end(
                        status="ok" if result.final_decision != HookDecisionType.DENY else "blocked"
                    )
                )
                checkpoint(
                    ShadowStepName.PRETOOL_GUARD,
                    CheckpointKind.AFTER_STEP,
                    {"hook_result": result.model_dump(mode="json")},
                )
                if result.final_decision == HookDecisionType.DENY:
                    final = checkpoint(
                        ShadowStepName.FINALIZE,
                        CheckpointKind.FINAL,
                        {
                            "blocked": True,
                            "span_log": span_log.to_audit_list(),
                        },
                    )
                    return ShadowRunResult(
                        run_id=config.run_id,
                        session_id=config.session_id,
                        status=ShadowRunStatus.COMPLETED,
                        checkpoint_count=self.checkpoint_store.count(config.run_id),
                        final_checkpoint_id=final.checkpoint_id,
                        warnings=["pretool_guard blocked tool intent"],
                        metadata={"blocked": True},
                    )

            span = span_log.start_span("mock_provider")
            checkpoint(
                ShadowStepName.MOCK_PROVIDER,
                CheckpointKind.BEFORE_STEP,
                {"envelope": envelope.to_audit_dict()},
            )
            response = self.mock_provider.generate(envelope)
            span_log = span_log.record(span.end(status="ok"))
            checkpoint(
                ShadowStepName.MOCK_PROVIDER,
                CheckpointKind.AFTER_STEP,
                {"response": response.model_dump(mode="json")},
            )

            bundle = None
            if config.enable_cathay:
                span = span_log.start_span("cathay_adapter")
                checkpoint(
                    ShadowStepName.CATHAY_ADAPTER,
                    CheckpointKind.BEFORE_STEP,
                    {"text": text},
                )
                cathay_output = self.cathay_adapter.analyze(
                    CathayAdapterInput(
                        trace_id=envelope.trace_id,
                        session_id=envelope.session_id,
                        turn_id=envelope.turn_id,
                        observations=[CathayTextObservation(text=text)],
                    )
                )
                span_log = span_log.record(span.end(status="ok" if cathay_output.ok else "error"))
                checkpoint(
                    ShadowStepName.CATHAY_ADAPTER,
                    CheckpointKind.AFTER_STEP,
                    {"cathay_output": cathay_output.model_dump(mode="json")},
                )
                warnings.extend(cathay_output.warnings)
                bundle = cathay_output.bundle

            memory_nodes = []
            if config.enable_shadow_memory:
                span = span_log.start_span("shadow_memory_write")
                checkpoint(
                    ShadowStepName.SHADOW_MEMORY_WRITE,
                    CheckpointKind.BEFORE_STEP,
                    {"has_bundle": bundle is not None},
                )
                fusion = ShadowMemoryFusion(self.shadow_memory_provider)
                if bundle is not None:
                    memory_nodes.extend(fusion.write_bundle(bundle))
                memory_nodes.append(fusion.write_envelope_metadata(envelope))
                span_log = span_log.record(span.end(status="ok"))
                checkpoint(
                    ShadowStepName.SHADOW_MEMORY_WRITE,
                    CheckpointKind.AFTER_STEP,
                    {
                        "node_count": len(memory_nodes),
                        "node_ids": [node.node_id for node in memory_nodes],
                    },
                )

            final = checkpoint(
                ShadowStepName.FINALIZE,
                CheckpointKind.FINAL,
                {
                    "status": "completed",
                    "span_log": span_log.to_audit_list(),
                    "shadow_memory_count": self.shadow_memory_provider.count_nodes(),
                },
            )

            return ShadowRunResult(
                run_id=config.run_id,
                session_id=config.session_id,
                status=ShadowRunStatus.COMPLETED,
                checkpoint_count=self.checkpoint_store.count(config.run_id),
                final_checkpoint_id=final.checkpoint_id,
                warnings=warnings,
                metadata={
                    "shadow_memory_count": self.shadow_memory_provider.count_nodes(),
                    "span_count": len(span_log.spans),
                },
            )

        except Exception as exc:
            self.circuit_breaker = self.circuit_breaker.record_failure()
            final = checkpoint(
                ShadowStepName.FINALIZE,
                CheckpointKind.ERROR,
                {"error": str(exc)},
                error=str(exc),
            )
            return ShadowRunResult(
                run_id=config.run_id,
                session_id=config.session_id,
                status=ShadowRunStatus.FAILED,
                checkpoint_count=self.checkpoint_store.count(config.run_id),
                final_checkpoint_id=final.checkpoint_id,
                error=str(exc),
                warnings=warnings,
            )