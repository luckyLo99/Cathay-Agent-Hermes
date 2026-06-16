from __future__ import annotations

from pathlib import Path

from hermes_ext.adapter_scan.contracts import AdapterScanConfig


class ReadOnlyProjectFilesystem:
    """
    Read-only filesystem enumerator.

    It only lists candidate source files. It never imports or writes.
    """

    def __init__(self, config: AdapterScanConfig) -> None:
        self.config = config

    def iter_source_files(self) -> list[Path]:
        root = self.config.project_root
        files: list[Path] = []

        for path in root.rglob("*"):
            if not path.is_file():
                continue

            if path.suffix not in self.config.include_suffixes:
                continue

            relative = path.relative_to(root)
            if self._is_excluded(relative):
                continue

            try:
                size = path.stat().st_size
            except OSError:
                continue

            if size > self.config.max_file_bytes:
                continue

            files.append(path)

        return sorted(files, key=lambda item: item.relative_to(root).as_posix())

    def _is_excluded(self, relative: Path) -> bool:
        parts = set(relative.parts)
        return any(part in parts for part in self.config.exclude_dirs)