from tsal.tools.party_tricks import run_trick


def test_orbital_trick():
    energy = run_trick("orbital", n=1, phi=0.0)
    assert isinstance(energy, float)


def test_phi_trick():
    score = run_trick("phi-align", complexity=1.0, coherence=0.0)
    assert isinstance(score, float)


def test_wavefunction_trick():
    val = run_trick("wavefunction", phi=0.1)
    assert isinstance(val, float)


def test_potential_trick():
    val = run_trick("potential", phi=0.1)
    assert isinstance(val, float)


def test_radius_trick():
    val = run_trick("radius", n=2, phi=0.1)
    assert isinstance(val, float)


def test_idm_trick():
    score = run_trick("idm", info_quality=0.9, info_quantity=1.0, accuracy=0.8, complexity=1.0, time_taken=1.0)
    assert isinstance(score, float)
