from tsal.tools.watchdog import watch


def test_watchdog_runs(tmp_path):
    sample = tmp_path / "a.py"
    sample.write_text("def a():\n    pass\n")
    watch(str(tmp_path), interval=0, cycles=1)
