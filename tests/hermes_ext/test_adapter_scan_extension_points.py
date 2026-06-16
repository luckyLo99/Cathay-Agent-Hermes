from __future__ import annotations

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterSurfaceKind,
    PythonSymbolRecord,
    RiskLevel,
    SourceFileRecord,
)
from hermes_ext.adapter_scan.extension_points import ExtensionPointMapper


def make_record(path: str, *, lifeline: bool = False, symbols: list[PythonSymbolRecord] | None = None) -> SourceFileRecord:
    return SourceFileRecord(
        relative_path=path,
        size_bytes=1,
        line_count=1,
        sha256="a" * 64,
        is_lifeline=lifeline,
        surface_guess=AdapterSurfaceKind.UNKNOWN,
        symbols=symbols or [],
    )


def test_mapper_marks_cli_as_forbidden_lifeline() -> None:
    candidates = ExtensionPointMapper().map_records([make_record("cli.py", lifeline=True)])

    assert candidates
    assert candidates[0].posture == AdapterIntegrationPosture.FORBIDDEN
    assert candidates[0].risk == RiskLevel.CRITICAL


def test_mapper_detects_provider_symbol() -> None:
    record = make_record(
        "some/provider_module.py",
        symbols=[
            PythonSymbolRecord(
                kind="class",
                name="CustomProvider",
                qualname="CustomProvider",
                line=3,
            )
        ],
    )

    candidates = ExtensionPointMapper().map_records([record])

    assert any(candidate.surface == AdapterSurfaceKind.PROVIDER for candidate in candidates)
    assert any(candidate.posture == AdapterIntegrationPosture.WRAPPER_ONLY for candidate in candidates)


def test_mapper_forces_lifeline_symbol_forbidden() -> None:
    record = make_record(
        "agent/memory_provider.py",
        lifeline=True,
        symbols=[
            PythonSymbolRecord(
                kind="class",
                name="MemoryProvider",
                qualname="MemoryProvider",
                line=10,
            )
        ],
    )

    candidates = ExtensionPointMapper().map_records([record])

    assert candidates
    assert all(candidate.posture == AdapterIntegrationPosture.FORBIDDEN for candidate in candidates)