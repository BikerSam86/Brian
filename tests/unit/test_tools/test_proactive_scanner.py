from tsal.tools.proactive_scanner import (
    scan_todos,
    scan_typos,
    scan_todo_file,
    scan_typos_file,
)


def test_scan_todos(tmp_path):
    f = tmp_path / "x.py"
    f.write_text("# TODO: fix\n")
    res = scan_todos(str(tmp_path))
    assert str(f) in res


def test_scan_todo_file(tmp_path):
    f = tmp_path / "x.py"
    f.write_text("# TODO: note\n")
    hits = scan_todo_file(f)
    assert hits and hits[0][0] == 1


def test_scan_typos(tmp_path):
    f = tmp_path / "y.py"
    f.write_text("athalaya\n")
    res = scan_typos(str(tmp_path))
    assert str(f) in res


def test_scan_typos_file(tmp_path):
    f = tmp_path / "y.py"
    f.write_text("athalaya\n")
    hits = scan_typos_file(f)
    assert hits and hits[0][0] == 1
