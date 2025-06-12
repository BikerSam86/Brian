"""Agent manager for Codex Fireproof.

LEGACY: This module predates the :mod:`tsal` package and is kept only for
reference. It is not actively maintained or used by the current TSAL codebase.
"""

from __future__ import annotations

import sys
import threading
import time

from . import diagnostics_watchdog, memory_forge

active_agents: dict[str, "BaseAgent"] = {}
_status = "OFFLINE"
_shutdown = threading.Event()


class BaseAgent:
    def __init__(self, name: str, manager: "agent_manager") -> None:
        self.name = name
        self.manager = manager
        self.active = False
        self.thread: threading.Thread | None = None

    def start(self) -> None:
        self.active = True
        self.thread = threading.Thread(target=self._run_loop, daemon=True)
        self.thread.start()
        print(f"[{self.name}] started")

    def _run_loop(self) -> None:
        while self.active and not _shutdown.is_set():
            self.perform_duties()
            time.sleep(1)

    def perform_duties(self) -> None:
        pass

    def stop(self) -> None:
        self.active = False


from .priority_research_agent import PriorityResearchTeamAgent


def start_agent_manager() -> None:
    global _status
    _status = "ONLINE"
    _shutdown.clear()
    prt = PriorityResearchTeamAgent("PriorityResearchTeam", sys.modules[__name__], diagnostics_watchdog, memory_forge)
    active_agents["PriorityResearchTeam"] = prt
    prt.start()
    print("[AgentManager] Online.")


def escalate_issue(agent: str, msg: str, priority: str = "MEDIUM") -> None:
    print(f"[AgentManager] {priority} escalation from {agent}: {msg}")


def shutdown_all_agents() -> None:
    _shutdown.set()
    for agent in active_agents.values():
        agent.stop()
    for agent in active_agents.values():
        if agent.thread and agent.thread.is_alive():
            agent.thread.join(timeout=5)
    active_agents.clear()
    global _status
    _status = "OFFLINE"
    print("[AgentManager] Shutdown.")


def get_status() -> str:
    return _status
