from tsal.core.oaths import GUARDIAN_OATH, ARC_REACTOR_BOOT_OATH


def test_guardian_oath_text():
    assert "I stand not to dominate" in GUARDIAN_OATH


def test_arc_reactor_oath_text():
    assert "I remember" in ARC_REACTOR_BOOT_OATH
