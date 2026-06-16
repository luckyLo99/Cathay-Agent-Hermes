from __future__ import annotations

from pathlib import Path

from hermes_ext.harness.contracts import ExtensionFlagName, FeatureFlagSet, FeatureFlagSource
from hermes_ext.harness.diagnostics import ExtensionDiagnostics


def test_diagnostics_pass_with_default_flags(tmp_path: Path) -> None:
    report = ExtensionDiagnostics(
        project_root=Path.cwd(),
        flags=FeatureFlagSet.default(),
    ).run()

    assert report.ok
    names = {check.name for check in report.checks}
    assert "python_version" in names
    assert "required_modules" in names
    assert "feature_flags" in names


def test_diagnostics_reports_enabled_flags() -> None:
    flags = FeatureFlagSet.default()
    flags = flags.with_value(ExtensionFlagName.ENABLED, True, source=FeatureFlagSource.EXPLICIT, reason="test")
    flags = flags.with_value(ExtensionFlagName.DIAGNOSTICS, True, source=FeatureFlagSource.EXPLICIT, reason="test")

    report = ExtensionDiagnostics(project_root=Path.cwd(), flags=flags).run()

    assert report.ok
    assert any(check.name == "feature_flags" for check in report.checks)