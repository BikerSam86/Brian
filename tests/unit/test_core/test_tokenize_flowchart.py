from tsal.core.tokenize_flowchart import tokenize_to_flowchart



def test_tokenize_basic_flow(tmp_path):
    code = [
    lines = [

        "def foo():",
        "    pass",
        "if True:",
        "    foo()",
    ]
    schema = str(tmp_path / "schema.json")
    # Minimal schema
    schema_data = {
        "language": "py",
        "ops": [
            {"keyword": "def", "type": "function"},
            {"keyword": "if", "type": "branch"},
        ],
    }
    (tmp_path / "schema.json").write_text(__import__('json').dumps(schema_data))
    assert len(nodes) == 2
    nodes, edges = tokenize_to_flowchart(lines)
    types = [n["type"] for n in nodes]
    assert types == ["def", "if"]
    assert edges == [{"from": 0, "to": 2}]
