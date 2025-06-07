"""Minimal mesh log scanner and voxel viewer."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List, Dict, Any

import numpy as np
import matplotlib.pyplot as plt


def scan(log_path: str) -> List[Dict[str, Any]]:
    """Return list of DATA payloads from a mesh log file."""
    entries: List[Dict[str, Any]] = []
    path = Path(log_path)
    if not path.exists():
        return entries
    for line in path.read_text().splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obj.get("event_type") == "DATA" and isinstance(obj.get("payload"), dict):
            entries.append(obj["payload"])
    return entries


def render_voxels(voxels: List[Dict[str, Any]]) -> None:
    """Render voxels using matplotlib."""
    if not voxels:
        return
    xs = np.array([v.get("pace", 0) for v in voxels])
    ys = np.array([v.get("rate", 0) for v in voxels])
    zs = np.arange(len(voxels))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(xs, ys, zs)
    ax.set_xlabel("pace")
    ax.set_ylabel("rate")
    ax.set_zlabel("index")
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description="TSAL Meshkeeper")
    parser.add_argument("log", nargs="?", default="data/mesh_log.jsonl")
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()
    voxels = scan(args.log)
    if args.render:
        render_voxels(voxels)
    else:
        print(json.dumps({"voxels": len(voxels)}))


if __name__ == "__main__":
    main()
