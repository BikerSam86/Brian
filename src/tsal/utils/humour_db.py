import sqlite3
from pathlib import Path
from typing import Sequence, Optional, Tuple, Union

DB_PATH = Path("system_io.db")

DEFAULT_STRUCTURED_JOKES = [
    ("Python", "Why do Python devs prefer dark mode? Because light attracts bugs."),
    ("General", "Why do programmers hate nature? It has too many bugs."),
]
DEFAULT_ONE_LINERS = [
    "Why did the chicken cross the road? To get to the other side.",
    "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.'",
]

def populate_humour_db(
    db_path: Union[Path, str] = DB_PATH, 
    jokes: Optional[Sequence[Union[Tuple[str, str], str]]] = None
) -> int:
    """
    Populates the 'humour' table with structured jokes (context, joke)
    and/or plain one-liners (context set to 'General').
    """
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS humour (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            context TEXT,
            joke TEXT UNIQUE
        )
        """
    )
    # Combine both joke types
    combined: list[Tuple[str, str]] = []
    jokes = jokes or []
    for entry in (jokes if jokes else []):
        if isinstance(entry, tuple) and len(entry) == 2:
            combined.append(entry)
        elif isinstance(entry, str):
            combined.append(("General", entry))
    # Use defaults if empty
    if not combined:
        combined = DEFAULT_STRUCTURED_JOKES + [("General", j) for j in DEFAULT_ONE_LINERS]

    cur.executemany(
        "INSERT OR IGNORE INTO humour (context, joke) VALUES (?, ?)",
        combined,
    )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM humour").fetchone()[0]
    conn.close()
    return count

def main(argv: Optional[Sequence[str]] = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Populate humour database")
    parser.add_argument("--db", default="system_io.db", help="Path to SQLite DB")
    args = parser.parse_args(argv)

    count = populate_humour_db(args.db)
    print(f"{count} jokes stored in {args.db}")

if __name__ == "__main__":
    main()
