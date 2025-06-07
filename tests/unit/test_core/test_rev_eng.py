from tsal.core.rev_eng import Rev_Eng

from tsal.core import mesh_logger


def test_log_data_and_summary(tmp_path, monkeypatch):
    log_file = tmp_path / "log.jsonl"
    monkeypatch.setattr(mesh_logger, "LOG_FILE", log_file)
    rev = Rev_Eng(origin="unit")
    start_bytes = rev.data_stats["total_bytes"]
    rev.log_data(10, direction="in", updown="up")
    rev.log_data(5, direction="out", updown="down")
    assert rev.data_stats["total_bytes"] == start_bytes + 15
    summary = rev.summary()
    assert summary["event_count"] == 0  # log_data only updates spin_log
    assert summary["data_stats"]["chunk_count"] == 2
    assert summary["collisions"]["xor"] == 1
    assert len(summary["voxels"]) == 2
    assert log_file.exists()


