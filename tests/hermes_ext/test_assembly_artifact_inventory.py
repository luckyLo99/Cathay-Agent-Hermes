from __future__ import annotations

from pathlib import Path

from hermes_ext.assembly.artifact_inventory import AssemblyArtifactInventory
from hermes_ext.assembly.contracts import AssemblyArtifactKind, AssemblyManifestConfig


def test_artifact_inventory_collects_source_test_report_files(tmp_path: Path) -> None:
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "x.py").write_text("x = 1\n", encoding="utf-8")
    (tmp_path / "tests" / "hermes_ext").mkdir(parents=True)
    (tmp_path / "tests" / "hermes_ext" / "test_x.py").write_text("def test_x(): pass\n", encoding="utf-8")
    (tmp_path / "reports" / "phase10").mkdir(parents=True)
    (tmp_path / "reports" / "phase10" / "r.json").write_text("{}", encoding="utf-8")

    artifacts = AssemblyArtifactInventory(
        AssemblyManifestConfig(
            project_root=tmp_path,
            require_phase9_native_boundary=False,
            require_phase10_golden_trace=False,
        )
    ).collect()

    kinds = {artifact.kind for artifact in artifacts}

    assert AssemblyArtifactKind.SOURCE in kinds
    assert AssemblyArtifactKind.TEST in kinds
    assert AssemblyArtifactKind.REPORT in kinds
    assert all(artifact.exists for artifact in artifacts)


def test_artifact_inventory_records_missing_trees(tmp_path: Path) -> None:
    artifacts = AssemblyArtifactInventory(
        AssemblyManifestConfig(
            project_root=tmp_path,
            require_phase9_native_boundary=False,
            require_phase10_golden_trace=False,
        )
    ).collect()

    assert any(not artifact.exists for artifact in artifacts)