from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from hermes_ext.assembly.contracts import (
    AssemblyArtifact,
    AssemblyArtifactKind,
    AssemblyInvariant,
    AssemblyInvariantSeverity,
    AssemblyInvariantStatus,
    AssemblyManifest,
    AssemblyManifestConfig,
    AssemblySummary,
)


def test_manifest_config_normalizes_project_root(tmp_path: Path) -> None:
    config = AssemblyManifestConfig(project_root=tmp_path)

    assert config.project_root == tmp_path.resolve()


def test_artifact_rejects_path_escape() -> None:
    with pytest.raises(ValidationError):
        AssemblyArtifact(
            relative_path="../cli.py",
            kind=AssemblyArtifactKind.SOURCE,
            exists=True,
        )


def test_artifact_rejects_bad_sha() -> None:
    with pytest.raises(ValidationError):
        AssemblyArtifact(
            relative_path="hermes_ext/x.py",
            kind=AssemblyArtifactKind.SOURCE,
            exists=True,
            sha256="bad",
        )


def test_manifest_hash_is_stable() -> None:
    invariant = AssemblyInvariant(
        invariant_id="test",
        status=AssemblyInvariantStatus.PASS,
        severity=AssemblyInvariantSeverity.INFO,
        message="ok",
    )
    manifest = AssemblyManifest(
        project_root=".",
        artifacts=[],
        invariants=[invariant],
        summary=AssemblySummary(
            total_artifacts=0,
            invariants_passed=1,
            invariants_warned=0,
            invariants_failed=0,
        ),
    ).with_hash()

    assert manifest.manifest_hash
    assert manifest.with_hash().manifest_hash == manifest.manifest_hash


def test_manifest_summary_must_match() -> None:
    with pytest.raises(ValidationError):
        AssemblyManifest(
            project_root=".",
            artifacts=[],
            invariants=[],
            summary=AssemblySummary(total_artifacts=1),
        )