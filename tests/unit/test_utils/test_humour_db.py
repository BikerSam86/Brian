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

