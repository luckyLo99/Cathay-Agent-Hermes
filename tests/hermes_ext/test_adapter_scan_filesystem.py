from __future__ import annotations

from pathlib import Path

from hermes_ext.adapter_scan.contracts import AdapterScanConfig
from hermes_ext.adapter_scan.filesystem import ReadOnlyProjectFilesystem


def test_filesystem_lists_python_files_and_excludes_dirs(tmp_path: Path) -> None:
    (tmp_path / "cli.py").write_text("print('hi')\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("# readme\n", encoding="utf-8")
    (tmp_path / "hermes_ext").mkdir()
    (tmp_path / "hermes_ext" / "ignored.py").write_text("x = 1\n", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "ignored.py").write_text("x = 1\n", encoding="utf-8")

    files = ReadOnlyProjectFilesystem(
        AdapterScanConfig(project_root=tmp_path)
    ).iter_source_files()

    assert [path.relative_to(tmp_path).as_posix() for path in files] == ["cli.py"]


def test_filesystem_skips_large_file(tmp_path: Path) -> None:
    (tmp_path / "big.py").write_text("x = 'large'\n", encoding="utf-8")

    files = ReadOnlyProjectFilesystem(
        AdapterScanConfig(project_root=tmp_path, max_file_bytes=1)
    ).iter_source_files()

    assert files == []