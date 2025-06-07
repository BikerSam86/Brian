import pytest
from tsal.core.constants import AXIS_ZERO, ensure_spin_axis, UndefinedPhaseError


class Dummy:
    pass


class DummySpin:
    spin = 1


def test_axis_zero_constant():
    assert AXIS_ZERO == "spin"


def test_ensure_spin_axis_raises():
    with pytest.raises(UndefinedPhaseError):
        ensure_spin_axis(Dummy())


def test_ensure_spin_axis_ok():
    ensure_spin_axis(DummySpin())
