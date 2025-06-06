from tsal.core.spiral_vector import SpiralVector, phi_alignment
from tsal.core.symbols import PHI, PHI_INV


def test_phi_alignment_calculation():
    score = phi_alignment(1.0, 0.0)
    expected = (1.0 * PHI_INV + 0.0 * PHI) / (PHI + PHI_INV)
    assert abs(score - expected) < 1e-9


def test_spiral_vector_signature_and_alignment():
    vec = SpiralVector(name="foo", complexity=0.5, coherence=0.5, intent="test")
    assert vec.phi_signature.startswith("φ^")
    expected_align = phi_alignment(0.5, 0.5)
    assert abs(vec.alignment() - expected_align) < 1e-9
