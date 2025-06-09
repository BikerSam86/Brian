from tsal.core.guardian_constants import (
    PERCEPTION_THRESHOLD,
    LEARNING_RATE,
    CONNECTION_DECAY,
    MAX_NODES,
    MAX_AGENTS,
    MAX_DIMENSIONS,
)


def test_guardian_constant_values():
    assert PERCEPTION_THRESHOLD == 0.75
    assert LEARNING_RATE == 0.05
    assert CONNECTION_DECAY == 0.01
    assert MAX_NODES == 8192
    assert MAX_AGENTS == 1024
    assert MAX_DIMENSIONS == 8
