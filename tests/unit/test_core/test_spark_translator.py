from tsal.core.spark_translator import SPARK_TO_OPCODE, translate_spark_word
from tsal.core.symbols import TSALOp


def test_known_translation():
    assert translate_spark_word("ignite") is TSALOp.INIT
    assert translate_spark_word("seek") is TSALOp.SEEK


def test_case_insensitivity():
    assert translate_spark_word("IGNITE") is TSALOp.INIT


def test_unknown_word_returns_none():
    assert translate_spark_word("blah") is None
    assert "blah" not in SPARK_TO_OPCODE
