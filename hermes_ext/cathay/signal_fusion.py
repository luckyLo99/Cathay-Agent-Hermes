from __future__ import annotations

from typing import Any

from hermes_ext.cathay.contracts import (
    CathayAdapterInput,
    CathayIntent,
    CathaySignalBundle,
    CathaySignalSeverity,
)
from hermes_ext.runtime.request_envelope import LLMRequestEnvelope


class CathaySignalFusion:
    """
    Converts CathaySignalBundle into read-only envelope metadata.

    It does not alter messages, tools, provider, model, memory, or skills.
    """

    @staticmethod
    def infer_intent(text: str, raw_payload: dict[str, Any]) -> CathayIntent:
        raw_intent = raw_payload.get("intent")
        if isinstance(raw_intent, str):
            try:
                return CathayIntent(raw_intent.strip().lower())
            except ValueError:
                pass

        lowered = text.lower()

        if any(item in lowered for item in ["pytest", "代码", "code", "refactor", "重构", "github"]):
            return CathayIntent.CODING

        if any(item in lowered for item in ["学习", "learn", "mastery", "掌握"]):
            return CathayIntent.LEARNING

        if any(item in lowered for item in ["计划", "规划", "phase", "阶段", "roadmap"]):
            return CathayIntent.PLANNING

        if any(item in lowered for item in ["复盘", "反思", "reflection"]):
            return CathayIntent.REFLECTION

        if any(item in lowered for item in ["难受", "焦虑", "陪伴", "support"]):
            return CathayIntent.EMOTIONAL_SUPPORT

        if any(item in lowered for item in ["install", "启动", "运行", "doctor", "环境"]):
            return CathayIntent.SYSTEM_OPERATION

        return CathayIntent.UNKNOWN

    @staticmethod
    def fuse_to_metadata(bundle: CathaySignalBundle) -> dict[str, Any]:
        highest_safety = "info"
        if bundle.safety:
            severity_order = {
                CathaySignalSeverity.INFO: 0,
                CathaySignalSeverity.LOW: 1,
                CathaySignalSeverity.MEDIUM: 2,
                CathaySignalSeverity.HIGH: 3,
                CathaySignalSeverity.CRITICAL: 4,
            }
            highest = max(bundle.safety, key=lambda item: severity_order[item.severity])
            highest_safety = highest.severity.value

        return {
            "cathay": {
                "phase": 3,
                "mode": "read_only_adapter",
                "bundle_hash": bundle.bundle_hash,
                "intent": bundle.intent.value,
                "has_blocking_safety": bundle.has_blocking_safety(),
                "requires_review": bundle.requires_review(),
                "highest_safety_severity": highest_safety,
                "signal_counts": {
                    "safety": len(bundle.safety),
                    "profile": len(bundle.profile),
                    "learning": len(bundle.learning),
                    "proactive": len(bundle.proactive),
                },
            }
        }

    @staticmethod
    def attach_to_envelope(
        envelope: LLMRequestEnvelope,
        bundle: CathaySignalBundle,
    ) -> LLMRequestEnvelope:
        metadata = dict(envelope.metadata)
        metadata.update(CathaySignalFusion.fuse_to_metadata(bundle))
        return envelope.model_copy(update={"metadata": metadata})

    @staticmethod
    def joined_observation_text(adapter_input: CathayAdapterInput) -> str:
        return "\n".join(item.text for item in adapter_input.observations)