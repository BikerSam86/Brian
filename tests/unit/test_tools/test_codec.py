from importlib import resources
from tsal.tools.codec import real_time_codec
from tsal.core.rev_eng import Rev_Eng


def test_real_time_codec_roundtrip():
    lines = ["def a():", "    return 1"]
    schema = str(resources.files("tsal.schemas").joinpath("python.json"))
    rev = Rev_Eng(origin="test")
    out = real_time_codec(lines, schema=schema, rev=rev)
    assert "def a():" in out
    assert rev.data_stats["chunk_count"] == len(lines) + 1


def test_real_time_codec_transform():
    lines = ["def a():", "    return 1"]
    schema = str(resources.files("tsal.schemas").joinpath("python.json"))
    def tweak(tokens):
        tokens[-1]["raw"] = "    return 2"
        return tokens
    out = real_time_codec(lines, schema=schema, transform=tweak)
    assert "return 2" in out
