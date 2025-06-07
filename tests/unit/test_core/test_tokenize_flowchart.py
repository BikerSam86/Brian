from tsal.core.tokenize_flowchart import tokenize_to_flowchart


def test_tokenize_simple():
    lines = [
        "def foo():",
        "    pass",
        "if True:",
        "    foo()",
    ]
    nodes, edges = tokenize_to_flowchart(lines)
    types = [n["type"] for n in nodes]
    assert types == ["def", "if"]
    assert edges == [{"from": 0, "to": 2}]
