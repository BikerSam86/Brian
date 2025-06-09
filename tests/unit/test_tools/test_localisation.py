from seedrunner_cli import localize, get_pron


def test_localize_fr():
    assert localize("Joker", "fr") == "Bouffon"


def test_get_pron():
    assert get_pron("Joker") == "/ˈdʒoʊ.kər/"
