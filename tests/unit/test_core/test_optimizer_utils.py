from tsal.core.optimizer_utils import extract_signature_from_source


def test_extract_signature_python():
    code = "def foo(x):\n    if x:\n        return 1\n    return 0\n"
    sig = extract_signature_from_source(code, "foo")
    assert sig.vector[0] > 0


def test_extract_signature_javascript():
    js = "function foo(x){ if(x){ return 1; } return 0; }"
    sig = extract_signature_from_source(js, "foo", language="javascript")
    assert sig.vector[0] > 0
