from __future__ import annotations

import argparse
from pathlib import Path

from hermes_ext.native_boundary.contract_suite import NoopNativeBoundaryContractSuite
from hermes_ext.native_boundary.report import NativeBoundaryContractReporter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run no-op native boundary contract tests")
    parser.add_argument(
        "--spec-json",
        default=None,
        help="optional Phase 8 zero-touch integration spec JSON",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="maximum spec entries to convert into contract cases",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="output format",
    )
    parser.add_argument("--output", default=None, help="optional output path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.spec_json:
        suite = NoopNativeBoundaryContractSuite.from_spec_json(
            Path(args.spec_json),
            limit=args.limit,
        )
    else:
        suite = NoopNativeBoundaryContractSuite.synthetic()

    result = suite.run()
    reporter = NativeBoundaryContractReporter()

    if args.format == "json":
        output = reporter.render_json(result)
    else:
        output = reporter.render_markdown(result)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding="utf-8")
    else:
        print(output)

    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())