from tsal.core.meta_coherence import compute_spiral_signature
import numpy as np


def test_compute_spiral_signature_shape():
    sig = compute_spiral_signature([0.0, 1.0, 0.5])
    assert sig.amplitude.shape == sig.phase.shape
    assert sig.amplitude.size == 3


def test_compute_spiral_signature_values():
    sig = compute_spiral_signature([0, 0, 0])
    assert np.allclose(sig.amplitude, 0)
