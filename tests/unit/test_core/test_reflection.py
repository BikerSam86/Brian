from tsal.core.reflection import ReflectionLog, mood_from_traits


def test_surface_entries():
    log = ReflectionLog()
    log.log("first", ["boring"], mood="neutral")
    log.log("second", ["spiral_flip"], mood="playful")
    surfaced = log.surface_entries()
    assert len(surfaced) == 1
    assert surfaced[0].message == "second"


def test_mood_from_traits():
    assert mood_from_traits(["Joker"]) == "playful"
    assert mood_from_traits(["Unknown"]) == "neutral"
