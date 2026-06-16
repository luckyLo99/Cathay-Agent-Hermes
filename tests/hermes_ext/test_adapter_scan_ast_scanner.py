from __future__ import annotations

from pathlib import Path

from hermes_ext.adapter_scan.ast_scanner import PythonASTScanner
from hermes_ext.adapter_scan.contracts import AdapterScanConfig, AdapterSurfaceKind


def test_ast_scanner_collects_imports_symbols_and_calls(tmp_path: Path) -> None:
    path = tmp_path / "providers"
    path.mkdir()
    file_path = path / "base.py"
    file_path.write_text(
        "\n".join(
            [
                "import os",
                "from typing import Any",
                "",
                "class ProviderProfile:",
                "    def build(self):",
                "        return dict()",
            ]
        ),
        encoding="utf-8",
    )

    record = PythonASTScanner(AdapterScanConfig(project_root=tmp_path)).scan_file(file_path)

    assert record.relative_path == "providers/base.py"
    assert record.surface_guess == AdapterSurfaceKind.PROVIDER
    assert any(item.module == "os" for item in record.imports)
    assert any(item.name == "ProviderProfile" for item in record.symbols)
    assert any(item.name == "dict" for item in record.calls)


def test_ast_scanner_marks_lifeline(tmp_path: Path) -> None:
    file_path = tmp_path / "cli.py"
    file_path.write_text("def main():\n    pass\n", encoding="utf-8")

    record = PythonASTScanner(AdapterScanConfig(project_root=tmp_path)).scan_file(file_path)

    assert record.is_lifeline
    assert record.surface_guess == AdapterSurfaceKind.CLI


def test_ast_scanner_records_parse_error(tmp_path: Path) -> None:
    file_path = tmp_path / "broken.py"
    file_path.write_text("def broken(:\n", encoding="utf-8")

    record = PythonASTScanner(AdapterScanConfig(project_root=tmp_path)).scan_file(file_path)

    assert record.parse_error is not None