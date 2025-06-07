from tsal.tools.spiral_audit import audit_directory


def test_audit_directory_counts(tmp_path):
    f = tmp_path / "demo.py"
    f.write_text("def x():\n    return 1\n")
    report = audit_directory(str(tmp_path))
    assert report["files"] == 1
    assert report["signatures"] == 1
