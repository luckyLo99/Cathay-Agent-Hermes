from __future__ import annotations

from hermes_ext.security.command_guard import CommandGuard
from hermes_ext.security.decisions import SecurityDecisionType


def test_command_guard_allows_simple_python_version_shape() -> None:
    decision = CommandGuard().evaluate_argv(["python", "--version"])

    assert decision.decision == SecurityDecisionType.ALLOW


def test_command_guard_denies_rm_rf_root() -> None:
    decision = CommandGuard().evaluate_argv(["rm", "-rf", "/"])

    assert decision.decision == SecurityDecisionType.DENY


def test_command_guard_asks_for_shell_metacharacter() -> None:
    decision = CommandGuard().evaluate_argv(["echo", "hello", "&&", "whoami"])

    assert decision.decision == SecurityDecisionType.ASK


def test_command_guard_asks_for_pip() -> None:
    decision = CommandGuard().evaluate_argv(["pip", "install", "x"])

    assert decision.decision == SecurityDecisionType.ASK


def test_command_guard_denies_null_byte() -> None:
    decision = CommandGuard().evaluate_argv(["python\x00", "--version"])

    assert decision.decision == SecurityDecisionType.DENY