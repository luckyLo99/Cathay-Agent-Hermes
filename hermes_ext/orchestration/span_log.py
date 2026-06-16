from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ShadowSpan(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    span_id: str = Field(default_factory=lambda: str(uuid4()))
    trace_id: str = Field(min_length=1)
    parent_span_id: str | None = None
    name: str = Field(min_length=1)
    started_at: datetime = Field(default_factory=utc_now)
    ended_at: datetime | None = None
    status: str = "started"
    attributes: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None

    @field_validator("trace_id", "name")
    @classmethod
    def fields_must_be_clean(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("span fields must not be empty")
        if "\x00" in value:
            raise ValueError("span fields must not contain null bytes")
        return value

    def end(self, *, status: str = "ok", error: str | None = None) -> "ShadowSpan":
        return self.model_copy(
            update={
                "ended_at": utc_now(),
                "status": status,
                "error": error,
            }
        )


class ShadowSpanLog(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    trace_id: str = Field(min_length=1)
    spans: list[ShadowSpan] = Field(default_factory=list)

    def start_span(
        self,
        name: str,
        *,
        parent_span_id: str | None = None,
        attributes: dict[str, Any] | None = None,
    ) -> ShadowSpan:
        return ShadowSpan(
            trace_id=self.trace_id,
            parent_span_id=parent_span_id,
            name=name,
            attributes=attributes or {},
        )

    def record(self, span: ShadowSpan) -> "ShadowSpanLog":
        return self.model_copy(update={"spans": [*self.spans, span]})

    def to_audit_list(self) -> list[dict[str, Any]]:
        return [span.model_dump(mode="json") for span in self.spans]