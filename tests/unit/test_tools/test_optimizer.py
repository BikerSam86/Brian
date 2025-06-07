import textwrap
from tsal.tools.brian import SymbolicOptimizer, spiral_optimize
from tsal.core.spiral_vector import SpiralVector

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


def test_spiral_optimize():
    vecs = [
        SpiralVector("a", 1.0, 1.0, "a"),
        SpiralVector("b", 2.0, 0.5, "b"),
        SpiralVector("c", 0.5, 2.0, "c"),
    ]
    ordered = spiral_optimize(vecs)
    assert [v.name for v in ordered][0] == "c"
