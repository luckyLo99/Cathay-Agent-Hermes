from __future__ import annotations

from pathlib import Path

from hermes_ext.security.decisions import SecurityDecisionType
from hermes_ext.security.path_guard import PathGuard, PathGuardConfig


def make_guard(tmp_path: Path) -> PathGuard:
    return PathGuard(PathGuardConfig(workspace_root=tmp_path))


def test_path_guard_allows_workspace_file(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_write("reports/phase2/out.md")

    assert decision.decision == SecurityDecisionType.ALLOW


def test_path_guard_denies_workspace_escape(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_read("../outside.txt")

    assert decision.decision == SecurityDecisionType.DENY
    assert decision.rule_id == "path.workspace_escape"


def test_path_guard_denies_env_file(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_read(".env")

    assert decision.decision == SecurityDecisionType.DENY
    assert decision.rule_id == "path.sensitive"


def test_path_guard_denies_ssh_component(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_read(".ssh/id_rsa")

    assert decision.decision == SecurityDecisionType.DENY