from __future__ import annotations

import argparse
from pathlib import Path

from hermes_ext.finalization.contracts import FinalizationBundle, FinalizationConfig
from hermes_ext.finalization.documentation_pack import FinalDocumentationPackBuilder
from hermes_ext.finalization.evidence_loader import FinalizationEvidenceLoader
from hermes_ext.finalization.merge_gate import MergeReadinessGate
from hermes_ext.finalization.report import FinalizationReporter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Phase 12 final stabilization documentation pack")
    parser.add_argument("--project-root", default=".", help="Hermes project root")
    parser.add_argument("--output-dir", default="reports/phase12", help="Phase 12 output directory")
    parser.add_argument(
        "--allow-warnings",
        action="store_true",
        help="reserved for future use; warnings are currently non-blocking",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    config = FinalizationConfig(
        project_root=Path(args.project_root),
        output_dir=Path(args.output_dir),
    )

    loader = FinalizationEvidenceLoader(config)
    evidence = loader.load()

    doc_pack = FinalDocumentationPackBuilder().build(evidence)
    readiness = MergeReadinessGate(config).evaluate(evidence)

    bundle = FinalizationBundle(
        documentation_pack=doc_pack,
        readiness_report=readiness,
        evidence=evidence,
    ).with_hash()

    reporter = FinalizationReporter()
    output_dir = config.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        output_dir / "final_documentation_pack.md": reporter.render_documentation_markdown(doc_pack),
        output_dir / "final_documentation_pack.json": reporter.render_documentation_json(doc_pack),
        output_dir / "merge_readiness_report.md": reporter.render_readiness_markdown(readiness),
        output_dir / "merge_readiness_report.json": reporter.render_readiness_json(readiness),
        output_dir / "rollback_index.md": reporter.render_rollback_index_markdown(doc_pack),
        output_dir / "maintenance_guide.md": reporter.render_maintenance_guide_markdown(doc_pack),
        output_dir / "final_stabilization_bundle.json": reporter.render_bundle_json(bundle),
    }

    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")

    return 0 if readiness.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())