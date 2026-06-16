# Phase 12 Maintenance Guide

Maintenance rules after Phase 12:

1. Any new hermes_ext module must include a no-import test.
2. Any runnable behavior must be gated by HERMES_EXT_ENABLED and kill-switch compatible.
3. Any tool-shaped behavior must pass through PreToolGuard.
4. Any memory-shaped behavior must remain shadow-only unless a later explicit phase approves native integration.
5. Any new trace-sensitive behavior must add or update golden trace cases.
6. Any new report-producing module must include markdown and JSON output.
7. Any future native boundary must remain no-op by default.
8. Any attempt to touch Hermes lifeline files requires a new phase, explicit approval, and a rollback plan.

## Rule

Maintenance is allowed only inside hermes_ext unless a later phase explicitly approves native integration.