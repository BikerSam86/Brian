from tsal.audit.brian_self_audit import recursive_bestest_beast_loop


def test_safe_mode(tmp_path):
    (tmp_path / "a.py").write_text("def a():\n    pass\n")
    recursive_bestest_beast_loop(1, safe=True)
