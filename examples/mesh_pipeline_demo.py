from tsal.core.tokenize_flowchart import tokenize_to_flowchart
from tsal.renderer.code_render import mesh_to_python
from tsal.core.phase_math import phase_match_enhanced
from importlib import resources

with open("examples/broken_code.py") as f:
    lines = f.readlines()

schema_path = resources.files("tsal.schemas").joinpath("python.json")
nodes, edges = tokenize_to_flowchart(lines, schema_path)
python_code = mesh_to_python(nodes)
print(python_code)
