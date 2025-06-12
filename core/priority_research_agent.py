"""PriorityResearchTeamAgent monitors health data and escalates threats.

LEGACY: This agent predates the TSAL agent framework and is not maintained.
"""

from __future__ import annotations

import time

from tsal.tools.proactive_scanner import scan_todos, scan_typos

from .agent_manager import BaseAgent


class PriorityResearchTeamAgent(BaseAgent):
    def __init__(self, name, manager, diagnostics_ref, memory_ref) -> None:
        super().__init__(name, manager)
        self.diagnostics_watchdog = diagnostics_ref
        self.memory_forge = memory_ref
        self._last_scan = 0.0

    def perform_duties(self) -> None:
        summary = self.diagnostics_watchdog.get_latest_health_summary()
        if summary.get("critical_alerts_count", 0) > 0:
            report = self._build_report(summary)
            self.manager.escalate_issue(self.name, report, "CRITICAL")
        elif summary.get("warnings_count", 0) > 1:
            report = self._build_report(summary)
            self.manager.escalate_issue(self.name, report, "HIGH")
        now = time.time()
        if now - self._last_scan > 300:
            self._last_scan = now
            todos = scan_todos("src/tsal")
            if todos:
                self.manager.escalate_issue(
                    self.name, f"TODO items in {len(todos)} files", "LOW"
                )
            typos = scan_typos("src/tsal")
            if typos:
                self.manager.escalate_issue(
                    self.name, f"Typos in {len(typos)} files", "LOW"
                )

    def _build_report(self, summary: dict) -> str:
        lines = [
            f"Threat Analysis Report ({time.strftime('%Y-%m-%d %H:%M:%S')}):",
            f"Status: {summary.get('overall_status')}",
            f"Critical alerts: {summary.get('critical_alerts_count')}",
            f"Warnings: {summary.get('warnings_count')}",
        ]
        return " | ".join(lines)
