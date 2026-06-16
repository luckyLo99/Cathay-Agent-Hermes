# Final Stabilization Documentation Pack

- pack_id: `93466d38-b439-4740-b837-d55c2e1cf6e0`
- phase: `12`
- pack_hash: `ea133a600350c2352db69f528d633ca661735d2335c72ddda37f64e7f3b00406`
- created_at: `2026-06-16T09:02:00.373874+00:00`

## Evidence Paths

- `reports/phase11/shadow_assembly_manifest.json`
- `reports/phase11/release_gate_report.json`
- `reports/phase11/phase11_test_result.md`
- `reports/phase11/phase11_exit_checklist.md`
- `reports/phase11/phase11_execution_log.md`
- `reports/phase10/golden_trace_replay_report.json`
- `reports/phase9/native_boundary_contract_report.json`

## Executive Summary

Phase 12 finalization packages the hermes_ext shadow architecture for merge-readiness review. It does not approve Hermes native integration and does not patch Hermes core.

- Phase 11 release gate ok: `True`
- Assembly manifest hash: `da522fc95449850a4efca58a94f0ac5dfdecdf091377d960913503d6c94a553f`
- Test evidence contains 241/241 PASS: `True`

## Architecture Summary

The shadow architecture remains isolated under hermes_ext:

- runtime: request envelope, mock provider, agent doctor.
- schema: portable schema validation.
- hooks/security: hook dispatcher, PreToolGuard, path/url/command/exec policies.
- cathay: read-only signal adapter.
- memoryx: isolated shadow memory provider.
- orchestration: checkpoint, replay, span log, circuit breaker.
- harness: feature flags and explicit integration harness.
- adapter_scan: read-only Hermes adapter mapping.
- integration_spec: zero-touch integration design matrix.
- native_boundary: no-op / blocked native boundary contract.
- golden_trace: deterministic replay pack.
- assembly: release-style manifest and invariant gate.
- finalization: documentation pack, merge readiness gate, stabilization bundle.

## Safety Invariants

The following Phase 11 assembly invariants are treated as non-negotiable release gates:

- `assembly.artifacts_exist` -> `pass` / `info`
- `assembly.no_lifeline_source_artifacts` -> `pass` / `critical`
- `assembly.feature_flags_default_disabled` -> `pass` / `critical`
- `assembly.no_forbidden_imports` -> `pass` / `critical`
- `assembly.phase10_golden_trace_stable` -> `pass` / `critical`
- `assembly.phase9_native_boundary_no_side_effects` -> `pass` / `critical`

If any critical invariant fails, Phase 12 must not be treated as merge-ready.

## Operator Commands

Recommended final verification commands:

```bash
.venv\Scripts\python -m pytest tests\hermes_ext -q
.venv\Scripts\python -m hermes_ext.runtime.agent_doctor --json --project-root .
.venv\Scripts\python -m hermes_ext.harness.cli doctor --project-root . --state-dir .hermes_ext_shadow --json
.venv\Scripts\python -m hermes_ext.assembly.cli \
  --project-root . \
  --manifest-md reports\phase11\shadow_assembly_manifest.md \
  --manifest-json reports\phase11\shadow_assembly_manifest.json \
  --gate-md reports\phase11\release_gate_report.md \
  --gate-json reports\phase11\release_gate_report.json
.venv\Scripts\python -m hermes_ext.finalization.cli \
  --project-root . \
  --output-dir reports\phase12
.venv\Scripts\python cli.py --help
.venv\Scripts\hermes doctor
```

## Rollback Index

Rollback anchors:

- Phase 11 rollback: `git reset --hard phase10-golden-trace-replay`
- Phase 10 rollback: `git reset --hard phase9-noop-native-boundary-contracts`
- Phase 9 rollback: `git reset --hard phase8-zero-touch-integration-spec`
- Phase 8 rollback: `git reset --hard phase7-readonly-adapter-scan`
- Phase 7 rollback: `git reset --hard phase6-feature-flag-harness`
- Phase 6 rollback: `git reset --hard phase5-shadow-orchestration-replay`
- Phase 5 rollback: `git reset --hard phase4-memoryx-shadow-provider`
- Phase 4 rollback: `git reset --hard phase3-cathay-readonly-adapter`
- Phase 3 rollback: `git reset --hard phase2-hook-pretool-policy`
- Phase 2 rollback: `git reset --hard phase1-offline-runtime-skeleton`
- Phase 1 rollback: `git reset --hard baseline-before-fusion`

## Merge Readiness Notes

Merge readiness is limited to hermes_ext shadow extension artifacts.

Merge-ready means:

- tests pass;
- release gate passes;
- no critical invariant fails;
- golden traces are stable;
- no-op native boundary remains side-effect free;
- feature flags are disabled by default;
- Hermes native files remain untouched.

Merge-ready does not mean:

- Hermes core integration is approved;
- native providers may be called;
- tools may execute;
- native memory may be written;
- prompt/state/runtime files may be patched.

## Maintenance Guide

Maintenance rules after Phase 12:

1. Any new hermes_ext module must include a no-import test.
2. Any runnable behavior must be gated by HERMES_EXT_ENABLED and kill-switch compatible.
3. Any tool-shaped behavior must pass through PreToolGuard.
4. Any memory-shaped behavior must remain shadow-only unless a later explicit phase approves native integration.
5. Any new trace-sensitive behavior must add or update golden trace cases.
6. Any new report-producing module must include markdown and JSON output.
7. Any future native boundary must remain no-op by default.
8. Any attempt to touch Hermes lifeline files requires a new phase, explicit approval, and a rollback plan.

## Non-negotiable Rule

This documentation pack only describes the hermes_ext shadow extension. It does not approve Hermes native integration.