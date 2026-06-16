from __future__ import annotations

import ast
from pathlib import Path


def test_cathay_adapter_does_not_import_cathay_agent() -> None:
    root = Path("hermes_ext/cathay")
    forbidden_prefixes = {
        "cathay_agent",
        "Cathay-Agent",
        "memoryx",
    }

    for path in root.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    assert not any(
                        alias.name.startswith(prefix) for prefix in forbidden_prefixes
                    ), f"{path} imports forbidden module {alias.name}"

            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                assert not any(
                    module.startswith(prefix) for prefix in forbidden_prefixes
                ), f"{path} imports forbidden module {module}"