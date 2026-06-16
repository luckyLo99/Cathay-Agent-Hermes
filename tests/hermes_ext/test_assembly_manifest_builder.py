from __future__ import annotations

import json
from pathlib import Path

from hermes_ext.assembly.contracts import AssemblyManifestConfig
from hermes_ext.assembly.manifest_builder import AssemblyManifestBuilder


def create_reports(root: Path) -> None:
    (root / "reports" / "phase10").mkdir(parents=True)
    (root / "reports" / "phase10" / "golden_trace_replay_report.json").write_text(
        json.dumps({"ok": True, "case_count": 1, "stable_cases": 1, "unstable_cases": 0, "failed": 0, "violations": []}),
        encoding="utf-8",
    )
    (root / "reports" / "phase9").mkdir(parents=True)
    (root / "reports" / "phase9" / "native_boundary_contract_report.json").write_text(
        json.dumps({"ok": True, "failed": 0, "violations": [], "results": []}),
        encoding="utf-8",
    )


def test_manifest_builder_builds_manifest(tmp_path: Path) -> None:
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "x.py").write_text("x = 1\n", encoding="utf-8")
    create_reports(tmp_path)

    manifest = AssemblyManifestBuilder(
        AssemblyManifestConfig(project_root=tmp_path)
    ).build()

    assert manifest.manifest_hash
    assert manifest.summary.source_artifacts == 1
    assert manifest.summary.invariants_failed == 0