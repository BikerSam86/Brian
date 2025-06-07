# Brian Self-Reflection Engine

This document sketches the modules that let Brian observe and repair itself.

- `feedback_ingest.py` turns crawler or user feedback into scored entries.
- `alignment_guard.py` blocks low φ-alignment changes.
- `goal_selector.py` picks the next task using impact, alignment and cost.
- `spiral_audit.py` runs `SymbolicOptimizer` across a directory.
- `reflect.py` prints a summary of a `Rev_Eng` session.
- `memory/core_brian_manifest.md` records Brian's purpose and history.

Run `tsal-spiral-audit` or `tsal-reflect` to exercise these tools from the CLI.
They require the `tsal` package to be installed with Matplotlib available.
