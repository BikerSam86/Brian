import sqlite3
from pathlib import Path
from typing import Sequence, Optional, Tuple

DB_PATH = Path("system_io.db")

DEFAULT_LANGUAGE_GRAMMARS = [
    ("Python", "PEP8; Indent with spaces; Colons start blocks"),
    ("JavaScript", "Semicolons optional; {} for blocks"),
]

DEFAULT_POS_RULES = [
    "noun",
    "verb",
    "adjective",
    "adverb",
    "preposition",
    "conjunction",
    "interjection",
]

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
