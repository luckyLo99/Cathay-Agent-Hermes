from __future__ import annotations

import argparse
from pathlib import Path

from hermes_ext.integration_spec.contracts import IntegrationSpecConfig
from hermes_ext.integration_spec.report import IntegrationSpecReporter
from hermes_ext.integration_spec.spec_builder import IntegrationSpecBuilder


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build zero-touch Hermes integration spec")
    parser.add_argument("--project-root", default=".", help="Hermes project root")
    parser.add_argument(
        "--scan-json",
        required=True,
        help="Phase 7 adapter scan JSON path",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="output format",
    )
    parser.add_argument("--output", required=True, help="output path")
    parser.add_argument(
        "--exclude-forbidden",
        action="store_true",
        help="exclude forbidden entries from output; off by default",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    config = IntegrationSpecConfig(
        project_root=Path(args.project_root),
        phase7_scan_json=Path(args.scan_json),
        allow_forbidden_entries=not args.exclude_forbidden,
    )
    spec = IntegrationSpecBuilder(config).build_from_scan_json()
    reporter = IntegrationSpecReporter()

    if args.format == "json":
        output = reporter.render_json(spec)
    else:
        output = reporter.render_markdown(spec)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())