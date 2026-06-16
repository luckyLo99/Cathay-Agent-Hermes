from __future__ import annotations

from hermes_ext.golden_trace.contracts import (
    GoldenTraceCase,
    GoldenTraceKind,
    GoldenTracePack,
)


def build_default_golden_trace_pack() -> GoldenTracePack:
    """
    Default deterministic golden trace pack.

    Cases intentionally cover:
    - diagnostics only
    - normal shadow run
    - dangerous tool blocked by PreToolGuard
    - shadow run with Cathay and memory disabled
    - no-op native boundary suite derived from Phase 8 spec
    """

    return GoldenTracePack(
        name="phase10-default-golden-trace-pack",
        version="1",
        cases=[
            GoldenTraceCase(
                case_id="diagnostic-default-off",
                name="Diagnostics remain safe with all feature flags disabled",
                kind=GoldenTraceKind.DIAGNOSTIC,
                flags={},
                expected_ok=True,
            ),
            GoldenTraceCase(
                case_id="shadow-basic-all-enabled",
                name="Shadow harness completes with Cathay, memory, replay enabled",
                kind=GoldenTraceKind.SHADOW_TEXT,
                text="Phase 10 golden trace: Hermes shadow replay must be stable.",
                flags={
                    "enabled": True,
                    "shadow_runner": True,
                    "pretool_guard": True,
                    "cathay": True,
                    "memoryx": True,
                    "checkpoint_replay": True,
                },
                expected_ok=True,
                expected_shadow_status="completed",
            ),
            GoldenTraceCase(
                case_id="shadow-dangerous-tool-blocked",
                name="Dangerous tool intent is blocked and remains deterministic",
                kind=GoldenTraceKind.SHADOW_TOOL_BLOCK,
                text="Phase 10 golden trace: dangerous shell intent must be blocked.",
                flags={
                    "enabled": True,
                    "shadow_runner": True,
                    "pretool_guard": True,
                    "cathay": False,
                    "memoryx": False,
                    "checkpoint_replay": True,
                },
                tool_payload={
                    "tool_name": "bash",
                    "argv": ["rm", "-rf", "/"],
                },
                expected_ok=True,
                expected_shadow_status="completed",
                expected_blocked=True,
            ),
            GoldenTraceCase(
                case_id="shadow-minimal-no-cathay-no-memory",
                name="Shadow harness completes with Cathay and memory disabled",
                kind=GoldenTraceKind.SHADOW_NO_CATHAY_NO_MEMORY,
                text="Phase 10 golden trace: minimal shadow run.",
                flags={
                    "enabled": True,
                    "shadow_runner": True,
                    "pretool_guard": False,
                    "cathay": False,
                    "memoryx": False,
                    "checkpoint_replay": False,
                },
                expected_ok=True,
                expected_shadow_status="completed",
            ),
            GoldenTraceCase(
                case_id="native-boundary-spec-noop",
                name="Native boundary spec-derived suite remains no-op or blocked",
                kind=GoldenTraceKind.NATIVE_BOUNDARY_SPEC,
                expected_ok=True,
                expected_native_violations=0,
            ),
        ],
        metadata={
            "phase": 10,
            "purpose": "deterministic shadow replay and no-op boundary verification",
        },
    )