# Phase 12 Rollback Index

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

## Rule

Rollback must target the last known safe phase tag and must not partially delete Hermes native files.