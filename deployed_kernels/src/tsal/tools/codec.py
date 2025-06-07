"""Real-time decode/encode helper."""

from typing import Iterable, Callable, Optional
from importlib import resources

from tsal.core.json_dsl import LanguageMap, SymbolicProcessor
from tsal.core.rev_eng import Rev_Eng


def real_time_codec(
    lines: Iterable[str],
    schema: str | None = None,
    transform: Optional[Callable[[list[dict]], list[dict]]] = None,
    rev: Optional[Rev_Eng] = None,
) -> str:
    """Decode lines, run an optional token transform, encode result."""
    if schema is None:
        schema = str(resources.files("tsal.schemas").joinpath("python.json"))
    lang = LanguageMap.load(schema)
    rev = rev or Rev_Eng(origin="real_time_codec")
    sp = SymbolicProcessor(lang, rev_eng=rev)
    source = list(lines)
    tokens = sp.decode(source)
    if transform:
        tokens = transform(tokens)
    return sp.encode(tokens)
