"""Snapshot management."""

from __future__ import annotations

import os
from datetime import datetime

SNAPSHOT_DIR = "snapshots_vault"
_status = "OFFLINE"


def _ensure_dir() -> None:
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)


def start_snapshot_controller() -> None:
    global _status
    _ensure_dir()
    _status = "ONLINE"
    print("[SnapshotController] Online.")


def create_system_snapshot(tag: str = "manual") -> str:
    _ensure_dir()
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    snap_id = f"snap_{tag}_{ts}"
    path = os.path.join(SNAPSHOT_DIR, snap_id)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "meta.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"snapshot {snap_id}\n")
    return snap_id


def get_status() -> str:
    return _status


def shutdown_snapshot_controller() -> None:
    global _status
    _status = "OFFLINE"
    print("[SnapshotController] Shutdown.")
