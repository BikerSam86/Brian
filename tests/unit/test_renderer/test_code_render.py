from tsal.renderer.code_render import mesh_to_python


def test_mesh_to_python_simple():
    nodes = [
        {"id": 0, "type": "def", "raw": "def foo():\n"},
        {"id": 1, "type": "return", "raw": "return 1\n"},
    ]

    python_code = mesh_to_python(nodes)

    assert python_code == "def foo():\n\n    return 1\n"
