from tsal.core.tokenize_flowchart import tokenize_to_flowchart


def test_tokenize_basic_flow(tmp_path):
    code = [
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
    nodes, edges = tokenize_to_flowchart(code, schema)
    assert len(nodes) == 2
    assert edges == [{"from": 0, "to": 2}]
