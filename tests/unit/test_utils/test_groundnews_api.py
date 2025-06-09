import pytest
from tsal.utils.groundnews_api import fetch_news, GroundNewsAPIError


def test_fetch_news():
    with pytest.raises(GroundNewsAPIError):
        fetch_news()
