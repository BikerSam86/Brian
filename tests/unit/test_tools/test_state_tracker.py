import yaml
from tsal.tools import state_tracker


def test_update_and_show(tmp_path, monkeypatch, capsys):
    log = tmp_path / "state_log.yaml"
    monkeypatch.setattr(state_tracker, "LOG_PATH", log)
    state_tracker.update_entry("mod", "v0", "v1", "v2")
    state_tracker.show_entry("mod")
    out = capsys.readouterr().out
    data = yaml.safe_load(out)
    assert data["mod"]["WAS_THEN"] == "v0"
    assert data["mod"]["IS_NOW"] == "v1"
    assert data["mod"]["WILL_BE"] == "v2"
