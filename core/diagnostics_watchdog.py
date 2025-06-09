"""System health monitor."""

from __future__ import annotations

from datetime import datetime
from threading import Event, Thread
import time

_status = "OFFLINE"
_last_summary = {
    "timestamp": None,
    "overall_status": "UNKNOWN",
    "critical_alerts_count": 0,
    "warnings_count": 0,
    "critical_alert_details": [],
    "warning_details": [],
}
_stop_event = Event()
_thread: Thread | None = None


def _run_loop(interval: int) -> None:
    while not _stop_event.is_set():
        run_manual_checks()
        _stop_event.wait(interval)


def start_watchdog(interval: int = 300) -> None:
    global _status, _thread
    if _status == "ONLINE":
        return
    _status = "ONLINE"
    run_manual_checks()
    _stop_event.clear()
    _thread = Thread(target=_run_loop, args=(interval,), daemon=True)
    _thread.start()
    print("[Watchdog] Online.")


def run_manual_checks() -> dict:
    global _last_summary
    # simple stub checks
    _last_summary = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "overall_status": "NOMINAL",
        "critical_alerts_count": 0,
        "warnings_count": 0,
        "critical_alert_details": [],
        "warning_details": [],
    }
    return _last_summary


def get_latest_health_summary() -> dict:
    return _last_summary


def shutdown_watchdog() -> None:
    global _status
    _status = "OFFLINE"
    _stop_event.set()
    if _thread and _thread.is_alive():
        _thread.join(timeout=5)
    print("[Watchdog] Shutdown.")
