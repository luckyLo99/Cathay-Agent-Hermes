from __future__ import annotations

import ipaddress
from urllib.parse import urlparse

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.security.decisions import SecurityDecision


class URLGuardConfig(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    allow_http: bool = False
    allowed_schemes: set[str] = Field(default_factory=lambda: {"https"})
    denied_hosts: set[str] = Field(
        default_factory=lambda: {
            "localhost",
            "metadata.google.internal",
        }
    )
    denied_host_suffixes: set[str] = Field(default_factory=lambda: {".local"})
    deny_private_ip_hosts: bool = True


class URLGuard:
    def __init__(self, config: URLGuardConfig | None = None) -> None:
        self.config = config or URLGuardConfig()

    def evaluate(self, url: str) -> SecurityDecision:
        if "\x00" in url:
            return SecurityDecision.deny("URL contains null byte", rule_id="url.null_byte")

        url = url.strip()
        if not url:
            return SecurityDecision.deny("URL is empty", rule_id="url.empty")

        parsed = urlparse(url)
        scheme = parsed.scheme.lower()
        host = (parsed.hostname or "").lower()

        if not scheme:
            return SecurityDecision.deny("URL scheme is missing", rule_id="url.missing_scheme")

        if scheme == "http" and not self.config.allow_http:
            return SecurityDecision.ask(
                "Plain HTTP requires approval",
                rule_id="url.http_requires_approval",
                metadata={"url": url},
            )

        if scheme not in self.config.allowed_schemes and not (scheme == "http" and self.config.allow_http):
            return SecurityDecision.deny(
                f"URL scheme denied: {scheme}",
                rule_id="url.scheme_denied",
                metadata={"scheme": scheme},
            )

        if not host:
            return SecurityDecision.deny("URL host is missing", rule_id="url.missing_host")

        if host in self.config.denied_hosts:
            return SecurityDecision.deny(
                f"URL host denied: {host}",
                rule_id="url.host_denied",
                metadata={"host": host},
            )

        for suffix in self.config.denied_host_suffixes:
            if host.endswith(suffix):
                return SecurityDecision.deny(
                    f"URL host suffix denied: {suffix}",
                    rule_id="url.host_suffix_denied",
                    metadata={"host": host, "suffix": suffix},
                )

        if self.config.deny_private_ip_hosts and self._is_private_ip_literal(host):
            return SecurityDecision.deny(
                f"Private IP host denied: {host}",
                rule_id="url.private_ip_denied",
                metadata={"host": host},
            )

        return SecurityDecision.allow(
            "URL allowed",
            rule_id="url.allow",
            metadata={"scheme": scheme, "host": host},
        )

    @staticmethod
    def _is_private_ip_literal(host: str) -> bool:
        try:
            ip = ipaddress.ip_address(host)
        except ValueError:
            return False

        return (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_multicast
            or ip.is_reserved
            or ip.is_unspecified
        )