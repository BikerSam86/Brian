from tsal.core.spin_algebra import SpinState, combine_spins


def test_combine_spins_inquiry():
    interaction = combine_spins(SpinState.CURIOSITY, SpinState.DUTY)
    assert interaction.result is SpinState.INQUIRY


def test_combine_spins_default():
    interaction = combine_spins(SpinState.DELIGHT, SpinState.DELIGHT)
    assert interaction.result is SpinState.DELIGHT
