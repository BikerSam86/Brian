from tsal.core import mesh_logger
from tsal.core.mesh_logger import log_event


def test_log_event_verbose(tmp_path, capsys, monkeypatch):
    log_file = tmp_path / "mesh.jsonl"
    monkeypatch.setattr(mesh_logger, "LOG_FILE", log_file)
    entry = log_event("TEST", {"x": 1}, verbose=True)
    captured = capsys.readouterr().out
    assert "TEST" in captured
    assert log_file.exists()
    assert entry["payload"] == {"x": 1}
