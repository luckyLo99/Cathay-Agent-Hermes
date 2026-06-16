from __future__ import annotations

from typing import Any, Literal
from urllib.parse import urlparse

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator


class ValidationResult(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    ok: bool
    schema_name: str
    error: str | None = None
    normalized: dict[str, Any] | None = None


class CommandInput(BaseModel):
    """
    Portable command schema.

    Phase 1 validates shape only. Policy decisions belong to Phase 2.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    argv: list[str] = Field(min_length=1)
    cwd: str | None = None
    timeout_seconds: int = Field(default=60, ge=1, le=600)

    @field_validator("argv")
    @classmethod
    def argv_must_be_list_of_non_empty_strings(cls, value: list[str]) -> list[str]:
        clean: list[str] = []
        for item in value:
            item = item.strip()
            if not item:
                raise ValueError("Command argv must not contain empty strings")
            if "\x00" in item:
                raise ValueError("Command argv must not contain null bytes")
            clean.append(item)
        return clean

    @field_validator("cwd")
    @classmethod
    def cwd_must_not_contain_null_bytes(cls, value: str | None) -> str | None:
        if value is not None and "\x00" in value:
            raise ValueError("cwd must not contain null bytes")
        return value


class FileWriteInput(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    path: str = Field(min_length=1)
    content: str
    encoding: Literal["utf-8"] = "utf-8"
    create_dirs: bool = False

    @field_validator("path")
    @classmethod
    def path_must_be_plain_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("path must not be empty")
        if "\x00" in value:
            raise ValueError("path must not contain null bytes")
        return value


class URLFetchInput(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    url: str = Field(min_length=1)
    method: Literal["GET", "POST"] = "GET"
    headers: dict[str, str] = Field(default_factory=dict)
    body: str | None = None
    timeout_seconds: int = Field(default=30, ge=1, le=120)

    @field_validator("url")
    @classmethod
    def url_must_have_supported_scheme(cls, value: str) -> str:
        value = value.strip()
        parsed = urlparse(value)
        if parsed.scheme not in {"http", "https"}:
            raise ValueError("url scheme must be http or https")
        if not parsed.netloc:
            raise ValueError("url must include host")
        if "\x00" in value:
            raise ValueError("url must not contain null bytes")
        return value


class MemoryWriteInput(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    namespace: str = Field(min_length=1)
    key: str = Field(min_length=1)
    value: str = Field(min_length=1)
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    source_trace_id: str | None = None

    @field_validator("namespace", "key", "value")
    @classmethod
    def text_fields_must_be_safe(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("field must not be empty")
        if "\x00" in value:
            raise ValueError("field must not contain null bytes")
        return value


class PortableSchemaValidator:
    """
    Fake portable schema compiler for Phase 1.

    It validates known payloads without executing anything.
    """

    _schemas: dict[str, type[BaseModel]] = {
        "command": CommandInput,
        "file_write": FileWriteInput,
        "url_fetch": URLFetchInput,
        "memory_write": MemoryWriteInput,
    }

    @classmethod
    def validate(cls, schema_name: str, payload: dict[str, Any]) -> ValidationResult:
        model_cls = cls._schemas.get(schema_name)
        if model_cls is None:
            return ValidationResult(
                ok=False,
                schema_name=schema_name,
                error=f"Unknown schema: {schema_name}",
                normalized=None,
            )

        try:
            parsed = model_cls.model_validate(payload)
        except ValidationError as exc:
            return ValidationResult(
                ok=False,
                schema_name=schema_name,
                error=str(exc),
                normalized=None,
            )

        return ValidationResult(
            ok=True,
            schema_name=schema_name,
            error=None,
            normalized=parsed.model_dump(mode="json"),
        )

    @classmethod
    def known_schemas(cls) -> list[str]:
        return sorted(cls._schemas.keys())