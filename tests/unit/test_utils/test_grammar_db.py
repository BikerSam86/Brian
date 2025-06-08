from tsal.utils.grammar_db import populate_grammar_db, get_grammar_by_context
import sqlite3


def test_populate_grammar_db(tmp_path):
    db = tmp_path / "grammar.db"
    rules = ["rule_a", "rule_b"]
    populate_grammar_db(db_path=str(db), grammars=None, reset=True)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS grammar_rules (id INTEGER PRIMARY KEY AUTOINCREMENT, rule TEXT UNIQUE)"
    )
    cur.executemany("INSERT OR IGNORE INTO grammar_rules (rule) VALUES (?)", [(r,) for r in rules])
    conn.commit()
    cur.execute("SELECT rule FROM grammar_rules")
    rows = {row[0] for row in cur.fetchall()}
    conn.close()
    assert rows == {"rule_a", "rule_b"}


def test_populate_and_query(tmp_path):
    db = tmp_path / "g.db"
    count = populate_grammar_db(db_path=db, grammars=[("Py", "syntax", "indent")], reset=True)
    assert count == 1
    rows = get_grammar_by_context(db, context="Py")
    assert rows == [("Py", "syntax", "indent")]
    count2 = populate_grammar_db(db_path=db, grammars=[("Py", "syntax", "indent")])
    assert count2 == 1
