from tsal.core.module_registry import registry


def test_lookup_by_name():
    meta = registry.get("anti_entropy_engine")
    assert meta and meta.nickname == "entropy_bitch_slapper"


def test_lookup_by_alias():
    meta = registry.get("coherence_rebuilder")
    assert meta and meta.name == "anti_entropy_engine"

