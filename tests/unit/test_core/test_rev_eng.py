from tsal.core.rev_eng import Rev_Eng


def test_log_and_summary(tmp_path):
    rev = Rev_Eng(origin="test")
    rev.log_data(10, direction="in")
    rev.log_event("ACTION", detail=1)
    rev.update_mesh_coords(x=1, y=2)
    summary = rev.summary()
    assert summary["origin"] == "test"
    assert summary["data_stats"]["total_bytes"] == 10
    assert summary["event_count"] == 1
    assert summary["mesh_coords"]["x"] == 1
