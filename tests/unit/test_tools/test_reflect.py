from tsal.tools.reflect import reflect


def test_reflect_outputs_path(tmp_path):
    sample = tmp_path / "m.py"
    sample.write_text("def x():\n    pass\n")
    result = reflect(str(tmp_path), as_json=True)
    assert 'm.py' in result
