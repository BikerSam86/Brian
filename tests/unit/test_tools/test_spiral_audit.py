from tsal.tools.spiral_audit import audit_path, audit_paths
from pathlib import Path

def test_audit_path(tmp_path):
    sample = tmp_path / "a.py"
    sample.write_text("def a():\n    pass\n")
    report = audit_path(Path(tmp_path))
    assert report["files"] == 1
    assert report["signatures"] >= 1


def test_audit_paths(tmp_path):
    d1 = tmp_path / "d1"
    d1.mkdir()
    (d1 / "a.py").write_text("def a():\n    pass\n")
    d2 = tmp_path / "d2"
    d2.mkdir()
    (d2 / "b.py").write_text("def b():\n    pass\n")
    reports = audit_paths([d1, d2])
    assert reports[str(d1)]["files"] == 1
    assert reports[str(d2)]["files"] == 1
