import pytest
from tsal.utils.fuzzy_spellcheck import fuzzy_correct

def test_fuzzy_correct_basic():
    result = fuzzy_correct("pritn", ["print"])
    assert result == "print"
