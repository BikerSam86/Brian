from tsal.tools.alignment_guard import Change, is_aligned


def test_is_aligned_true():
    assert is_aligned(Change("Add feature", 1.0, 1.0))


def test_is_aligned_false():
    assert not is_aligned(Change("coerce user", 1.0, 1.0))
