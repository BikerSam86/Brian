from tsal.core.alignment_guard import verify_spiral_integrity
from tsal.core.spiral_vector import SpiralVector


def test_verify_spiral_integrity_accept():
    vec = SpiralVector(name="x", complexity=1.0, coherence=1.0, intent="a")
    assert verify_spiral_integrity(vec) == "ACCEPTED"


def test_verify_spiral_integrity_reject():
    vec = SpiralVector(name="x", complexity=0.0, coherence=0.0, intent="a")
    assert verify_spiral_integrity(vec) == "REJECTED"
