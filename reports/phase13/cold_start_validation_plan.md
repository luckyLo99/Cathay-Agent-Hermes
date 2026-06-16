# Phase 13 Cold Start Validation Plan

- plan_id: `7919b9ee-da2a-4eb6-accd-ae0cd21087d8`
- phase: `13`
- plan_hash: `1b11c6b3e1d3d3b6abbb3974ab398df16650aa26bed6ac635b3703881703e96a`

## Objective

Reproduce the Phase 12 evidence from a clean checkout before any human merge decision is treated as valid.

## Steps

1. Checkout tag phase12-final-stabilization-merge-readiness.
2. Create or reuse the isolated Python virtual environment.
3. Run py_compile for hermes_ext source files.
4. Run pytest tests/hermes_ext -q.
5. Run hermes_ext.runtime.agent_doctor.
6. Run hermes_ext.harness.cli doctor with all flags disabled.
7. Run hermes_ext.finalization.cli to regenerate Phase 12 evidence.
8. Run hermes_ext.human_review.cli to regenerate Phase 13 reports.
9. Run cli.py --help.
10. Run hermes doctor.
11. Inspect git diff --stat and git status --short.

## Pass Criteria

- All hermes_ext tests pass.
- Phase 12 merge readiness remains ok=true.
- Phase 13 merge decision report remains ok=true for pending review.
- No Hermes lifeline files appear in git diff.
- No provider, tool, native memory, state, secret, or patch side effect occurs.

## Forbidden Actions

- Do not modify Hermes CLI or main loop.
- Do not modify pyproject.toml or lock files.
- Do not install new dependencies.
- Do not call real providers or models.
- Do not execute real tools.
- Do not write Hermes native memory.
- Do not generate native adapter code.
