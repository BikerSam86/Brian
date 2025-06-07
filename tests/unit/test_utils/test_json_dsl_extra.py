from tsal.core.json_dsl import LanguageMap, SymbolicProcessor
from tsal.core.rev_eng import Rev_Eng


def test_symbolic_processor_logs(monkeypatch):
    lang = LanguageMap(language="py", ops=[{"keyword": "def", "type": "func"}])
    rev = Rev_Eng(origin="unit")
    sp = SymbolicProcessor(lang, rev_eng=rev)
    lines = ["def a():", "    return 1"]
    tokens = sp.decode(lines)
    out = sp.encode(tokens)
    assert "def a():" in out
    assert rev.data_stats["chunk_count"] == 2 + 1  # two decodes + encode
