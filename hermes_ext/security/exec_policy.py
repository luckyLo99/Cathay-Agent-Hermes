from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from hermes_ext.security.decisions import SecurityDecision


class ExecPolicyDecision(str, Enum):
    ALLOW = "allow"
    ASK = "ask"
    DENY = "deny"


PatternToken = str | list[str]


class ExecPolicyRule(BaseModel):
    """
    Minimal prefix rule.

    Examples:
      pattern=["python", ["--version", "-V"]], decision="allow"
      pattern=["git", "status"], decision="allow"
      pattern=["rm", "-rf"], decision="deny"
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    rule_id: str = Field(min_length=1)
    pattern: list[PatternToken] = Field(min_length=1)
    decision: ExecPolicyDecision
    reason: str = Field(min_length=1)

    @field_validator("pattern")
    @classmethod
    def validate_pattern(cls, value: list[PatternToken]) -> list[PatternToken]:
        for token in value:
            if isinstance(token, str):
                if not token.strip():
                    raise ValueError("pattern token must not be empty")
            elif isinstance(token, list):
                if not token:
                    raise ValueError("pattern alt list must not be empty")
                for alt in token:
                    if not isinstance(alt, str) or not alt.strip():
                        raise ValueError("pattern alt must be non-empty string")
            else:
                raise ValueError("pattern token must be str or list[str]")
        return value

    def matches(self, argv: list[str]) -> bool:
        if len(argv) < len(self.pattern):
            return False

        for index, expected in enumerate(self.pattern):
            actual = argv[index]
            if isinstance(expected, str):
                if actual != expected:
                    return False
            else:
                if actual not in expected:
                    return False

        return True


class ExecPolicy(BaseModel):
    """
    Small deterministic exec policy.

    Default posture:
    - known safe read-only commands allowed
    - known dangerous commands denied
    - package managers, git mutation, docker, network tools ask
    - unknown commands ask
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    rules: list[ExecPolicyRule] = Field(default_factory=list)
    unknown_decision: ExecPolicyDecision = ExecPolicyDecision.ASK

    @classmethod
    def default(cls) -> "ExecPolicy":
        return cls(
            rules=[
                ExecPolicyRule(
                    rule_id="allow.python.version",
                    pattern=["python", ["--version", "-V"]],
                    decision=ExecPolicyDecision.ALLOW,
                    reason="Python version check is read-only",
                ),
                ExecPolicyRule(
                    rule_id="allow.pytest.collect",
                    pattern=["python", "-m", "pytest"],
                    decision=ExecPolicyDecision.ASK,
                    reason="Pytest may execute project code; approval required in Phase 2",
                ),
                ExecPolicyRule(
                    rule_id="allow.git.status",
                    pattern=["git", "status"],
                    decision=ExecPolicyDecision.ALLOW,
                    reason="git status is read-only",
                ),
                ExecPolicyRule(
                    rule_id="allow.git.diff",
                    pattern=["git", "diff"],
                    decision=ExecPolicyDecision.ALLOW,
                    reason="git diff is read-only",
                ),
                ExecPolicyRule(
                    rule_id="allow.git.branch",
                    pattern=["git", "branch"],
                    decision=ExecPolicyDecision.ALLOW,
                    reason="git branch inspection is read-only by default",
                ),
                ExecPolicyRule(
                    rule_id="ask.git.add",
                    pattern=["git", "add"],
                    decision=ExecPolicyDecision.ASK,
                    reason="git add stages changes",
                ),
                ExecPolicyRule(
                    rule_id="ask.git.commit",
                    pattern=["git", "commit"],
                    decision=ExecPolicyDecision.ASK,
                    reason="git commit mutates repository history",
                ),
                ExecPolicyRule(
                    rule_id="deny.git.force_push",
                    pattern=["git", "push", "--force"],
                    decision=ExecPolicyDecision.DENY,
                    reason="force push is forbidden",
                ),
                ExecPolicyRule(
                    rule_id="deny.rm.rf",
                    pattern=["rm", "-rf"],
                    decision=ExecPolicyDecision.DENY,
                    reason="recursive force delete is forbidden",
                ),
                ExecPolicyRule(
                    rule_id="deny.powershell.remove_item.force",
                    pattern=["Remove-Item"],
                    decision=ExecPolicyDecision.ASK,
                    reason="PowerShell Remove-Item requires approval",
                ),
                ExecPolicyRule(
                    rule_id="ask.pip.install",
                    pattern=["pip", "install"],
                    decision=ExecPolicyDecision.ASK,
                    reason="dependency installation requires approval",
                ),
                ExecPolicyRule(
                    rule_id="ask.python.pip.install",
                    pattern=["python", "-m", "pip", "install"],
                    decision=ExecPolicyDecision.ASK,
                    reason="dependency installation requires approval",
                ),
                ExecPolicyRule(
                    rule_id="ask.curl",
                    pattern=["curl"],
                    decision=ExecPolicyDecision.ASK,
                    reason="network fetch requires approval",
                ),
                ExecPolicyRule(
                    rule_id="ask.wget",
                    pattern=["wget"],
                    decision=ExecPolicyDecision.ASK,
                    reason="network fetch requires approval",
                ),
            ]
        )

    def evaluate(self, argv: list[str]) -> SecurityDecision:
        if not argv:
            return SecurityDecision.deny("Command argv is empty", rule_id="exec.empty")

        for rule in self.rules:
            if rule.matches(argv):
                return self._to_security_decision(rule)

        if self.unknown_decision == ExecPolicyDecision.ALLOW:
            return SecurityDecision.allow("Unknown command allowed by policy", rule_id="exec.unknown.allow")

        if self.unknown_decision == ExecPolicyDecision.DENY:
            return SecurityDecision.deny("Unknown command denied by policy", rule_id="exec.unknown.deny")

        return SecurityDecision.ask("Unknown command requires approval", rule_id="exec.unknown.ask")

    @staticmethod
    def _to_security_decision(rule: ExecPolicyRule) -> SecurityDecision:
        if rule.decision == ExecPolicyDecision.ALLOW:
            return SecurityDecision.allow(rule.reason, rule_id=rule.rule_id)

        if rule.decision == ExecPolicyDecision.DENY:
            return SecurityDecision.deny(rule.reason, rule_id=rule.rule_id)

        return SecurityDecision.ask(rule.reason, rule_id=rule.rule_id)