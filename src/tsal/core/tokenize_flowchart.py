import json
from typing import List, Tuple, Dict


def tokenize_to_flowchart(
    source_lines: List[str], schema_path: str
) -> Tuple[List[Dict], List[Dict]]:
    """Turns code into flowchart nodes using language schema."""
    with open(schema_path) as f:
        ops = json.load(f)["ops"]
    triggers = {op["keyword"]: op for op in ops}
    nodes: List[Dict] = []
    edges: List[Dict] = []
    for i, line in enumerate(source_lines):
        tokens = line.strip().split()
        if tokens and tokens[0] in triggers:
            nodes.append({"id": i, "type": tokens[0], "raw": line})
            if len(nodes) > 1:
                edges.append({"from": nodes[-2]["id"], "to": nodes[-1]["id"]})
    return nodes, edges
