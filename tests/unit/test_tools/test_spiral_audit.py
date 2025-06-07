
from pathlib import Path
from tsal.tools.spiral_audit import audit_directory
from tsal.tools.spiral_audit import audit_path


def test_audit_directory_counts(tmp_path):
    f = tmp_path / "demo.py"
    f.write_text("def x():\n    return 1\n")
    report = audit_directory(str(tmp_path))
    assert report["files"] == 1
    assert report["signatures"] == 1


def test_audit_path(tmp_path):
    sample = tmp_path / "a.py"
    sample.write_text("def a():\n    pass\n")
    audit_path(Path(tmp_path))
