import json
import sys
import types

import pytest

requests_stub = types.SimpleNamespace(get=lambda *a, **k: None, HTTPError=Exception)
yaml_stub = types.SimpleNamespace(safe_load=lambda *a, **k: {})
sys.modules.setdefault("requests", requests_stub)
sys.modules.setdefault("yaml", yaml_stub)

from tsal.core import mesh_logger
from tsal.core.mesh_logger import log_event


def test_log_event_writes(tmp_path, monkeypatch):
    log_file = tmp_path / "mesh.jsonl"
    monkeypatch.setattr(mesh_logger, "LOG_FILE", log_file)
    entry = log_event("TEST", {"foo": 1}, verbose=False)
    data = log_file.read_text().strip().splitlines()
    assert len(data) == 1
    saved = json.loads(data[0])
    assert saved["event_type"] == "TEST"
    assert saved["payload"] == {"foo": 1}
    assert "timestamp" in saved


def test_log_event_invalid(tmp_path, monkeypatch):
    log_file = tmp_path / "mesh.jsonl"
    monkeypatch.setattr(mesh_logger, "LOG_FILE", log_file)
    with pytest.raises(ValueError):
        log_event("BAD", "not a dict")
