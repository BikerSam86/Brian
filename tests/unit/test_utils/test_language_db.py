from tsal.utils.language_db import populate_language_db
import sqlite3


def test_populate_language_db(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "tsal.utils.language_db.fetch_languages", lambda: ["Python", "Rust"]
    )
    db = tmp_path / "lang.db"
    count = populate_language_db(db_path=str(db))
    assert count == 2

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT name FROM languages")
    rows = {row[0] for row in cur.fetchall()}
    conn.close()
    assert rows == {"Python", "Rust"}
