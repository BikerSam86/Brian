"""Simple redundant memory store.

LEGACY: Superseded by :mod:`tsal.utils.persistence` but kept for reference.
"""

from __future__ import annotations

import json
import os
from threading import RLock
from datetime import datetime

MEMORY_DIR = "memory_vault"
SNAPSHOT_FILE = os.path.join(MEMORY_DIR, "memory_snapshot.json")

_state: dict = {}
_lock = RLock()
_status = "OFFLINE"


def _ensure_dir() -> None:
    os.makedirs(MEMORY_DIR, exist_ok=True)


def save_memory_state() -> None:
    with _lock:
        _ensure_dir()
        data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "payload": _state,
        }
        with open(SNAPSHOT_FILE, "w", encoding="utf-8") as fh:
            json.dump(data, fh)


def load_memory_state() -> None:
    global _state
    if not os.path.exists(SNAPSHOT_FILE):
        return
    with open(SNAPSHOT_FILE, "r", encoding="utf-8") as fh:
        try:
            content = json.load(fh)
            _state = content.get("payload", {})
        except json.JSONDecodeError:
            _state = {}


def get_memory_value(key: str, default=None):
    with _lock:
        return _state.get(key, default)


def set_memory_value(key: str, value) -> None:
    with _lock:
        _state[key] = value
        save_memory_state()


def start_memory_forge() -> None:
    global _status
    _ensure_dir()
    load_memory_state()
    _status = "ONLINE"
    print("[MemoryForge] Online.")


def get_status() -> str:
    return _status


def shutdown_memory_forge() -> None:
    global _status
    save_memory_state()
    _status = "OFFLINE"
    print("[MemoryForge] Shutdown.")
