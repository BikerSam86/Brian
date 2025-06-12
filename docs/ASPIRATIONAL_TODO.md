# TSAL Advanced To-Do

The repo covers the basics but several modules remain placeholders. This list tracks the high-level tasks to expand the system.

- **Meshkeeper viewer** – `src/tsal/tools/meshkeeper.py`
  - Add real-time GPU/CLI visualization of mesh logs (`--render` flag is minimal now).
  - Export heatmaps and support interactive rotation.
- **Feedback ingest** – `src/tsal/tools/feedback_ingest.py`
  - Expand `_score()` with RL-derived weights and context filters.
- **Goal selector** – `src/tsal/tools/goal_selector.py`
  - Implement reinforcement learning signals to tune `score_goals`.
- **Module draft generator** – `src/tsal/tools/module_draft.py`
  - Rewrite using AST pattern matching instead of naive parsing.
- **TriStar governor** – `src/tsal/tristar/governor.py`
  - Support multi-node voting and consensus handling.
- **Error dignity protocols** – `src/tsal/utils/error_dignity.py`
  - Persist error artifacts and transform them into training data.
- **GPU mesh visualisation** – `src/tsal/cli/meshkeeper.py`
  - Hook into the viewer to display 3D heatmaps.

