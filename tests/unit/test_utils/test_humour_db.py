from tsal.utils.humour_db import populate_humour_db


def test_populate_no_duplicates(tmp_path):
    db = tmp_path / "h.db"
    count = populate_humour_db(db_path=db, jokes=[("ctx", "j1")])
    assert count == 1
    count2 = populate_humour_db(db_path=db, jokes=[("ctx", "j1")])
    assert count2 == 1

