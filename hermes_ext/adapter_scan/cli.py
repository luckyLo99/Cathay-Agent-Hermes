from __future__ import annotations

import argparse
from pathlib import Path

from hermes_ext.adapter_scan.contracts import AdapterScanConfig
from hermes_ext.adapter_scan.report import AdapterScanReporter
from hermes_ext.adapter_scan.scanner import AdapterScanEngine


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Hermes read-only adapter scan")
    parser.add_argument("--project-root", default=".", help="Hermes project root")
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="output format",
    )
    parser.add_argument("--output", default=None, help="optional output file")
    parser.add_argument(
        "--include-hermes-ext",
        action="store_true",
        help="include hermes_ext in scan; off by default",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    exclude_dirs = list(AdapterScanConfig(project_root=Path(args.project_root)).exclude_dirs)
    if args.include_hermes_ext and "hermes_ext" in exclude_dirs:
        exclude_dirs.remove("hermes_ext")

    config = AdapterScanConfig(
        project_root=Path(args.project_root),
        exclude_dirs=tuple(exclude_dirs),
    )
    report = AdapterScanEngine(config).run()
    renderer = AdapterScanReporter()

    if args.format == "json":
        output = renderer.render_json(report)
    else:
        output = renderer.render_markdown(report)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding="utf-8")
    else:
        print(output)

    return 0 if report.summary.parse_errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())