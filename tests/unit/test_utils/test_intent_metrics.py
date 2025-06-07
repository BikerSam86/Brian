from tsal.utils.intent_metrics import calculate_idm, MetricInputs, timed_idm


def dummy_fn(x):
    return x * 2


def test_calculate_idm_basic():
    score = calculate_idm(1.0, 10, 0.8, 5, 0.5)
    assert round(score, 3) == round((1.0 * 10 * 0.8) / (5 * 0.5), 3)


def test_timed_idm(monkeypatch):
    calls = iter([0, 0.1])
    monkeypatch.setattr('time.time', lambda: next(calls))
    inputs = MetricInputs(quality=1.0, quantity=2.0, accuracy=0.5, complexity=1.0)
    score, result = timed_idm(inputs, dummy_fn, 3)
    assert result == 6
    assert score > 0
