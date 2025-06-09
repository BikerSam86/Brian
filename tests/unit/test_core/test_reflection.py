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


def test_spiral_hash_changes():
    log1 = ReflectionLog(state="a", spin="x")
    log2 = ReflectionLog(state="b", spin="x")
    assert log1.spiral_hash != log2.spiral_hash


def test_to_markdown():
    log = ReflectionLog()
    log.log("note", ["spiral_flip"], mood="playful")
    md = log.to_markdown()
    assert md.startswith("-")


def test_emit_mesh(monkeypatch):
    log = ReflectionLog()
    log.log("hello", ["spiral_flip"], mood="playful")

    records = []

    def fake(event_type, payload, phase=None, origin=None, verbose=False):
        records.append((event_type, payload))

    monkeypatch.setattr("tsal.core.mesh_logger.log_event", fake)
    log.emit_mesh()
    assert records and records[0][0] == "REFLECTION"
