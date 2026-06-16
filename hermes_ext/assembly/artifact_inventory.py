from __future__ import annotations

import hashlib
from pathlib import Path

from hermes_ext.assembly.contracts import AssemblyArtifact, AssemblyArtifactKind, AssemblyManifestConfig


class AssemblyArtifactInventory:
    """
    Read-only artifact inventory.

    It records hermes_ext source files, hermes_ext tests, and phase reports.
    It never imports scanned modules and never writes scanned files.
    """

    EXCLUDED_DIR_NAMES = {
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        ".git",
        ".venv",
        "venv",
    }

    def __init__(self, config: AssemblyManifestConfig) -> None:
        self.config = config

    def collect(self) -> list[AssemblyArtifact]:
        artifacts: list[AssemblyArtifact] = []
        artifacts.extend(self._collect_tree("hermes_ext", AssemblyArtifactKind.SOURCE))

        if self.config.include_tests:
            artifacts.extend(self._collect_tree("tests/hermes_ext", AssemblyArtifactKind.TEST))

        if self.config.include_reports:
            artifacts.extend(self._collect_tree("reports", AssemblyArtifactKind.REPORT))

        artifacts = sorted(
            artifacts,
            key=lambda item: (item.kind.value, item.relative_path),
        )

        return artifacts[: self.config.max_artifacts]

    def _collect_tree(self, relative_root: str, kind: AssemblyArtifactKind) -> list[AssemblyArtifact]:
        root = self.config.project_root / relative_root
        if not root.exists():
            return [
                AssemblyArtifact(
                    relative_path=relative_root,
                    kind=kind,
                    exists=False,
                    metadata={"missing_tree": True},
                )
            ]

        artifacts: list[AssemblyArtifact] = []
        for path in root.rglob("*"):
            if not path.is_file():
                continue

            if self._is_excluded(path):
                continue

            if path.suffix not in {".py", ".md", ".json", ".txt"}:
                continue

            artifacts.append(self._artifact_for_path(path, kind))

        return artifacts

    def _artifact_for_path(self, path: Path, kind: AssemblyArtifactKind) -> AssemblyArtifact:
        relative = path.relative_to(self.config.project_root).as_posix()
        content = path.read_bytes()

        return AssemblyArtifact(
            relative_path=relative,
            kind=kind,
            exists=True,
            size_bytes=len(content),
            sha256=hashlib.sha256(content).hexdigest(),
        )

    def _is_excluded(self, path: Path) -> bool:
        return any(part in self.EXCLUDED_DIR_NAMES for part in path.parts)
