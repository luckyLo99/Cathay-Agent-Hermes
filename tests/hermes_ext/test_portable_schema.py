from __future__ import annotations

from hermes_ext.schema.portable_schema import PortableSchemaValidator


def test_known_schemas_are_stable() -> None:
    assert PortableSchemaValidator.known_schemas() == [
        "command",
        "file_write",
        "memory_write",
        "url_fetch",
    ]


def test_command_schema_accepts_list_argv() -> None:
    result = PortableSchemaValidator.validate(
        "command",
        {"argv": ["python", "--version"], "timeout_seconds": 30},
    )

    assert result.ok
    assert result.normalized is not None
    assert result.normalized["argv"] == ["python", "--version"]


def test_command_schema_rejects_string_command() -> None:
    result = PortableSchemaValidator.validate(
        "command",
        {"argv": "python --version"},
    )

    assert not result.ok
    assert result.error


def test_command_schema_rejects_extra_field() -> None:
    result = PortableSchemaValidator.validate(
        "command",
        {
            "argv": ["python", "--version"],
            "unexpected": True,
        },
    )

    assert not result.ok
    assert result.error


def test_file_write_schema_accepts_basic_payload() -> None:
    result = PortableSchemaValidator.validate(
        "file_write",
        {
            "path": "reports/phase1/example.md",
            "content": "hello",
            "encoding": "utf-8",
            "create_dirs": True,
        },
    )

    assert result.ok


def test_url_fetch_schema_rejects_unsupported_scheme() -> None:
    result = PortableSchemaValidator.validate(
        "url_fetch",
        {"url": "file:///etc/passwd"},
    )

    assert not result.ok
    assert "scheme" in result.error


def test_memory_write_schema_accepts_confidence() -> None:
    result = PortableSchemaValidator.validate(
        "memory_write",
        {
            "namespace": "phase1",
            "key": "mock-runtime",
            "value": "offline only",
            "confidence": 0.8,
        },
    )

    assert result.ok


def test_unknown_schema_is_rejected() -> None:
    result = PortableSchemaValidator.validate(
        "unknown_schema",
        {"x": 1},
    )

    assert not result.ok
    assert result.error == "Unknown schema: unknown_schema"