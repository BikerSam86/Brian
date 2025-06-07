from tsal.tristar.handshake import handshake
from tsal.core.rev_eng import Rev_Eng


def test_handshake_basic():
    metrics = handshake(0.5, 1.0)
    assert set(metrics.keys()) == {"delta", "potential", "resonance"}


def test_handshake_logs(monkeypatch):
    events = []
    rev = Rev_Eng(origin="unit")

    def fake_log_event(action: str, **details):
        events.append((action, details))

    monkeypatch.setattr(rev, "log_event", fake_log_event)
    handshake(0.1, 0.2, rev)
    assert events and events[0][0] == "TRISTAR_HANDSHAKE"
