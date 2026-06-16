from __future__ import annotations

import json

from hermes_ext.native_boundary.contract_suite import NoopNativeBoundaryContractSuite
from hermes_ext.native_boundary.report import NativeBoundaryContractReporter


def test_native_boundary_reporter_renders_markdown_and_json() -> None:
    result = NoopNativeBoundaryContractSuite.synthetic().run()
    reporter = NativeBoundaryContractReporter()

    markdown = reporter.render_markdown(result)
    json_text = reporter.render_json(result)
    parsed = json.loads(json_text)

    assert "# No-op Native Boundary Contract Report" in markdown
    assert "Non-negotiable Rule" in markdown
    assert parsed["ok"] is True