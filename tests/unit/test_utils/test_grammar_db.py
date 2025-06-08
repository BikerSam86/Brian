import sqlite3
from tsal.utils.grammar_db import populate_grammar_db, get_grammar_by_context


def test_populate_and_query(tmp_path):
    db = tmp_path / "g.db"
    count = populate_grammar_db(db_path=db, grammars=[("Py", "syntax", "indent")])
    assert count == 1
    rows = get_grammar_by_context(db, context="Py")
    assert rows == [("Py", "syntax", "indent")]
    count2 = populate_grammar_db(db_path=db, grammars=[("Py", "syntax", "indent")])
    assert count2 == 1

