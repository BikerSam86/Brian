from tsal.utils.grammar_db import populate_grammar_db
import sqlite3


def test_populate_grammar_db(tmp_path):
    db = tmp_path / "grammar.db"
    count = populate_grammar_db(db_path=str(db), rules=["rule_a", "rule_b"])
    assert count == 2

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT rule FROM grammar_rules")
    rows = {row[0] for row in cur.fetchall()}
    conn.close()
    assert rows == {"rule_a", "rule_b"}
