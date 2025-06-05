from tsal.core.tokenize_flowchart import tokenize_to_flowchart
from tsal.renderer.code_render import mesh_to_python
from tsal.core.phase_math import phase_match_enhanced

with open("examples/broken_code.py") as f:
    lines = f.readlines()

nodes, edges = tokenize_to_flowchart(lines, "schemas/python.json")
python_code = mesh_to_python(nodes)
print(python_code)
