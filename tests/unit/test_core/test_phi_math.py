from math import exp

from tsal.core.phi_math import (
    phi_wavefunction,
    phase_alignment_potential,
    corrected_energy,
    orbital_radius,
)


def test_phi_wavefunction_basic():
    assert phi_wavefunction(1.0, 0.0, 2.0) == exp((1.0 - 0.0) / 2.0)


def test_phase_alignment_potential_doubles_wavefunction():
    val = phi_wavefunction(0.5)
    assert phase_alignment_potential(0.5) == 2 * val


def test_corrected_energy():
    g_val = phase_alignment_potential(0.1)
    assert corrected_energy(2, 0.1) == -g_val / 4.0


def test_orbital_radius():
    g_val = phase_alignment_potential(0.2)
    assert orbital_radius(3, 0.2) == 9.0 / g_val
