import sqlite3
from typing import Sequence, Optional

DEFAULT_JOKES = [
    "Why did the chicken cross the road? To get to the other side.",
    "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.'",
]


def populate_humour_db(
    db_path: str = "system_io.db", jokes: Optional[Sequence[str]] = None
) -> int:
    if jokes is None:
        jokes = DEFAULT_JOKES

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS jokes (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT UNIQUE)"
    )
    cur.executemany(
        "INSERT OR IGNORE INTO jokes (text) VALUES (?)",
        [(j,) for j in jokes],
    )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM jokes").fetchone()[0]
    conn.close()
    return count


def main(argv: Optional[Sequence[str]] = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Populate humour database")
    parser.add_argument("--db", default="system_io.db", help="Path to SQLite database")
    args = parser.parse_args(argv)

    count = populate_humour_db(args.db)
    print(f"{count} jokes stored in {args.db}")


if __name__ == "__main__":
    main()
