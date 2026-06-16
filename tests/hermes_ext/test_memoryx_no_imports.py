from __future__ import annotations

import ast
from pathlib import Path


def test_memoryx_shadow_layer_does_not_import_forbidden_projects() -> None:
    root = Path("hermes_ext/memoryx")
    forbidden_prefixes = {
        "memoryx",
        "cathay_agent",
        "Cathay-Agent",
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