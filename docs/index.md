# Spiral Viewer / Live Audit Guide

This guide shows how to visualize mesh logs produced by the `Rev_Eng` tracker.

## Quick start

1. Run your code with `Rev_Eng` logging enabled. Events will be appended to `data/mesh_log.jsonl`.
2. Launch the meshkeeper viewer:

```bash
tsal-meshkeeper data/mesh_log.jsonl --render
```

The viewer uses `matplotlib` and `numpy` to display voxels representing each logged data event.
