"""
Zero-touch integration specification layer.

Phase 8 rules:
- Do not import Hermes core modules.
- Do not generate patches.
- Do not modify Hermes files.
- Consume adapter scan output and produce design-only specs.
"""

from __future__ import annotations

from hermes_ext.integration_spec.contracts import (
    IntegrationDesignMatrix,
    IntegrationMode,
    IntegrationSpecConfig,
    IntegrationSpecStatus,
    IntegrationSurfacePlan,
    ZeroTouchIntegrationSpec,
)
from hermes_ext.integration_spec.spec_builder import IntegrationSpecBuilder

__all__ = [
    "IntegrationDesignMatrix",
    "IntegrationMode",
    "IntegrationSpecBuilder",
    "IntegrationSpecConfig",
    "IntegrationSpecStatus",
    "IntegrationSurfacePlan",
    "ZeroTouchIntegrationSpec",
]