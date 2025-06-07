from tsal.core.state_vector import FourVector


def test_rotate_changes_components():
    vec = FourVector(1.0, 1.0, 1.0, 1.0)
    before = (vec.pace, vec.rate, vec.state, vec.spin)
    vec.rotate_by_phi()
    after = (vec.pace, vec.rate, vec.state, vec.spin)
    assert before != after


def test_magnitude_positive():
    vec = FourVector(0.5, 0.5, 0.5, 0.5)
    assert vec.magnitude() > 0

