from __future__ import annotations

from hermes_ext.orchestration.span_log import ShadowSpanLog


def test_span_log_records_span() -> None:
    log = ShadowSpanLog(trace_id="trace")
    span = log.start_span("mock_provider")
    log = log.record(span.end(status="ok"))

    assert len(log.spans) == 1
    assert log.spans[0].status == "ok"
    assert log.spans[0].ended_at is not None


def test_span_log_audit_list() -> None:
    log = ShadowSpanLog(trace_id="trace")
    log = log.record(log.start_span("step").end(status="ok"))

    audit = log.to_audit_list()

    assert audit[0]["name"] == "step"
    assert audit[0]["status"] == "ok"