from tsal.tools.meshkeeper import scan
from tsal.core import mesh_logger
from tsal.core.rev_eng import Rev_Eng


def test_scan(tmp_path, monkeypatch):
    log_file = tmp_path / "log.jsonl"
    monkeypatch.setattr(mesh_logger, "LOG_FILE", log_file)
    rev = Rev_Eng(origin="unit")
    rev.log_data(5, direction="in", updown="up")
    voxels = scan(str(log_file))
    assert len(voxels) == 1
    assert voxels[0]["spin"] == "up"
