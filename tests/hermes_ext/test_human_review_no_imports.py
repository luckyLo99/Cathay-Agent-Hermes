import ast
from pathlib import Path


FORBIDDEN_IMPORT_ROOTS = {
    "cli",
    "run_agent",
    "hermes_cli",
    "gateway",
    "providers",
    "tools",
    "model_tools",
    "toolsets",
    "agent",
    "hermes_state",
    "dotenv",
    "openai",
    "anthropic",
    "google",
    "mistralai",
}

FORBIDDEN_TEXT_MARKERS = {
    "import providers",
    "import gateway",
    "import tools.registry",
    "import tools.memory_tool",
    "import agent.memory_provider",
    "import agent.memory_manager",
    "import hermes_state",
    "import dotenv",
    "from openai",
    "from anthropic",
    "native adapter implementation",
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _human_review_files() -> list[Path]:
    root = _repo_root() / "hermes_ext/human_review"
    return sorted(root.glob("*.py"))


def test_human_review_has_no_forbidden_imports():
    files = _human_review_files()
    assert files

    for path in files:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    root_name = alias.name.split(".")[0]
                    assert root_name not in FORBIDDEN_IMPORT_ROOTS, (path, alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module is None:
                    continue
                root_name = node.module.split(".")[0]
                assert root_name not in FORBIDDEN_IMPORT_ROOTS, (path, node.module)


def test_human_review_source_has_no_forbidden_text_markers():
    files = _human_review_files()
    assert files

    for path in files:
        text = path.read_text(encoding="utf-8").lower()
        for marker in FORBIDDEN_TEXT_MARKERS:
            if marker == "native adapter implementation":
                # Allowed only in explicit forbidden-work or prohibition strings.
                idx = text.find(marker)
                if idx == -1:
                    continue
                context_before = text[max(0, idx - 30):idx]
                assert (
                    "do not" in context_before
                    or "does not" in context_before
                    or "do not implement native adapter" in text
                ), (path, marker)
                continue
            assert marker not in text, (path, marker)