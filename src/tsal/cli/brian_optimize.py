"""CLI wrapper for the Brian optimizer."""

from .brian import main as _main


def main() -> None:
    _main()


if __name__ == "__main__":
    main()
