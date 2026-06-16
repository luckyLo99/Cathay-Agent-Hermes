from __future__ import annotations

from collections import defaultdict

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.golden_trace.contracts import (
    GoldenTraceCaseResult,
    GoldenTracePack,
)


class GoldenTraceVerification(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    ok: bool
    stable_cases: int = Field(ge=0)
    unstable_cases: int = Field(ge=0)
    violations: list[str] = Field(default_factory=list)


class GoldenTraceVerifier:
    """
    Verifies that each case has the same canonical hash across iterations.
    """

    def verify(
        self,
        *,
        pack: GoldenTracePack,
        results: list[GoldenTraceCaseResult],
    ) -> GoldenTraceVerification:
        grouped: dict[str, list[GoldenTraceCaseResult]] = defaultdict(list)
        for result in results:
            grouped[result.case_id].append(result)

        violations: list[str] = []
        stable_cases = 0
        unstable_cases = 0

        for case in pack.cases:
            case_results = grouped.get(case.case_id, [])
            if not case_results:
                violations.append(f"{case.case_id}: missing results")
                unstable_cases += 1
                continue

            hashes = {result.canonical_hash for result in case_results}
            if len(hashes) == 1 and all(result.ok for result in case_results):
                stable_cases += 1
            else:
                unstable_cases += 1
                violations.append(
                    f"{case.case_id}: unstable hash or failed result; hashes={sorted(hashes)}"
                )

        return GoldenTraceVerification(
            ok=not violations,
            stable_cases=stable_cases,
            unstable_cases=unstable_cases,
            violations=violations,
        )