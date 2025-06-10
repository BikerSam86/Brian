from tsal.tools.proactive_scanner import scan_todos, scan_typos


def test_scan_todos(tmp_path):
    f = tmp_path / "x.py"
    f.write_text("# TODO: fix\n")
    res = scan_todos(str(tmp_path))
    assert str(f) in res


def test_scan_typos(tmp_path):
    f = tmp_path / "y.py"
    f.write_text("athalaya\n")
    res = scan_typos(str(tmp_path))
    assert str(f) in res
