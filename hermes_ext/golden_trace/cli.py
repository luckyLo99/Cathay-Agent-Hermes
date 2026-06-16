from __future__ import annotations

import argparse
from pathlib import Path

from hermes_ext.golden_trace.contracts import GoldenTraceRunConfig
from hermes_ext.golden_trace.report import GoldenTraceReporter
from hermes_ext.golden_trace.runner import GoldenTraceRunner


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run hermes_ext golden trace replay")
    parser.add_argument("--project-root", default=".", help="Hermes project root")
    parser.add_argument("--state-dir", required=True, help="golden trace shadow state directory")
    parser.add_argument("--repeat", type=int, default=2, help="replay repetitions")
    parser.add_argument("--spec-json", default=None, help="optional Phase 8 zero-touch spec JSON")
    parser.add_argument("--native-boundary-limit", type=int, default=100, help="spec-derived native boundary case limit")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", required=True, help="output path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    config = GoldenTraceRunConfig(
        project_root=Path(args.project_root),
        state_dir=Path(args.state_dir),
        repeat=args.repeat,
        spec_json=Path(args.spec_json) if args.spec_json else None,
        native_boundary_limit=args.native_boundary_limit,
    )
    report = GoldenTraceRunner(config).run_default_pack()
    renderer = GoldenTraceReporter()

    output = renderer.render_json(report) if args.format == "json" else renderer.render_markdown(report)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")

    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())