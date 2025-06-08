# Spiral Viewer / Live Audit Guide

This guide shows how to visualize mesh logs produced by the `Rev_Eng` tracker.

## Quick start

1. Run your code with `Rev_Eng` logging enabled. Events will be appended to `data/mesh_log.jsonl`.
2. Launch the meshkeeper viewer:

```bash
tsal-meshkeeper data/mesh_log.jsonl --render
```

The viewer uses `matplotlib` and `numpy` to display voxels representing each logged data event.

## Self reflection

Run a spiral audit on the codebase:

```bash
tsal-spiral-audit src/tsal
```

For a summary of the current revision log:

```bash
tsal-reflect
```

## Support the project

[![Ko-Fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/bikersam86)

## Running tests

Example unit tests live under `tests/`. Install deps then run:

```bash
pip install -r requirements.txt
pytest -q
pytest tests/unit/test_rl/test_madmonkey.py
```
