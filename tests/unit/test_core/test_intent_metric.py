from tsal.core.intent_metric import calculate_idm
import pytest


def test_calculate_idm_basic():
    score = calculate_idm(0.9, 10, 0.95, 50, 0.8)
    assert abs(score - 0.21375) < 1e-6


def test_calculate_idm_invalid():
    with pytest.raises(ValueError):
        calculate_idm(1.0, 1.0, 1.0, 0.0, 1.0)
