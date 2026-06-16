from __future__ import annotations

import argparse
from pathlib import Path

from hermes_ext.harness.contracts import ExtensionHarnessMode, HarnessRunRequest
from hermes_ext.harness.feature_flags import FeatureFlagResolver
from hermes_ext.harness.integration_harness import IntegrationHarness


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="hermes_ext Phase 6 local harness")
    sub = parser.add_subparsers(dest="command", required=True)

    doctor = sub.add_parser("doctor", help="run extension diagnostics")
    doctor.add_argument("--project-root", default=".", help="project root")
    doctor.add_argument("--state-dir", default=".hermes_ext_shadow", help="shadow state directory")
    doctor.add_argument("--flags-json", default=None, help="optional feature flag JSON file")
    doctor.add_argument("--json", action="store_true", help="print JSON")

    shadow = sub.add_parser("shadow-run", help="run explicit shadow harness")
    shadow.add_argument("--project-root", default=".", help="project root")
    shadow.add_argument("--state-dir", required=True, help="shadow state directory")
    shadow.add_argument("--flags-json", default=None, help="optional feature flag JSON file")
    shadow.add_argument("--text", required=True, help="input text for shadow run")
    shadow.add_argument("--tool-name", default=None, help="optional tool name for pretool guard")
    shadow.add_argument("--argv", nargs="*", default=None, help="optional argv for pretool guard")
    shadow.add_argument("--json", action="store_true", help="print JSON")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    flags_json = Path(args.flags_json) if args.flags_json else None
    flags = FeatureFlagResolver(json_path=flags_json).resolve()

    if args.command == "doctor":
        request = HarnessRunRequest(
            mode=ExtensionHarnessMode.DIAGNOSTIC,
            state_dir=Path(args.state_dir),
            flags=flags,
        )
        result = IntegrationHarness(project_root=Path(args.project_root)).run(request)
        print(result.to_json() if args.json else _human_summary(result.model_dump(mode="json")))
        return 0 if result.ok else 1

    if args.command == "shadow-run":
        tool_payload = None
        if args.tool_name:
            tool_payload = {"tool_name": args.tool_name}
            if args.argv:
                tool_payload["argv"] = args.argv

        request = HarnessRunRequest(
            mode=ExtensionHarnessMode.SHADOW,
            text=args.text,
            state_dir=Path(args.state_dir),
            flags=flags,
            tool_payload=tool_payload,
        )
        result = IntegrationHarness(project_root=Path(args.project_root)).run(request)
        print(result.to_json() if args.json else _human_summary(result.model_dump(mode="json")))
        return 0 if result.ok else 1

    parser.error("unknown command")
    return 2


def _human_summary(data: dict) -> str:
    lines = [
        f"ok: {data.get('ok')}",
        f"mode: {data.get('mode')}",
        f"error: {data.get('error')}",
    ]

    shadow = data.get("shadow_result")
    if isinstance(shadow, dict):
        lines.append(f"shadow_status: {shadow.get('status')}")
        lines.append(f"checkpoint_count: {shadow.get('checkpoint_count')}")

    warnings = data.get("warnings") or []
    if warnings:
        lines.append("warnings:")
        lines.extend([f"- {item}" for item in warnings])

    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())