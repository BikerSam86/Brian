from tsal.core import Node, verify_connectivity


def test_verify_connectivity_true():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    a.connect(b)
    b.connect(c)
    c.connect(a)
    assert verify_connectivity([a, b, c]) is True


def test_verify_connectivity_false():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    a.connect(b)
    # c is isolated
    assert verify_connectivity([a, b, c]) is False
