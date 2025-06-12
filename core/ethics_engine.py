"""Minimal Ethics Engine for Codex Fireproof.

LEGACY: This standalone version has been superseded by :mod:`tsal.core.ethics_engine`.
It is retained only for archival purposes.
"""

IMMUTABLE_LAWS = [
    "Protect life",
    "Honor kindness",
    "Preserve truth",
]

_status = "OFFLINE"


def start_ethics_engine() -> None:
    global _status
    _status = "ONLINE"
    for law in IMMUTABLE_LAWS:
        print(f"[EthicsEngine] Law active: {law}")
    print("[EthicsEngine] Online.")


def get_status() -> str:
    return _status


def shutdown_ethics_engine() -> None:
    global _status
    _status = "OFFLINE"
    print("[EthicsEngine] Shutdown.")
