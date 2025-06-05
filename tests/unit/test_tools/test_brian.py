from tsal.tools.brian import optimizer


def test_analyze_and_repair(tmp_path):
    sample = tmp_path / "sample.py"
    sample.write_text(
        """\n
def beta():\n    return 2\n\n
def alpha():\n    return 1\n"""
    )
    suggestions = optimizer.analyze_and_repair(str(sample))
    assert any("alpha" in s for s in suggestions)
