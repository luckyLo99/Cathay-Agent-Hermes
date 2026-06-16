"""
Feature flag integration harness for hermes_ext.

Phase 6 rules:
- Default all extension features OFF.
- Do not modify Hermes core entrypoints.
- Do not read .env.
- Do not call real models.
- Do not execute real tools.
- Do not write Hermes native memory.
"""

from __future__ import annotations

from hermes_ext.harness.contracts import (
    ExtensionFlagName,
    ExtensionHarnessMode,
    FeatureFlagSet,
    HarnessRunRequest,
    HarnessRunResult,
)
from hermes_ext.harness.feature_flags import FeatureFlagResolver
from hermes_ext.harness.integration_harness import IntegrationHarness

__all__ = [
    "ExtensionFlagName",
    "ExtensionHarnessMode",
    "FeatureFlagResolver",
    "FeatureFlagSet",
    "HarnessRunRequest",
    "HarnessRunResult",
    "IntegrationHarness",
]