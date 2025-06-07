from tsal.tools.aletheia_checker import is_typo, scan_file


def test_is_typo_common():
    assert is_typo("Athalaya")
    assert not is_typo("Aletheia")


def test_scan_file_detects_typo(tmp_path):
    f = tmp_path / "demo.txt"
    f.write_text("This line mentions Athalaya once.")
    results = scan_file(f)
    assert results == [(1, "This line mentions Athalaya once.")]
