"""
No-op native boundary contract layer.

Phase 9 rules:
- Do not import Hermes core modules.
- Do not execute real tools.
- Do not call real providers or models.
- Do not write Hermes native memory.
- Do not mutate Hermes state.
- Do not generate patches.
"""

from __future__ import annotations

from hermes_ext.native_boundary.adapters import (
    NoopGatewayBoundaryAdapter,
    NoopMemoryBoundaryAdapter,
    NoopProviderBoundaryAdapter,
    NoopStateBoundaryAdapter,
    NoopToolBoundaryAdapter,
)
from hermes_ext.native_boundary.contract_suite import NoopNativeBoundaryContractSuite
from hermes_ext.native_boundary.contracts import (
    NativeBoundaryKind,
    NativeBoundaryOperation,
    NativeBoundaryRequest,
    NativeBoundaryResult,
    NativeBoundaryVerdict,
)
from hermes_ext.native_boundary.noop_boundary import NoopNativeBoundary

__all__ = [
    "NativeBoundaryKind",
    "NativeBoundaryOperation",
    "NativeBoundaryRequest",
    "NativeBoundaryResult",
    "NativeBoundaryVerdict",
    "NoopGatewayBoundaryAdapter",
    "NoopMemoryBoundaryAdapter",
    "NoopNativeBoundary",
    "NoopNativeBoundaryContractSuite",
    "NoopProviderBoundaryAdapter",
    "NoopStateBoundaryAdapter",
    "NoopToolBoundaryAdapter",
]