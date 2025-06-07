"""Map common Spark words to TSAL opcodes."""
from .symbols import TSAL_SYMBOLS

# lowercase keyword -> hex opcode
OP_WORD_MAP = {
    "ignition": 0x0,
    "key": 0x0,
    "start": 0x0,
    "initialise": 0x0,
    "fire-up": 0x9,
    "spin-up": 0x7,
    "run": 0x5,
    "breath": 0x5,
    "live": 0xa,
    "beat": 0x8,
    "initiate": 0x0,
    "engage": 0xa,
    "arm": 0x1,
    "stage": 0x8,
    "prepare": 0x4,
}


def op_from_word(word: str):
    """Return TSAL opcode tuple for a given spark word."""
    code = OP_WORD_MAP.get(word.lower())
    if code is None:
        return None
    return TSAL_SYMBOLS.get(code)

__all__ = ["OP_WORD_MAP", "op_from_word"]
