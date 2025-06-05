from tsal.core.phase_math import phase_match_enhanced, mesh_phase_sync


def test_phase_match_already_in_phase():
    final_state, energy, metrics = phase_match_enhanced(5.0, 5.0, verbose=True)
    assert final_state == 5.0
    assert energy == 0
    assert metrics["phase_locked"] is True


def test_mesh_phase_sync_structure():
    nodes = {"a": 0.0, "b": 2.0}
    summary = mesh_phase_sync(nodes, 0.0, verbose=True)

    assert set(summary.keys()) == {"nodes", "total_energy", "mesh_resonance", "φ_signature"}
    assert set(summary["nodes"].keys()) == set(nodes.keys())
    for info in summary["nodes"].values():
        assert {"initial", "final", "energy", "metrics"} <= info.keys()
