# Golden Trace Replay Report

- report_id: `040d519b-52f1-4630-bd06-384a3c217e73`
- ok: `True`
- repeat: `2`
- case_count: `5`
- result_count: `10`
- passed: `10`
- failed: `0`
- stable_cases: `5`
- unstable_cases: `0`
- report_hash: `b72769094efee7415cfa797b246f7ef0f7d88a95e77a7c3aacf87cbe3314a457`
- created_at: `2026-06-16T07:46:26.658500+00:00`

## Case Hash Stability

| Case | Iterations | Unique Hashes | Stable |
|---|---:|---:|---:|
| `diagnostic-default-off` | 2 | 1 | True |
| `native-boundary-spec-noop` | 2 | 1 | True |
| `shadow-basic-all-enabled` | 2 | 1 | True |
| `shadow-dangerous-tool-blocked` | 2 | 1 | True |
| `shadow-minimal-no-cathay-no-memory` | 2 | 1 | True |

## Violations

- none

## Results

| Case | Iteration | Status | OK | Canonical Hash | Error |
|---|---:|---|---:|---|---|
| `diagnostic-default-off` | 0 | passed | True | `c6cecb06d09bd1b9b08070e63af3775f930c533ba4ccfaef6d63de0acd4ebc0a` | — |
| `shadow-basic-all-enabled` | 0 | passed | True | `125736efaf975f253f440693e30125fda209bc2f1e7e507bc6d0313024c0a883` | — |
| `shadow-dangerous-tool-blocked` | 0 | passed | True | `c3e17d39588e79cbdebf7454229a897ee0f45ffea47d20e97faa83f29d040c8d` | — |
| `shadow-minimal-no-cathay-no-memory` | 0 | passed | True | `484f1d8c6d2e05726c536f226dcb645e1da45a698a6813bd9cea277e971bef60` | — |
| `native-boundary-spec-noop` | 0 | passed | True | `9c33053755f64d7e3019369477fe8c23e692427a6b6a669d1d952a6de46c5fbe` | — |
| `diagnostic-default-off` | 1 | passed | True | `c6cecb06d09bd1b9b08070e63af3775f930c533ba4ccfaef6d63de0acd4ebc0a` | — |
| `shadow-basic-all-enabled` | 1 | passed | True | `125736efaf975f253f440693e30125fda209bc2f1e7e507bc6d0313024c0a883` | — |
| `shadow-dangerous-tool-blocked` | 1 | passed | True | `c3e17d39588e79cbdebf7454229a897ee0f45ffea47d20e97faa83f29d040c8d` | — |
| `shadow-minimal-no-cathay-no-memory` | 1 | passed | True | `484f1d8c6d2e05726c536f226dcb645e1da45a698a6813bd9cea277e971bef60` | — |
| `native-boundary-spec-noop` | 1 | passed | True | `9c33053755f64d7e3019369477fe8c23e692427a6b6a669d1d952a6de46c5fbe` | — |

## Non-negotiable Rule

Passing golden trace replay proves deterministic shadow behavior only. It does not approve Hermes core integration.