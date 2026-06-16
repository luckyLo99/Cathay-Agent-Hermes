from __future__ import annotations

import ast
from pathlib import Path


def test_integration_spec_layer_does_not_import_hermes_core_or_patch_tools() -> None:
    root = Path("hermes_ext/integration_spec")
    forbidden_prefixes = {
        "run_agent",
        "cli",
        "hermes_state",
        "hermes_cli",
        "gateway",
        "model_tools",
        "toolsets",
        "tools.registry",
        "tools.memory_tool",
        "agent.memory_provider",
        "agent.memory_manager",
        "agent.system_prompt",
        "providers",
        "memoryx",
        "cathay_agent",
        "dotenv",
        "openai",
        "anthropic",
        "openfeature",
        "pydantic_settings",
    }

    for path in root.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    assert not any(
                        alias.name == prefix or alias.name.startswith(prefix + ".")
                        for prefix in forbidden_prefixes
                    ), f"{path} imports forbidden module {alias.name}"

            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                assert not any(
                    module == prefix or module.startswith(prefix + ".")
                    for prefix in forbidden_prefixes
                ), f"{path} imports forbidden module {module}"