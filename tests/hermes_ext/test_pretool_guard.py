from __future__ import annotations

from pathlib import Path

from hermes_ext.hooks.builtin_hooks import build_default_dispatcher
from hermes_ext.hooks.contracts import HookDecisionType, HookEvent
from hermes_ext.security.decisions import SecurityDecisionType
from hermes_ext.security.pretool_guard import PreToolGuard, PreToolGuardConfig


def make_guard(tmp_path: Path) -> PreToolGuard:
    return PreToolGuard(PreToolGuardConfig(workspace_root=tmp_path))


def test_pretool_guard_allows_safe_python_version(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_tool("bash", {"argv": ["python", "--version"]})

    assert decision.decision == SecurityDecisionType.ALLOW


def test_pretool_guard_denies_dangerous_delete(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_tool("bash", {"argv": ["rm", "-rf", "/"]})

    assert decision.decision == SecurityDecisionType.DENY


def test_pretool_guard_denies_path_escape(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_tool("write_file", {"path": "../escape.txt", "content": "x"})

    assert decision.decision == SecurityDecisionType.DENY


def test_pretool_guard_allows_workspace_write(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_tool(
        "write_file",
        {"path": "reports/phase2/out.md", "content": "ok"},
    )

    assert decision.decision == SecurityDecisionType.ALLOW


def test_pretool_guard_asks_memory_write(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_tool(
        "memory_write",
        {
            "namespace": "phase2",
            "key": "rule",
            "value": "memory writes require approval",
            "confidence": 0.8,
        },
    )

    assert decision.decision == SecurityDecisionType.ASK


def test_pretool_guard_denies_bad_url(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_tool("url_fetch", {"url": "file:///etc/passwd"})

    assert decision.decision == SecurityDecisionType.DENY


def test_pretool_guard_asks_unknown_tool(tmp_path: Path) -> None:
    guard = make_guard(tmp_path)

    decision = guard.evaluate_tool("unknown_tool", {"x": 1})

    assert decision.decision == SecurityDecisionType.ASK


def test_default_dispatcher_runs_pretool_guard() -> None:
    dispatcher = build_default_dispatcher()
    event = HookEvent.pre_tool_use(
        trace_id="trace",
        session_id="session",
        tool_name="bash",
        payload={"argv": ["rm", "-rf", "/"]},
    )

    result = dispatcher.dispatch(event)

    assert result.final_decision == HookDecisionType.DENY
    assert result.blocked