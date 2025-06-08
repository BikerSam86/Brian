import sqlite3
from pathlib import Path
from typing import Sequence

DB_PATH = Path("system_io.db")


def populate_grammar_db(db_path: Path = DB_PATH, examples: Sequence[tuple[str, str]] | None = None) -> int:
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
    grammars = examples or [
        ("Python", "PEP8; Indent with spaces; Colons start blocks"),
        ("JavaScript", "Semicolons optional; {} for blocks"),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO grammar (language, rules) VALUES (?, ?)",
        grammars,
    )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM grammar").fetchone()[0]
    conn.close()
    return count


def main(argv: Sequence[str] | None = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Populate grammar database")
    parser.add_argument("--db", default="system_io.db", help="Path to SQLite DB")
    args = parser.parse_args(argv)

    count = populate_grammar_db(Path(args.db))
    print(f"{count} grammar rules stored in {args.db}")


if __name__ == "__main__":
    main()
