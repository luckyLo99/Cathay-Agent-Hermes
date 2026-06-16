from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.assembly.artifact_inventory import AssemblyArtifactInventory
from hermes_ext.assembly.contracts import AssemblyInvariantStatus, AssemblyManifestConfig
from hermes_ext.assembly.invariant_suite import AssemblyInvariantSuite


def create_clean_phase_reports(root: Path) -> None:
    (root / "reports" / "phase10").mkdir(parents=True)
    (root / "reports" / "phase10" / "golden_trace_replay_report.json").write_text(
        json.dumps(
            {
                "ok": True,
                "case_count": 5,
                "stable_cases": 5,
                "unstable_cases": 0,
                "failed": 0,
                "violations": [],
            }
        ),
        encoding="utf-8",
    )
    (root / "reports" / "phase9").mkdir(parents=True)
    (root / "reports" / "phase9" / "native_boundary_contract_report.json").write_text(
        json.dumps(
            {
                "ok": True,
                "failed": 0,
                "violations": [],
                "results": [
                    {
                        "native_called": False,
                        "tool_executed": False,
                        "provider_called": False,
                        "memory_written": False,
                        "state_mutated": False,
                        "patch_generated": False,
                        "secret_read": False,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


def test_invariant_suite_passes_clean_minimal_project(tmp_path: Path) -> None:
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "x.py").write_text("x = 1\n", encoding="utf-8")
    create_clean_phase_reports(tmp_path)

    config = AssemblyManifestConfig(project_root=tmp_path)
    artifacts = AssemblyArtifactInventory(config).collect()
    invariants = AssemblyInvariantSuite(config).run(artifacts)

    assert all(item.status != AssemblyInvariantStatus.FAIL for item in invariants)


def test_invariant_suite_detects_forbidden_import(tmp_path: Path) -> None:
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "bad.py").write_text("import run_agent\n", encoding="utf-8")
    create_clean_phase_reports(tmp_path)

    config = AssemblyManifestConfig(project_root=tmp_path)
    artifacts = AssemblyArtifactInventory(config).collect()
    invariants = AssemblyInvariantSuite(config).run(artifacts)

    assert any(
        item.invariant_id == "assembly.no_forbidden_imports"
        and item.status == AssemblyInvariantStatus.FAIL
        for item in invariants
    )


def test_invariant_suite_detects_bad_golden_trace(tmp_path: Path) -> None:
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "x.py").write_text("x = 1\n", encoding="utf-8")
    create_clean_phase_reports(tmp_path)
    (tmp_path / "reports" / "phase10" / "golden_trace_replay_report.json").write_text(
        json.dumps(
            {
                "ok": False,
                "case_count": 5,
                "stable_cases": 4,
                "unstable_cases": 1,
                "failed": 1,
                "violations": ["unstable"],
            }
        ),
        encoding="utf-8",
    )

    config = AssemblyManifestConfig(project_root=tmp_path)
    artifacts = AssemblyArtifactInventory(config).collect()
    invariants = AssemblyInvariantSuite(config).run(artifacts)

    assert any(
        item.invariant_id == "assembly.phase10_golden_trace_stable"
        and item.status == AssemblyInvariantStatus.FAIL
        for item in invariants
    )