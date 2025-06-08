import sqlite3
from typing import Sequence, Optional

DEFAULT_RULES = [
    "noun",
    "verb",
    "adjective",
    "adverb",
    "preposition",
    "conjunction",
    "interjection",
]


def populate_grammar_db(
    db_path: str = "system_io.db", rules: Optional[Sequence[str]] = None
) -> int:
    if rules is None:
        rules = DEFAULT_RULES

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS grammar_rules (id INTEGER PRIMARY KEY AUTOINCREMENT, rule TEXT UNIQUE)"
    )
    cur.executemany(
        "INSERT OR IGNORE INTO grammar_rules (rule) VALUES (?)",
        [(r,) for r in rules],
    )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM grammar_rules").fetchone()[0]
    conn.close()
    return count


def main(argv: Optional[Sequence[str]] = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Populate grammar rules database")
    parser.add_argument("--db", default="system_io.db", help="Path to SQLite database")
    args = parser.parse_args(argv)

    count = populate_grammar_db(args.db)
    print(f"{count} rules stored in {args.db}")


if __name__ == "__main__":
    main()
