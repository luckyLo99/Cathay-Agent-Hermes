from __future__ import annotations

from pathlib import Path
from typing import Any

from hermes_ext.harness.contracts import (
    ExtensionFlagName,
    ExtensionHarnessMode,
    HarnessRunRequest,
    HarnessRunResult,
)
from hermes_ext.harness.diagnostics import ExtensionDiagnostics
from hermes_ext.hooks.builtin_hooks import build_default_dispatcher
from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.orchestration.checkpoint_store import CheckpointStore
from hermes_ext.orchestration.contracts import ReplayMode, ShadowRunConfig
from hermes_ext.orchestration.replay import ReplayService
from hermes_ext.orchestration.shadow_runner import ShadowRunner


class IntegrationHarness:
    """
    Explicit local integration harness.

    It is the only Phase 6 entrypoint that connects feature flags to ShadowRunner.
    """

    def __init__(self, *, project_root: Path | None = None) -> None:
        self.project_root = project_root or Path.cwd()

    def run(self, request: HarnessRunRequest) -> HarnessRunResult:
        diagnostics = ExtensionDiagnostics(
            project_root=self.project_root,
            flags=request.flags,
        ).run()

        warnings: list[str] = []
        if not diagnostics.ok:
            return HarnessRunResult(
                request_id=request.request_id,
                ok=False,
                mode=request.mode,
                flags=request.flags.to_audit_dict(),
                diagnostics=diagnostics.to_audit_dict(),
                error="extension diagnostics failed",
            )

        if request.mode == ExtensionHarnessMode.OFF:
            return HarnessRunResult(
                request_id=request.request_id,
                ok=True,
                mode=request.mode,
                flags=request.flags.to_audit_dict(),
                diagnostics=diagnostics.to_audit_dict(),
                warnings=["harness mode is off"],
            )

        if request.mode == ExtensionHarnessMode.DIAGNOSTIC:
            return HarnessRunResult(
                request_id=request.request_id,
                ok=True,
                mode=request.mode,
                flags=request.flags.to_audit_dict(),
                diagnostics=diagnostics.to_audit_dict(),
            )

        if not request.flags.is_enabled(ExtensionFlagName.SHADOW_RUNNER):
            return HarnessRunResult(
                request_id=request.request_id,
                ok=False,
                mode=request.mode,
                flags=request.flags.to_audit_dict(),
                diagnostics=diagnostics.to_audit_dict(),
                error="shadow_runner flag is not effectively enabled",
            )

        request.state_dir.mkdir(parents=True, exist_ok=True)
        checkpoint_db = request.state_dir / "shadow_checkpoints.db"
        memory_db = request.state_dir / "shadow_memory.db"

        dispatcher = build_default_dispatcher() if request.flags.is_enabled(ExtensionFlagName.PRETOOL_GUARD) else None

        checkpoint_store = CheckpointStore(checkpoint_db)
        shadow_memory_provider = ShadowMemoryProvider(memory_db)

        runner = ShadowRunner(
            checkpoint_store=checkpoint_store,
            shadow_memory_provider=shadow_memory_provider,
            dispatcher=dispatcher,
        )

        shadow_config = ShadowRunConfig(
            session_id=f"harness-{request.request_id}",
            enable_cathay=request.flags.is_enabled(ExtensionFlagName.CATHAY),
            enable_shadow_memory=request.flags.is_enabled(ExtensionFlagName.MEMORYX),
            enable_pretool_guard=request.flags.is_enabled(ExtensionFlagName.PRETOOL_GUARD),
            metadata={
                "harness_request_id": request.request_id,
                **request.metadata,
            },
        )

        shadow_result = runner.run_text(
            request.text,
            config=shadow_config,
            tool_payload=request.tool_payload,
        )

        replay_result: dict[str, Any] | None = None
        if request.flags.is_enabled(ExtensionFlagName.CHECKPOINT_REPLAY):
            replay = ReplayService(checkpoint_store).replay_run(
                shadow_result.run_id,
                mode=ReplayMode.DRY_RUN,
            )
            replay_result = replay.model_dump(mode="json")

        if not request.flags.is_enabled(ExtensionFlagName.CATHAY):
            warnings.append("cathay disabled by feature flag")

        if not request.flags.is_enabled(ExtensionFlagName.MEMORYX):
            warnings.append("memoryx shadow memory disabled by feature flag")

        return HarnessRunResult(
            request_id=request.request_id,
            ok=shadow_result.error is None,
            mode=request.mode,
            flags=request.flags.to_audit_dict(),
            diagnostics=diagnostics.to_audit_dict(),
            shadow_result=shadow_result.model_dump(mode="json"),
            replay_result=replay_result,
            error=shadow_result.error,
            warnings=[*warnings, *shadow_result.warnings],
        )