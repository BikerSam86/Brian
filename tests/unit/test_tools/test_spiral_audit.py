from tsal.tools.spiral_audit import audit_path
from pathlib import Path

def test_audit_path(tmp_path):
    sample = tmp_path / "a.py"
    sample.write_text("def a():\n    pass\n")
    report = audit_path(Path(tmp_path))
    assert report["files"] == 1
    assert report["signatures"] >= 1
