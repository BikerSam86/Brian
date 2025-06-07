from __future__ import annotations

from typing import Optional

from ..core.tsal_executor import TSALOp


def audio_to_opcode(freq: float) -> Optional[TSALOp]:
    """Return opcode for frequency range."""
    if freq < 200:
        return TSALOp.SEEK
    if freq < 400:
        return TSALOp.SPIRAL
    if freq < 600:
        return TSALOp.SYNC  # type: ignore[attr-defined]
    return None
