from tsal.core import DynamicLogicGate


def test_logic_gate_lock_toggle():
    gate = DynamicLogicGate(unlock_sequence=[1, 0])
    assert gate.process(1) == 1
    assert gate.locked is False
    gate.process(0)
    assert gate.locked is True
    gate.process(1)
    gate.process(0)
    assert gate.locked is False


def test_logic_gate_plasticity_and_simulation():
    gate = DynamicLogicGate(threshold_a=1.0)
    out1 = gate.process(0.5)
    assert out1 == 0
    gate.process(1.5, reward=1.0)
    assert gate.threshold_a > 1.0
    prev = gate.threshold_a
    gate.process(1.5, reward=1.0, simulate=True)
    assert gate.threshold_a == prev
