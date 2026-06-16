"""CLI for Phase 13 human review reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from hermes_ext.human_review.contracts import HumanReviewDecision
from hermes_ext.human_review.decision_gate import HumanReviewDecisionGate
from hermes_ext.human_review.dossier import (
    ColdStartValidationPlanBuilder,
    HumanReviewDossierBuilder,
)
from hermes_ext.human_review.evidence_loader import HumanReviewEvidenceLoader
from hermes_ext.human_review.experiment_proposal import NativeExperimentProposalBuilder
from hermes_ext.human_review.report import HumanReviewReporter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate Phase 13 human review and merge-decision reports."
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root containing reports/phase12.",
    )
    parser.add_argument(
        "--output-dir",
        default="reports/phase13",
        help="Output directory for Phase 13 reports.",
    )
    parser.add_argument(
        "--decision",
        default=HumanReviewDecision.PENDING.value,
        choices=[decision.value for decision in HumanReviewDecision],
        help="Human review decision state.",
    )
    parser.add_argument(
        "--reviewer",
        default="",
        help="Human reviewer identity. Required for non-pending decisions.",
    )
    parser.add_argument(
        "--ack",
        action="append",
        default=[],
        help="Decision acknowledgement. May be provided multiple times.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable summary.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    project_root = Path(args.project_root)
    output_dir = Path(args.output_dir)

    decision = HumanReviewDecision(args.decision)
    acknowledgements = tuple(args.ack or ())

    evidence = HumanReviewEvidenceLoader(project_root).load()
    dossier = HumanReviewDossierBuilder().build(evidence)
    cold_start_plan = ColdStartValidationPlanBuilder().build()
    native_experiment_proposal = NativeExperimentProposalBuilder().build()

    merge_decision_report = HumanReviewDecisionGate().evaluate(
        evidence=evidence,
        native_experiment_proposal=native_experiment_proposal,
        decision=decision,
        reviewer=args.reviewer,
        acknowledgements=acknowledgements,
    )

    bundle = HumanReviewReporter(output_dir).write_all(
        dossier=dossier,
        cold_start_plan=cold_start_plan,
        native_experiment_proposal=native_experiment_proposal,
        merge_decision_report=merge_decision_report,
    )

    summary = {
        "ok": merge_decision_report.ok,
        "review_ready": merge_decision_report.review_ready,
        "decision_allowed": merge_decision_report.decision_allowed,
        "decision": merge_decision_report.decision.value,
        "reviewer": merge_decision_report.reviewer,
        "output_dir": str(output_dir),
        "bundle_hash": bundle.bundle_hash,
        "blocking_failures": list(merge_decision_report.blocking_failures),
        "missing_acknowledgements": list(merge_decision_report.missing_acknowledgements),
        "native_experiment_status": native_experiment_proposal.status,
    }

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(
            "phase13 human_review "
            f"ok={str(merge_decision_report.ok).lower()} "
            f"decision={merge_decision_report.decision.value} "
            f"review_ready={str(merge_decision_report.review_ready).lower()} "
            f"decision_allowed={str(merge_decision_report.decision_allowed).lower()} "
            f"output_dir={output_dir} "
            f"bundle_hash={bundle.bundle_hash}"
        )

    return 0 if merge_decision_report.ok else 2


if __name__ == "__main__":
    raise SystemExit(main())