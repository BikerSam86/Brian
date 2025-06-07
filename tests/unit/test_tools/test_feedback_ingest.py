from tsal.tools.feedback_ingest import ingest_lines


def test_ingest_lines_scores():
    data = ingest_lines(["all good", "error happened"])
    assert len(data) == 2
    assert data[0]["score"] > data[1]["score"]
