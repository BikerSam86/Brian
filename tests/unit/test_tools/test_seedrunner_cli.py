from seedrunner_cli import hash_stack


def test_hash_stack_deterministic():
    seeds = ["A", "B"]
    assert hash_stack(seeds) == hash_stack(seeds)

