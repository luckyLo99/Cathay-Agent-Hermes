from __future__ import annotations

from hermes_ext.security.decisions import SecurityDecisionType
from hermes_ext.security.exec_policy import ExecPolicy, ExecPolicyDecision, ExecPolicyRule


def test_exec_policy_allows_git_status() -> None:
    decision = ExecPolicy.default().evaluate(["git", "status"])

    assert decision.decision == SecurityDecisionType.ALLOW


def test_exec_policy_denies_git_force_push() -> None:
    decision = ExecPolicy.default().evaluate(["git", "push", "--force"])

    assert decision.decision == SecurityDecisionType.DENY


def test_exec_policy_asks_unknown_command() -> None:
    decision = ExecPolicy.default().evaluate(["some-unknown-command"])

    assert decision.decision == SecurityDecisionType.ASK


def test_exec_policy_supports_alternatives() -> None:
    policy = ExecPolicy(
        rules=[
            ExecPolicyRule(
                rule_id="python.version",
                pattern=["python", ["--version", "-V"]],
                decision=ExecPolicyDecision.ALLOW,
                reason="version check",
            )
        ]
    )

    assert policy.evaluate(["python", "--version"]).decision == SecurityDecisionType.ALLOW
    assert policy.evaluate(["python", "-V"]).decision == SecurityDecisionType.ALLOW


def test_exec_policy_empty_argv_denied() -> None:
    decision = ExecPolicy.default().evaluate([])

    assert decision.decision == SecurityDecisionType.DENY