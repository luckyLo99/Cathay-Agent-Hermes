from __future__ import annotations

from pathlib import Path

from hermes_ext.cathay.adapter import CathayContractAdapter
from hermes_ext.cathay.contracts import CathayAdapterInput, CathayTextObservation
from hermes_ext.memoryx.contracts import MemoryNodeKind, MemoryNodeStatus
from hermes_ext.memoryx.fusion import ShadowMemoryFusion
from hermes_ext.memoryx.provider import ShadowMemoryProvider
from hermes_ext.runtime.request_envelope import LLMRequestEnvelope, PromptSegment


def test_fusion_writes_cathay_bundle_as_shadow_nodes(tmp_path: Path) -> None:
    provider = ShadowMemoryProvider(tmp_path / "shadow.db")
    fusion = ShadowMemoryFusion(provider)

    output = CathayContractAdapter().analyze(
        CathayAdapterInput(
            trace_id="trace",
            session_id="session",
            turn_id="turn",
            observations=[
                CathayTextObservation(
                    text="Trae DeepSeek Hermes Phase 4 pytest stability"
                )
            ],
        )
    )
    assert output.bundle is not None

    nodes = fusion.write_bundle(output.bundle)

    assert nodes
    assert provider.count_nodes() == len(nodes)
    kinds = {node.kind for node in nodes}
    assert MemoryNodeKind.PROFILE_HYPOTHESIS in kinds
    assert MemoryNodeKind.LEARNING_SIGNAL in kinds


def test_fusion_quarantines_sensitive_profile(tmp_path: Path) -> None:
    provider = ShadowMemoryProvider(tmp_path / "shadow.db")
    fusion = ShadowMemoryFusion(provider)

    output = CathayContractAdapter().analyze(
        CathayAdapterInput(
            trace_id="trace",
            session_id="session",
            turn_id="turn",
            raw_cathay_payload={
                "profile": {"api_key": "sk-abcdefghijklmnopqrstuvwxyz123456"}
            },
        )
    )
    assert output.bundle is not None

    nodes = fusion.write_bundle(output.bundle)

    assert any(node.status == MemoryNodeStatus.QUARANTINED for node in nodes)


def test_fusion_writes_envelope_metadata_snapshot(tmp_path: Path) -> None:
    provider = ShadowMemoryProvider(tmp_path / "shadow.db")
    fusion = ShadowMemoryFusion(provider)

    envelope = LLMRequestEnvelope(
        messages=[
            PromptSegment.from_message("user", "hello", segment_type="conversation")
        ],
        metadata={"phase": 4, "shadow_only": True},
    )

    node = fusion.write_envelope_metadata(envelope)

    assert node.kind == MemoryNodeKind.ENVELOPE_METADATA
    assert provider.count_nodes() == 1