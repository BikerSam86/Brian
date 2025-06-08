from tsal.tools.party_tricks import run_trick


def test_orbital_trick():
    energy = run_trick("orbital", n=1, phi=0.0)
    assert isinstance(energy, float)


def test_phi_trick():
    score = run_trick("phi-align", complexity=1.0, coherence=0.0)
    assert isinstance(score, float)
