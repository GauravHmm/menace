from menace.menace import Menace


def test_menace_starts_with_no_matchboxes():
    menace = Menace()

    assert menace.matchboxes == {}


def test_menace_can_store_matchbox():
    menace = Menace()

    menace.matchboxes["---------"] = "test"

    assert menace.matchboxes["---------"] == "test"