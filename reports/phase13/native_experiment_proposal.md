# Phase 13 Native Experiment Proposal

- proposal_id: `bc9a0da3-ceda-4c08-9bd8-25472545aace`
- phase: `13`
- candidate_next_phase: `Phase 14: No-op-first Native Experiment Design`
- status: `document_only_not_approved`
- proposal_hash: `686f1411d2bb03065ca0741d24a5737d91817db8f84596402e816e4590ef4e17`

## Objective

Describe what a future native experiment phase would need to prove before any Hermes native boundary could be reconsidered.

## Allowed Work

- Write design documents only.
- Define candidate native experiment scope.
- Define no-op-first test requirements.
- Define rollback and kill-switch requirements.
- Define human approval requirements for a later phase.

## Forbidden Work

- Do not implement native adapter code.
- Do not modify Hermes native lifeline files.
- Do not call native providers or model SDKs.
- Do not execute real tools.
- Do not write Hermes native memory.
- Do not write Hermes skills.
- Do not modify state databases.
- Do not generate patches against Hermes core.

## Required Preconditions

- Phase 13 human review must explicitly approve shadow merge or request changes.
- A separate future phase must explicitly authorize native experiment design.
- The future phase must start from no-op-first contracts.
- The future phase must include rollback and exit criteria before code.
- The future phase must preserve feature flags default-off and kill-switch dominance.

## Rollback Requirements

- Primary rollback anchor remains phase12-final-stabilization-merge-readiness.
- Previous rollback anchor remains phase11-shadow-assembly-manifest.
- No rollback step may partially delete Hermes native files.
- Any future experimental files must be deletable without affecting Hermes runtime.

## Non-negotiable Interpretation

This proposal is document-only and not approved. It must not be used as permission to implement native adapter code.
