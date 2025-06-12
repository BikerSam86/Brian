"""Boot sequence for Codex Fireproof.

LEGACY: Retained for compatibility with early prototypes. The modern TSAL
framework provides its own startup routines.
"""

from __future__ import annotations

import importlib
import sys
import time

CORE_MODULES = [
    "core.ethics_engine",
    "core.memory_forge",
    "core.agent_manager",
    "core.snapshot_controller",
    "core.diagnostics_watchdog",
    "core.priority_research_agent",
]


def verify_core_modules() -> None:
    missing = []
    for name in CORE_MODULES:
        try:
            importlib.import_module(name)
        except Exception:
            missing.append(name)
    if missing:
        print(f"Missing modules: {', '.join(missing)}")
        sys.exit(1)


def launch_core_system() -> None:
    from . import ethics_engine, memory_forge, agent_manager, snapshot_controller, diagnostics_watchdog

    ethics_engine.start_ethics_engine()
    memory_forge.start_memory_forge()
    agent_manager.start_agent_manager()
    snapshot_controller.start_snapshot_controller()
    diagnostics_watchdog.start_watchdog()
    print("[Kernel] Core online.")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        diagnostics_watchdog.shutdown_watchdog()
        agent_manager.shutdown_all_agents()
        snapshot_controller.shutdown_snapshot_controller()
        memory_forge.shutdown_memory_forge()
        ethics_engine.shutdown_ethics_engine()
        print("[Kernel] Shutdown complete.")


if __name__ == "__main__":
    verify_core_modules()
    launch_core_system()
