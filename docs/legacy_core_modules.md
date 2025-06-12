# Legacy Core Modules

The `core/` directory contains an early prototype of TSAL's system management code.
These modules were part of "Codex Fireproof" and predate the current `tsal`
package. They are retained for historical reference only and are **not** used by
modern TSAL components.

Modules included:

- `agent_manager.py`
- `diagnostics_watchdog.py`
- `ethics_engine.py`
- `kernel_bootstrap.py`
- `memory_forge.py`
- `priority_research_agent.py`
- `snapshot_controller.py`

You can still run `python core/kernel_bootstrap.py` to launch the legacy stack,
but expect limited functionality. The recommended approach is to use the
facilities provided under `src/tsal/` instead.
