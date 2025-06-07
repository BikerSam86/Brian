from tsal.core.spiral_vector import SpiralVector
from tsal.core.spiral_fusion import SpiralFusionProtocol


def test_fusion_signature_updates():
    v1 = SpiralVector("a", 1.0, 0.5, "first")
    v2 = SpiralVector("b", 0.5, 1.0, "second")
    fusion = SpiralFusionProtocol("combo", [v1])
    initial_sig = fusion.phi_signature
    fusion.fuse(v2)
    assert fusion.phi_signature != initial_sig
    unified = fusion.unified_vector()
    assert unified.name == "combo"
    expected_complexity = (1.0 + 0.5) / 2
    expected_coherence = (0.5 + 1.0) / 2
    assert abs(unified.complexity - expected_complexity) < 1e-9
    assert abs(unified.coherence - expected_coherence) < 1e-9
