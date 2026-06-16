"""
Read-only Hermes adapter scan.

Phase 7 rules:
- Do not import Hermes core modules.
- Do not execute Hermes code.
- Do not modify scanned files.
- Do not read .env or API keys.
- Produce adapter maps only.
"""

from __future__ import annotations

from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterScanConfig,
    AdapterScanReport,
    AdapterSurfaceKind,
    ExtensionPointCandidate,
    RiskLevel,
    SourceFileRecord,
)
from hermes_ext.adapter_scan.scanner import AdapterScanEngine

__all__ = [
    "AdapterIntegrationPosture",
    "AdapterScanConfig",
    "AdapterScanEngine",
    "AdapterScanReport",
    "AdapterSurfaceKind",
    "ExtensionPointCandidate",
    "RiskLevel",
    "SourceFileRecord",
]