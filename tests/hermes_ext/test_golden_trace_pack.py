from __future__ import annotations

from hermes_ext.golden_trace.contracts import GoldenTraceKind
from hermes_ext.golden_trace.trace_pack import build_default_golden_trace_pack


def test_default_golden_trace_pack_has_expected_cases() -> None:
    pack = build_default_golden_trace_pack()

    kinds = {case.kind for case in pack.cases}

    assert GoldenTraceKind.DIAGNOSTIC in kinds
    assert GoldenTraceKind.SHADOW_TEXT in kinds
    assert GoldenTraceKind.SHADOW_TOOL_BLOCK in kinds
    assert GoldenTraceKind.NATIVE_BOUNDARY_SPEC in kinds
    assert len(pack.cases) >= 5


def test_default_golden_trace_pack_has_stable_case_ids() -> None:
    pack = build_default_golden_trace_pack()

    ids = [case.case_id for case in pack.cases]

    assert len(ids) == len(set(ids))
    assert "shadow-dangerous-tool-blocked" in ids