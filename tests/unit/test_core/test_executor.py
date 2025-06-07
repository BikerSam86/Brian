from tsal.core.executor import TSALExecutor, MetaFlagProtocol
from tsal.core.rev_eng import Rev_Eng


def test_dry_run(monkeypatch):
    rev = Rev_Eng(origin="unit")
    events = []
    monkeypatch.setattr(rev, "log_event", lambda action, **d: events.append((action, d)))
    exe = TSALExecutor(MetaFlagProtocol(dry_run=True, narrative_mode=True), rev=rev)
    exe.execute(0xA, local=0.1, remote=0.2, fork=True)
    assert not exe.op_log
    assert events and events[0][0] == "OP_NARRATIVE"


def test_resonance_logging(monkeypatch):
    rev = Rev_Eng(origin="unit")
    events = []
    monkeypatch.setattr(rev, "log_event", lambda action, **d: events.append((action, d)))
    exe = TSALExecutor(MetaFlagProtocol(resonance_threshold=0.0), rev=rev)
    exe.execute(0xA, local=0.5, remote=1.0)
    assert any(a == "RESONANCE_THRESHOLD" for a, _ in events)


def test_fork_tracking():
    exe = TSALExecutor(MetaFlagProtocol(fork_tracking=True))
    exe.execute(0x9, fork=True)
    assert exe.forks == [1]
