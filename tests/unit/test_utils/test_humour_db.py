from tsal.utils.humour_db import populate_humour_db
import sqlite3


def test_populate_humour_db(tmp_path):
    db = tmp_path / "humour.db"
    count = populate_humour_db(db_path=str(db), jokes=["j1", "j2"])
    assert count == 2

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT joke FROM humour")
    rows = {row[0] for row in cur.fetchall()}
    conn.close()
    assert rows == {"j1", "j2"}


def test_populate_no_duplicates(tmp_path):
    db = tmp_path / "h.db"
    count = populate_humour_db(db_path=db, jokes=[("ctx", "j1")])
    assert count == 1
    count2 = populate_humour_db(db_path=db, jokes=[("ctx", "j1")])
    assert count2 == 1

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT joke FROM humour")
    rows = {row[0] for row in cur.fetchall()}
    conn.close()
    assert rows == {"j1"}
    