from tsal.core.opwords import op_from_word, guess_opcode, OP_WORD_MAP


def test_known_words_map_to_ops():
    assert op_from_word("ignition")[1] == "INIT"
    assert op_from_word("engage")[1] == "SYNC"
    assert op_from_word("spin-up")[1] == "SPIRAL"
    assert op_from_word("beat")[1] == "CYCLE"


def test_synonym_words_map_to_ops():
    assert op_from_word("launch")[1] == "INIT"
    assert op_from_word("connect")[1] == "MESH"
    assert op_from_word("rotate")[1] == "ROT"


def test_missing_word_returns_none():
    assert op_from_word("unknown") is None


def test_word_map_case_insensitive():
    assert op_from_word("INITIATE")[1] == "INIT"


def test_guess_opcode_close_match():
    assert guess_opcode("launh")[1] == "INIT"
