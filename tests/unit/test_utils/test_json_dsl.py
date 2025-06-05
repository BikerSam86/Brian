from tsal.core.json_dsl import LanguageMap, SymbolicProcessor


def test_language_map_roundtrip(tmp_path):
    data = {"language": "foo", "ops": [{"keyword": "bar", "type": "baz"}]}
    file = tmp_path / "lang.json"
    LanguageMap(language="foo", ops=data["ops"]).dump(file)
    loaded = LanguageMap.load(file)
    assert loaded.language == "foo"
    assert loaded.ops == data["ops"]


def test_symbolic_processor_encode_decode():
    lang = LanguageMap(language="py", ops=[{"keyword": "def", "type": "function"}])
    sp = SymbolicProcessor(lang)
    lines = ["def test():", "    pass"]
    tokens = sp.decode(lines)
    assert tokens[0]["type"] == "function"
    out = sp.encode(tokens)
    assert "def test():" in out

