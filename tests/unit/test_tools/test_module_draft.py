from tsal.tools.module_draft import generate_template
import textwrap


def test_generate_template(tmp_path):
    sample = tmp_path / "sample.py"
    sample.write_text(textwrap.dedent(
        """
        import os

        def foo(x):
            return x + 1

        class Bar:
            def baz(self):
                return 2
        """
    ))
    template = generate_template(sample)
    assert "def foo" in template
    assert "class Bar" in template
    assert template.count("pass") == 2
