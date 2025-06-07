import textwrap
from tsal.tools.brian import SymbolicOptimizer

def test_annotate_code(tmp_path):
    sample = tmp_path / "sample.py"
    sample.write_text(textwrap.dedent(
        """
        def beta():
            return 2

        def alpha():
            return 1
        """
    ))

    opt = SymbolicOptimizer()
    annotated = opt.annotate_code(sample.read_text())

    assert annotated.startswith("# Suggested order:")
    assert "def beta" in annotated and "def alpha" in annotated
    # two functions should get energy docstrings
    assert annotated.count("OPTENERGY") == 2


def test_repair_file(tmp_path):
    sample = tmp_path / "module.py"
    sample.write_text(textwrap.dedent(
        """
        def alpha():
            pass

        def beta():
            pass
        """
    ))

    opt = SymbolicOptimizer(target_signatures={"alpha": [10, 0, 0], "beta": [0, 0, 0]})
    suggestions = opt.repair_file(str(sample))

    # file should now have beta defined before alpha
    new_contents = sample.read_text()
    assert new_contents.startswith("def beta")
    assert any("alpha" in s for s in suggestions)
    assert len(suggestions) == 2
