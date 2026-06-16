from __future__ import annotations

from hermes_ext.cathay.contracts import (
    CathayAdapterInput,
    CathayAdapterMode,
    CathayAdapterOutput,
    CathaySignalBundle,
)
from hermes_ext.cathay.learning_bridge import CathayLearningBridge
from hermes_ext.cathay.profile_bridge import CathayProfileBridge
from hermes_ext.cathay.proactive_bridge import CathayProactiveBridge
from hermes_ext.cathay.safety_bridge import CathaySafetyBridge
from hermes_ext.cathay.signal_fusion import CathaySignalFusion


class CathayContractAdapter:
    """
    Read-only Cathay adapter.

    It converts Cathay-like payloads and current text observations into
    typed advisory signals. It does not import Cathay-Agent.
    """

    def __init__(
        self,
        *,
        safety_bridge: CathaySafetyBridge | None = None,
        profile_bridge: CathayProfileBridge | None = None,
        learning_bridge: CathayLearningBridge | None = None,
        proactive_bridge: CathayProactiveBridge | None = None,
    ) -> None:
        self.safety_bridge = safety_bridge or CathaySafetyBridge()
        self.profile_bridge = profile_bridge or CathayProfileBridge()
        self.learning_bridge = learning_bridge or CathayLearningBridge()
        self.proactive_bridge = proactive_bridge or CathayProactiveBridge()

    def analyze(self, adapter_input: CathayAdapterInput) -> CathayAdapterOutput:
        prepared = adapter_input.prepared()

        if prepared.mode == CathayAdapterMode.OFF:
            return CathayAdapterOutput(
                ok=True,
                mode=prepared.mode,
                bundle=CathaySignalBundle(
                    trace_id=prepared.trace_id,
                    session_id=prepared.session_id,
                    turn_id=prepared.turn_id,
                    metadata={"disabled": True},
                ).with_hash(),
                warnings=["Cathay adapter disabled"],
            )

        text = CathaySignalFusion.joined_observation_text(prepared)
        raw_payload = prepared.raw_cathay_payload

        try:
            intent = CathaySignalFusion.infer_intent(text, raw_payload)

            bundle = CathaySignalBundle(
                trace_id=prepared.trace_id,
                session_id=prepared.session_id,
                turn_id=prepared.turn_id,
                intent=intent,
                safety=self.safety_bridge.extract(raw_payload, text),
                profile=self.profile_bridge.extract(raw_payload, text),
                learning=self.learning_bridge.extract(raw_payload, text),
                proactive=self.proactive_bridge.extract(raw_payload, text),
                metadata={
                    "mode": prepared.mode.value,
                    "observation_count": len(prepared.observations),
                    "raw_payload_keys": sorted(raw_payload.keys()),
                    "read_only": True,
                },
            ).with_hash()

            warnings: list[str] = []
            if prepared.mode == CathayAdapterMode.OBSERVE_ONLY:
                warnings.append("observe_only: signals are advisory and must not mutate Hermes state")

            if bundle.has_blocking_safety():
                warnings.append("blocking safety signal present")

            if bundle.requires_review():
                warnings.append("human review required before persistence or action")

            return CathayAdapterOutput(
                ok=True,
                mode=prepared.mode,
                bundle=bundle,
                warnings=warnings,
            )

        except Exception as exc:
            return CathayAdapterOutput(
                ok=False,
                mode=prepared.mode,
                error=str(exc),
            )