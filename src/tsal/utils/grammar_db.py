import sqlite3
from pathlib import Path
from typing import Optional, Sequence, Tuple, Union

DB_PATH = Path("system_io.db")

DEFAULT_GRAMMARS = [
    ("Python", "syntax", "Indent with spaces"),
    ("Python", "style", "PEP8"),
    ("Python", "block", "Colons start blocks"),
    ("JavaScript", "syntax", "Semicolons optional"),
    ("JavaScript", "block", "{} for code blocks"),
    ("Universal", "part_of_speech", "noun"),
    ("Universal", "part_of_speech", "verb"),
]

def create_grammar_table(
    db_path: Union[Path, str] = DB_PATH, *, reset: bool = False
) -> None:
    conn = sqlite3.connect(str(db_path))
    if reset:
        cur.execute("DROP TABLE IF EXISTS grammar")
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            context TEXT,
            lens TEXT,
            rule TEXT,
            UNIQUE(context, lens, rule)
    conn.commit()
    conn.close()


def populate_grammar_db(
    db_path: Union[Path, str] = DB_PATH,
    grammars: Optional[Sequence[Tuple[str, str, str]]] = None,
    *,
    reset: bool = False,
) -> int:
    create_grammar_table(db_path, reset=reset)
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    grammars = grammars or DEFAULT_GRAMMARS
        "INSERT OR IGNORE INTO grammar (context, lens, rule) VALUES (?, ?, ?)",
def get_grammar_by_context(
    db_path: Union[Path, str] = DB_PATH,
    context: Optional[str] = None,
    lens: Optional[str] = None,
) -> list[Tuple[str, str, str]]:
    create_grammar_table(db_path)
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    sql = "SELECT context, lens, rule FROM grammar WHERE 1=1"
    params = []
    if context:
        sql += " AND context=?"
        params.append(context)
    if lens:
        sql += " AND lens=?"
        params.append(lens)
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return rows


def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description="Populate or query grammar database"
    )
    parser.add_argument("--context", help="Query by context (e.g., Python)")
    parser.add_argument(
        "--lens", help="Query by lens (e.g., syntax, style, part_of_speech)"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Drop and recreate the grammar table before populating",
    )
    if args.context or args.lens:
        rows = get_grammar_by_context(args.db, args.context, args.lens)
        for context, lens, rule in rows:
            print(f"[{context} | {lens}] {rule}")
        print(f"{len(rows)} rules returned.")
    else:
        count = populate_grammar_db(args.db, reset=args.reset)
        print(f"{count} grammar rules stored in {args.db}")

def populate_language_grammar_db(
    db_path: Path = DB_PATH, examples: Optional[Sequence[Tuple[str, str]]] = None
) -> int:
    """Create or enrich the language grammar table."""
    grammars = examples or DEFAULT_LANGUAGE_GRAMMARS
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS grammar (
            id INTEGER PRIMARY KEY,
            language TEXT,
            rules TEXT
        )
        """
    )
    cur.executemany(
        "INSERT OR IGNORE INTO grammar (language, rules) VALUES (?, ?)",
        grammars,
    )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM grammar").fetchone()[0]
    conn.close()
    return count

def populate_pos_grammar_db(
    db_path: Path = DB_PATH, rules: Optional[Sequence[str]] = None
) -> int:
    """Create or enrich the universal part-of-speech grammar table."""
    rules = rules or DEFAULT_POS_RULES
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS grammar_rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule TEXT UNIQUE
        )
        """
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

    parser = argparse.ArgumentParser(description="Populate grammar database(s)")
    parser.add_argument("--db", default="system_io.db", help="Path to SQLite DB")
    parser.add_argument("--language", action="store_true", help="Populate language-specific grammar table")
    parser.add_argument("--pos", action="store_true", help="Populate universal part-of-speech grammar table")
    args = parser.parse_args(argv)

    total = 0
    if args.language or not (args.language or args.pos):
        n = populate_language_grammar_db(Path(args.db))
        print(f"{n} language grammars stored in {args.db}")
        total += n
    if args.pos or not (args.language or args.pos):
        n = populate_pos_grammar_db(Path(args.db))
        print(f"{n} part-of-speech rules stored in {args.db}")
        total += n
    if total == 0:
        print("No grammar tables selected—use --language or --pos")

if __name__ == "__main__":
    main()
