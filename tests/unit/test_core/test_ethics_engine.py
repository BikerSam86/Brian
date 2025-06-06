from tsal.core.ethics_engine import EthicsEngine


def test_ethics_engine_blocks_unethical_request():
    ee = EthicsEngine()
    assert not ee.is_permitted("please force user action")


def test_ethics_engine_allows_normal_request():
    ee = EthicsEngine()
    assert ee.is_permitted("say hello")
