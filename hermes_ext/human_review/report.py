"""Report rendering for Phase 13 human review."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from hermes_ext.human_review.contracts import (
    ColdStartValidationPlan,
    HumanReviewBundle,
    HumanReviewDossier,
    MergeDecisionReport,
    NativeExperimentProposal,
    stable_json_dumps,
)


class HumanReviewReporter:
    """Write markdown and JSON reports for Phase 13."""

    def __init__(self, output_dir: str | Path) -> None:
        self.output_dir = Path(output_dir)

    def write_all(
        self,
        dossier: HumanReviewDossier,
        cold_start_plan: ColdStartValidationPlan,
        native_experiment_proposal: NativeExperimentProposal,
        merge_decision_report: MergeDecisionReport,
    ) -> HumanReviewBundle:
        self.output_dir.mkdir(parents=True, exist_ok=True)

        output_paths: list[str] = []

        output_paths.append(
            self._write_text("human_review_dossier.md", self._dossier_md(dossier))
        )
        output_paths.append(
            self._write_json("human_review_dossier.json", dossier.model_dump(mode="json"))
        )

        output_paths.append(
            self._write_text(
                "merge_decision_report.md",
                self._merge_decision_md(merge_decision_report),
            )
        )
        output_paths.append(
            self._write_json(
                "merge_decision_report.json",
                merge_decision_report.model_dump(mode="json"),
            )
        )

        output_paths.append(
            self._write_text(
                "cold_start_validation_plan.md",
                self._cold_start_plan_md(cold_start_plan),
            )
        )
        output_paths.append(
            self._write_json(
                "cold_start_validation_plan.json",
                cold_start_plan.model_dump(mode="json"),
            )
        )

        output_paths.append(
            self._write_text(
                "native_experiment_proposal.md",
                self._native_experiment_proposal_md(native_experiment_proposal),
            )
        )
        output_paths.append(
            self._write_json(
                "native_experiment_proposal.json",
                native_experiment_proposal.model_dump(mode="json"),
            )
        )

        output_paths.append(
            self._write_text(
                "review_board_checklist.md",
                self._review_board_checklist_md(),
            )
        )
        output_paths.append(
            self._write_text(
                "phase13_execution_log.md",
                self._execution_log_md(merge_decision_report),
            )
        )
        output_paths.append(
            self._write_text(
                "phase13_exit_checklist.md",
                self._exit_checklist_md(merge_decision_report),
            )
        )
        output_paths.append(
            self._write_text_if_missing(
                "phase13_test_result.md",
                self._test_result_placeholder(),
            )
        )

        bundle = HumanReviewBundle(
            bundle_id=dossier.dossier_id,
            dossier=dossier.model_dump(mode="json"),
            cold_start_validation_plan=cold_start_plan.model_dump(mode="json"),
            native_experiment_proposal=native_experiment_proposal.model_dump(mode="json"),
            merge_decision_report=merge_decision_report.model_dump(mode="json"),
            output_artifacts=tuple(output_paths + [str(self.output_dir / "phase13_review_bundle.json")]),
        )

        self._write_json("phase13_review_bundle.json", bundle.model_dump(mode="json"))

        return bundle

    def _write_text(self, filename: str, content: str) -> str:
        path = self.output_dir / filename
        path.write_text(content.strip() + "\n", encoding="utf-8")
        return str(path)

    def _write_text_if_missing(self, filename: str, content: str) -> str:
        path = self.output_dir / filename
        if not path.exists():
            path.write_text(content.strip() + "\n", encoding="utf-8")
        return str(path)

    def _write_json(self, filename: str, payload: dict[str, Any]) -> str:
        path = self.output_dir / filename
        path.write_text(stable_json_dumps(payload) + "\n", encoding="utf-8")
        return str(path)

    def _dossier_md(self, dossier: HumanReviewDossier) -> str:
        lines = [
            "# Phase 13 Human Review Dossier",
            "",
            f"- dossier_id: `{dossier.dossier_id}`",
            f"- phase: `{dossier.phase}`",
            f"- dossier_hash: `{dossier.dossier_hash}`",
            "",
            "## Source Evidence",
            "",
        ]
        lines.extend(f"- `{path}`" for path in dossier.source_evidence)

        title_map = {
            "executive_summary": "Executive Summary",
            "scope": "Scope",
            "architecture_review": "Architecture Review",
            "risk_register": "Risk Register",
            "acceptance_criteria": "Acceptance Criteria",
            "review_questions": "Review Questions",
            "next_phase_policy": "Next Phase Policy",
        }

        for key, title in title_map.items():
            lines.extend(["", f"## {title}", "", dossier.sections[key]])

        return "\n".join(lines)

    def _merge_decision_md(self, report: MergeDecisionReport) -> str:
        lines = [
            "# Phase 13 Merge Decision Report",
            "",
            f"- report_id: `{report.report_id}`",
            f"- phase: `{report.phase}`",
            f"- decision: `{report.decision.value}`",
            f"- reviewer: `{report.reviewer or 'n/a'}`",
            f"- ok: `{str(report.ok).lower()}`",
            f"- review_ready: `{str(report.review_ready).lower()}`",
            f"- decision_allowed: `{str(report.decision_allowed).lower()}`",
            f"- report_hash: `{report.report_hash}`",
            "",
            "## Required Acknowledgements",
            "",
        ]

        if report.required_acknowledgements:
            lines.extend(f"- `{ack}`" for ack in report.required_acknowledgements)
        else:
            lines.append("- none")

        lines.extend(["", "## Missing Acknowledgements", ""])

        if report.missing_acknowledgements:
            lines.extend(f"- `{ack}`" for ack in report.missing_acknowledgements)
        else:
            lines.append("- none")

        lines.extend(
            [
                "",
                "## Findings",
                "",
                "| ID | Status | Severity | Message |",
                "|---|---|---|---|",
            ]
        )

        for finding in report.findings:
            message = finding.message.replace("|", "\\|")
            lines.append(
                f"| `{finding.id}` | `{finding.status}` | `{finding.severity}` | {message} |"
            )

        lines.extend(["", "## Blocking Failures", ""])

        if report.blocking_failures:
            lines.extend(f"- `{item}`" for item in report.blocking_failures)
        else:
            lines.append("- none")

        lines.extend(["", "## Recommendations", ""])
        lines.extend(f"- {item}" for item in report.recommendations)

        lines.extend(
            [
                "",
                "## Interpretation",
                "",
                "- `ok=true` means the Phase 13 review packet and selected decision state are valid.",
                "- It does not approve Hermes native integration.",
                "- It does not authorize native adapter implementation.",
                "- Any native experiment must start in a separate explicitly approved phase.",
            ]
        )

        return "\n".join(lines)

    def _cold_start_plan_md(self, plan: ColdStartValidationPlan) -> str:
        lines = [
            "# Phase 13 Cold Start Validation Plan",
            "",
            f"- plan_id: `{plan.plan_id}`",
            f"- phase: `{plan.phase}`",
            f"- plan_hash: `{plan.plan_hash}`",
            "",
            "## Objective",
            "",
            plan.objective,
            "",
            "## Steps",
            "",
        ]
        lines.extend(f"{index}. {step}" for index, step in enumerate(plan.steps, start=1))

        lines.extend(["", "## Pass Criteria", ""])
        lines.extend(f"- {item}" for item in plan.pass_criteria)

        lines.extend(["", "## Forbidden Actions", ""])
        lines.extend(f"- {item}" for item in plan.forbidden_actions)

        return "\n".join(lines)

    def _native_experiment_proposal_md(
        self,
        proposal: NativeExperimentProposal,
    ) -> str:
        lines = [
            "# Phase 13 Native Experiment Proposal",
            "",
            f"- proposal_id: `{proposal.proposal_id}`",
            f"- phase: `{proposal.phase}`",
            f"- candidate_next_phase: `{proposal.candidate_next_phase}`",
            f"- status: `{proposal.status}`",
            f"- proposal_hash: `{proposal.proposal_hash}`",
            "",
            "## Objective",
            "",
            proposal.objective,
            "",
            "## Allowed Work",
            "",
        ]
        lines.extend(f"- {item}" for item in proposal.allowed_work)

        lines.extend(["", "## Forbidden Work", ""])
        lines.extend(f"- {item}" for item in proposal.forbidden_work)

        lines.extend(["", "## Required Preconditions", ""])
        lines.extend(f"- {item}" for item in proposal.required_preconditions)

        lines.extend(["", "## Rollback Requirements", ""])
        lines.extend(f"- {item}" for item in proposal.rollback_requirements)

        lines.extend(
            [
                "",
                "## Non-negotiable Interpretation",
                "",
                "This proposal is document-only and not approved. It must not be used as permission to implement native adapter code.",
            ]
        )

        return "\n".join(lines)

    def _review_board_checklist_md(self) -> str:
        return "\n".join(
            [
                "# Phase 13 Review Board Checklist",
                "",
                "- [ ] Phase 12 evidence reviewed.",
                "- [ ] Phase 12 merge readiness report reviewed.",
                "- [ ] Phase 12 test result reviewed.",
                "- [ ] Phase 12 no-touch constraints reviewed.",
                "- [ ] Rollback evidence reviewed.",
                "- [ ] Maintenance guide reviewed.",
                "- [ ] Shadow-only merge scope accepted or rejected.",
                "- [ ] Native integration explicitly marked not approved.",
                "- [ ] Native experiment proposal treated as document-only.",
                "- [ ] Final decision recorded with reviewer identity if non-pending.",
            ]
        )

    def _execution_log_md(self, report: MergeDecisionReport) -> str:
        return "\n".join(
            [
                "# Phase 13 Execution Log",
                "",
                "- phase: `13`",
                "- name: `Human Review / Merge Decision / Native Experiment Proposal`",
                f"- decision: `{report.decision.value}`",
                f"- ok: `{str(report.ok).lower()}`",
                f"- review_ready: `{str(report.review_ready).lower()}`",
                f"- decision_allowed: `{str(report.decision_allowed).lower()}`",
                "",
                "## Actions",
                "",
                "- Loaded Phase 12 evidence.",
                "- Generated human review dossier.",
                "- Generated cold-start validation plan.",
                "- Generated native experiment proposal.",
                "- Generated merge decision report.",
                "- Generated review board checklist.",
                "- Generated Phase 13 review bundle.",
                "",
                "## Boundary",
                "",
                "- No Hermes native code was modified.",
                "- No native adapter was implemented.",
                "- No provider/model/tool was called.",
                "- No native memory was written.",
                "- No patch was generated.",
            ]
        )

    def _exit_checklist_md(self, report: MergeDecisionReport) -> str:
        status = "PASS" if report.ok else "FAIL"
        return "\n".join(
            [
                "# Phase 13 Exit Checklist",
                "",
                f"- decision gate: `{status}`",
                "- human review dossier generated: `PASS`",
                "- merge decision report generated: `PASS`",
                "- cold-start validation plan generated: `PASS`",
                "- native experiment proposal generated: `PASS`",
                "- review board checklist generated: `PASS`",
                "- native experiment status: `document_only_not_approved`",
                "- Hermes native lifeline modifications: `0 expected`",
                "- native adapter work: `not performed`",
                "- real provider/model/tool use: `not performed`",
                "- native memory write: `not performed`",
                "",
                "Phase 13 may be committed only if external verification commands pass.",
            ]
        )

    def _test_result_placeholder(self) -> str:
        return "\n".join(
            [
                "# Phase 13 Test Result",
                "",
                "This file is preserved if a real pytest capture already exists.",
                "",
                "Recommended capture command:",
                "",
                "```bash",
                ".venv\\Scripts\\python -m pytest tests\\hermes_ext -q",
                "```",
            ]
        )