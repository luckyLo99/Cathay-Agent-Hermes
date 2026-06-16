from __future__ import annotations

import ast
import hashlib
from pathlib import Path

from hermes_ext.adapter_scan.contracts import (
    AdapterScanConfig,
    AdapterSurfaceKind,
    PythonCallRecord,
    PythonImportRecord,
    PythonSymbolRecord,
    SourceFileRecord,
)


class PythonASTScanner:
    """
    Static AST scanner.

    This class reads source text and parses AST.
    It never imports or executes the scanned module.
    """

    def __init__(self, config: AdapterScanConfig) -> None:
        self.config = config

    def scan_file(self, path: Path) -> SourceFileRecord:
        relative_path = path.relative_to(self.config.project_root).as_posix()
        content_bytes = path.read_bytes()
        sha256 = hashlib.sha256(content_bytes).hexdigest()

        try:
            source = content_bytes.decode("utf-8")
        except UnicodeDecodeError:
            source = content_bytes.decode("utf-8", errors="replace")

        base = {
            "relative_path": relative_path,
            "size_bytes": len(content_bytes),
            "line_count": len(source.splitlines()),
            "sha256": sha256,
            "is_lifeline": relative_path in self.config.lifeline_files,
            "surface_guess": self._guess_surface(relative_path),
        }

        try:
            tree = ast.parse(source, filename=relative_path)
        except SyntaxError as exc:
            return SourceFileRecord(
                **base,
                parse_error=f"{exc.__class__.__name__}: {exc}",
            )

        visitor = _ASTRecordVisitor()
        visitor.visit(tree)

        return SourceFileRecord(
            **base,
            imports=visitor.imports,
            symbols=visitor.symbols,
            calls=visitor.calls,
            parse_error=None,
        )

    @staticmethod
    def _guess_surface(relative_path: str) -> AdapterSurfaceKind:
        if relative_path in {"cli.py", "hermes_cli/main.py"}:
            return AdapterSurfaceKind.CLI
        if relative_path == "run_agent.py":
            return AdapterSurfaceKind.RUNTIME_LOOP
        if relative_path.startswith("providers/"):
            return AdapterSurfaceKind.PROVIDER
        if relative_path == "tools/registry.py":
            return AdapterSurfaceKind.TOOL_REGISTRY
        if relative_path in {"model_tools.py", "toolsets.py"}:
            return AdapterSurfaceKind.TOOL_ORCHESTRATION
        if relative_path.startswith("agent/memory") or relative_path == "tools/memory_tool.py":
            return AdapterSurfaceKind.MEMORY
        if relative_path in {"agent/system_prompt.py", "agent/prompt_builder.py"}:
            return AdapterSurfaceKind.PROMPT
        if relative_path == "agent/context_compressor.py":
            return AdapterSurfaceKind.CONTEXT
        if relative_path == "hermes_state.py":
            return AdapterSurfaceKind.STATE_DB
        if relative_path.startswith("gateway/"):
            return AdapterSurfaceKind.GATEWAY
        if relative_path.startswith("cron/"):
            return AdapterSurfaceKind.CRON
        if relative_path.startswith("tools/threat_patterns") or relative_path == "agent/redact.py":
            return AdapterSurfaceKind.SECURITY
        return AdapterSurfaceKind.UNKNOWN


class _ASTRecordVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.imports: list[PythonImportRecord] = []
        self.symbols: list[PythonSymbolRecord] = []
        self.calls: list[PythonCallRecord] = []
        self._scope: list[str] = []

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.imports.append(
                PythonImportRecord(
                    module=alias.name,
                    alias=alias.asname,
                    line=getattr(node, "lineno", 0),
                )
            )
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        module = node.module or ""
        if node.level:
            module = "." * node.level + module
        for alias in node.names:
            self.imports.append(
                PythonImportRecord(
                    module=module or ".",
                    name=alias.name,
                    alias=alias.asname,
                    line=getattr(node, "lineno", 0),
                )
            )
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        qualname = ".".join([*self._scope, node.name])
        self.symbols.append(
            PythonSymbolRecord(
                kind="class",
                name=node.name,
                qualname=qualname,
                line=getattr(node, "lineno", 0),
            )
        )
        self._scope.append(node.name)
        self.generic_visit(node)
        self._scope.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function(node, kind="function")

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node, kind="async_function")

    def visit_Call(self, node: ast.Call) -> None:
        name = self._call_name(node.func)
        if name:
            self.calls.append(
                PythonCallRecord(
                    name=name,
                    line=getattr(node, "lineno", 0),
                )
            )
        self.generic_visit(node)

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef, *, kind: str) -> None:
        qualname = ".".join([*self._scope, node.name])
        self.symbols.append(
            PythonSymbolRecord(
                kind=kind,
                name=node.name,
                qualname=qualname,
                line=getattr(node, "lineno", 0),
            )
        )
        self._scope.append(node.name)
        self.generic_visit(node)
        self._scope.pop()

    def _call_name(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Name):
            return node.id

        if isinstance(node, ast.Attribute):
            prefix = self._call_name(node.value)
            if prefix:
                return f"{prefix}.{node.attr}"
            return node.attr

        return None