from tsal.tools.reflect import reflect_summary
from tsal.core.rev_eng import Rev_Eng


def test_reflect_summary_contains_origin():
    rev = Rev_Eng(origin="unit")
    summary = reflect_summary(rev)
    assert "\"origin\": \"unit\"" in summary
