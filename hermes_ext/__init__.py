"""
Hermes extension layer.

Phase 1 rule:
- This package must not import Hermes core modules.
- This package must be deletable without breaking Hermes.
- This package must not read API keys, .env files, or provider config.
"""

from __future__ import annotations

__all__ = ["__version__"]

__version__ = "0.1.0-phase1"