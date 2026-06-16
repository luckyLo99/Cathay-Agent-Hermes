from __future__ import annotations

import argparse
from pathlib import Path

from hermes_ext.assembly.contracts import AssemblyManifestConfig
from hermes_ext.assembly.manifest_builder import AssemblyManifestBuilder
from hermes_ext.assembly.release_gate import AssemblyReleaseGate
from hermes_ext.assembly.report import AssemblyReporter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build hermes_ext shadow assembly manifest")
    parser.add_argument("--project-root", default=".", help="Hermes project root")
    parser.add_argument("--manifest-md", required=True, help="output manifest markdown path")
    parser.add_argument("--manifest-json", required=True, help="output manifest json path")
    parser.add_argument("--gate-md", required=True, help="output gate markdown path")
    parser.add_argument("--gate-json", required=True, help="output gate json path")
    parser.add_argument(
        "--allow-missing-phase-reports",
        action="store_true",
        help="warn instead of fail if Phase 9/10 reports are missing",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    config = AssemblyManifestConfig(
        project_root=Path(args.project_root),
        require_phase9_native_boundary=not args.allow_missing_phase_reports,
        require_phase10_golden_trace=not args.allow_missing_phase_reports,
    )
    manifest = AssemblyManifestBuilder(config).build()
    gate = AssemblyReleaseGate().evaluate(manifest)
    reporter = AssemblyReporter()

    outputs = {
        Path(args.manifest_md): reporter.render_manifest_markdown(manifest),
        Path(args.manifest_json): reporter.render_manifest_json(manifest),
        Path(args.gate_md): reporter.render_gate_markdown(gate),
        Path(args.gate_json): reporter.render_gate_json(gate),
    }

    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    return 0 if gate.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())