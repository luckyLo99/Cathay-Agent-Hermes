from __future__ import annotations

from pathlib import Path

from hermes_ext.runtime.agent_doctor import AgentDoctor, CheckStatus, main


def test_agent_doctor_runs_offline() -> None:
    report = AgentDoctor(Path.cwd()).run_all()

    check_names = {check.name for check in report.checks}

    assert "python_version" in check_names
    assert "extension_layout" in check_names
    assert "api_key_independence" in check_names
    assert "mock_provider" in check_names
    assert "portable_schema" in check_names
    assert "git_status" in check_names
    assert all(check.status != CheckStatus.FAIL for check in report.checks)


def test_agent_doctor_json_cli() -> None:
    exit_code = main(["--json", "--project-root", "."])

    assert exit_code in {0, 1}