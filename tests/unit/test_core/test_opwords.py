from tsal.core.opwords import op_from_word, OP_WORD_MAP


def test_known_words_map_to_ops():
    assert op_from_word("ignition")[1] == "INIT"
    assert op_from_word("engage")[1] == "SYNC"
    assert op_from_word("spin-up")[1] == "SPIRAL"
    assert op_from_word("beat")[1] == "CYCLE"


def test_missing_word_returns_none():
    assert op_from_word("unknown") is None


def test_word_map_case_insensitive():
    assert op_from_word("INITIATE")[1] == "INIT"
