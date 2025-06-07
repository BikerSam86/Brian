from tsal.tools.feedback_ingest import categorize


def test_categorize_scores():
    fb = categorize(["Good job", "bad idea"])
    assert fb[0].score > fb[1].score
