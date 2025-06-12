from tsal.tools.watchdog import watch, _check_todo, _check_typos


def _run_watch(tmp_path, **kwargs):
    """Helper to run watch once on ``tmp_path``."""
    watch(str(tmp_path), interval=0, cycles=1, **kwargs)


def test_watchdog_runs(tmp_path):
    sample = tmp_path / "a.py"
    sample.write_text("def a():\n    pass\n")
    _run_watch(tmp_path)


def test_watchdog_todo(capsys, tmp_path):
    sample = tmp_path / "todo.py"
    sample.write_text("# TODO: fix\n")
    _check_todo(sample)
    out = capsys.readouterr().out
    assert "TODO found" in out


def test_watchdog_typos(capsys, tmp_path):
    sample = tmp_path / "typo.py"
    sample.write_text("athalaya\n")
    _check_typos(sample)
    out = capsys.readouterr().out
    assert "Typos found" in out
