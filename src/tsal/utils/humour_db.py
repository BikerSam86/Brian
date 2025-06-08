import sqlite3
from pathlib import Path
from typing import Sequence

DB_PATH = Path("system_io.db")


def populate_humour_db(db_path: Path = DB_PATH, jokes: Sequence[tuple[str, str]] | None = None) -> int:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS humour (
            id INTEGER PRIMARY KEY,
            context TEXT,
            joke TEXT
        )
        """
    )
    seed = jokes or [
        ("Python", "Why do Python devs prefer dark mode? Because light attracts bugs."),
        ("General", "Why do programmers hate nature? It has too many bugs."),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO humour (context, joke) VALUES (?, ?)",
        seed,
    )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM humour").fetchone()[0]
    conn.close()
    return count


def main(argv: Sequence[str] | None = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Populate humour database")
    parser.add_argument("--db", default="system_io.db", help="Path to SQLite DB")
    args = parser.parse_args(argv)

    count = populate_humour_db(Path(args.db))
    print(f"{count} jokes stored in {args.db}")


if __name__ == "__main__":
    main()
