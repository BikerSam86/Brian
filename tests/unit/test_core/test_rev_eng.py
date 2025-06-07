from tsal.core.rev_eng import Rev_Eng


def test_log_data_and_summary(monkeypatch):
    rev = Rev_Eng(origin="unit")
    start_bytes = rev.data_stats["total_bytes"]
    rev.log_data(10, direction="in")
    rev.log_data(5, direction="out")
    assert rev.data_stats["total_bytes"] == start_bytes + 15
    summary = rev.summary()
    assert summary["event_count"] == 0  # log_data only updates spin_log
    assert summary["data_stats"]["chunk_count"] == 2
