from tsal.tools.scorer import score_code


def test_score_code():
    score, label = score_code("x=1")
    assert 0 < score
    assert label.startswith("\u03d5^")
