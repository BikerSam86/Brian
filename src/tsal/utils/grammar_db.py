import sqlite3
from typing import Sequence, Optional, Tuple, Iterable

DEFAULT_RULES = [
    "noun",
    "verb",
    "adjective",
    "adverb",
    "preposition",
    "conjunction",
    "interjection",
]

DEFAULT_GRAMMAR: list[Tuple[str, str, str]] = [
    ("Python", "syntax", "indentation"),
    ("JavaScript", "syntax", "semicolon"),
]


def create_grammar_rules_table(db_path: str, *, reset: bool = False) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    if reset:
        cur.execute("DROP TABLE IF EXISTS grammar_rules")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS grammar_rules (id INTEGER PRIMARY KEY AUTOINCREMENT, rule TEXT UNIQUE)"
    )
    conn.commit()
    conn.close()


def create_grammar_table(db_path: str, *, reset: bool = False) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    if reset:
        cur.execute("DROP TABLE IF EXISTS grammar")
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS grammar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            context TEXT,
            lens TEXT,
            rule TEXT,
            UNIQUE(context, lens, rule)
        )
        """
    )
    conn.commit()
    conn.close()


def populate_grammar_db(
    db_path: str = "system_io.db",
    *,
    rules: Optional[Sequence[str]] = None,
    grammars: Optional[Iterable[Tuple[str, str, str]]] = None,
    reset: bool = False,
) -> int:
    if rules is None:
        rules = DEFAULT_RULES
    if grammars is None:
        grammars = DEFAULT_GRAMMAR

    create_grammar_rules_table(db_path, reset=reset)
    create_grammar_table(db_path, reset=reset)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executemany(
        "INSERT OR IGNORE INTO grammar_rules (rule) VALUES (?)",
        [(r,) for r in rules],
    )
    if grammars:
        cur.executemany(
            "INSERT OR IGNORE INTO grammar (context, lens, rule) VALUES (?, ?, ?)",
            list(grammars),
        )
    conn.commit()
    rules_count = cur.execute("SELECT COUNT(*) FROM grammar_rules").fetchone()[0]
    grammar_count = cur.execute("SELECT COUNT(*) FROM grammar").fetchone()[0]
    conn.close()
    return grammar_count if grammars else rules_count


def get_grammar_by_context(
    db_path: str,
    *,
    context: Optional[str] = None,
    lens: Optional[str] = None,
) -> list[tuple[str, str, str]]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT context, lens, rule FROM grammar"
    params: list[str] = []
    if context or lens:
        clauses = []
        if context:
            clauses.append("context = ?")
            params.append(context)
        if lens:
            clauses.append("lens = ?")
            params.append(lens)
        query += " WHERE " + " AND ".join(clauses)
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows


def main(argv: Optional[Sequence[str]] = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Populate or query the grammar database")
    parser.add_argument("--db", default="system_io.db", help="Path to SQLite database")
    parser.add_argument("--context", help="Filter by context when querying")
    parser.add_argument("--lens", help="Filter by lens when querying")
    parser.add_argument("--reset", action="store_true", help="Drop and recreate tables before populating")
    args = parser.parse_args(argv)

    if args.context or args.lens:
        rows = get_grammar_by_context(args.db, context=args.context, lens=args.lens)
        for row in rows:
            print("|".join(row))
    else:
        count = populate_grammar_db(args.db, reset=args.reset)
        print(f"{count} entries stored in {args.db}")


if __name__ == "__main__":
    main()
