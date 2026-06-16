from __future__ import annotations

from hermes_ext.golden_trace.contracts import (
    GoldenTraceCase,
    GoldenTraceCaseResult,
    GoldenTraceKind,
    GoldenTracePack,
    GoldenTraceStatus,
)
from hermes_ext.golden_trace.verifier import GoldenTraceVerifier


def test_verifier_accepts_stable_hashes() -> None:
    pack = GoldenTracePack(
        cases=[
            GoldenTraceCase(
                case_id="case",
                name="case",
                kind=GoldenTraceKind.DIAGNOSTIC,
            )
        ]
    )
    results = [
        GoldenTraceCaseResult(
            case_id="case",
            iteration=0,
            ok=True,
            status=GoldenTraceStatus.PASSED,
            canonical_hash="abc",
            normalized_output={"ok": True},
        ),
        GoldenTraceCaseResult(
            case_id="case",
            iteration=1,
            ok=True,
            status=GoldenTraceStatus.PASSED,
            canonical_hash="abc",
            normalized_output={"ok": True},
        ),
    ]

    verification = GoldenTraceVerifier().verify(pack=pack, results=results)

    assert verification.ok
    assert verification.stable_cases == 1


def test_verifier_rejects_unstable_hashes() -> None:
    pack = GoldenTracePack(
        cases=[
            GoldenTraceCase(
                case_id="case",
                name="case",
                kind=GoldenTraceKind.DIAGNOSTIC,
            )
        ]
    )
    results = [
        GoldenTraceCaseResult(
            case_id="case",
            iteration=0,
            ok=True,
            status=GoldenTraceStatus.PASSED,
            canonical_hash="abc",
            normalized_output={"ok": True},
        ),
        GoldenTraceCaseResult(
            case_id="case",
            iteration=1,
            ok=True,
            status=GoldenTraceStatus.PASSED,
            canonical_hash="def",
            normalized_output={"ok": True},
        ),
    ]

    verification = GoldenTraceVerifier().verify(pack=pack, results=results)

    assert not verification.ok
    assert verification.unstable_cases == 1