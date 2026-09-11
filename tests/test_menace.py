from menace.menace import Menace
from menace.board import Board

def test_menace_starts_with_no_matchboxes():
    menace = Menace()

    assert menace.matchboxes == {}


def test_menace_can_store_matchbox():
    menace = Menace()

    menace.matchboxes["---------"] = "test"

    assert menace.matchboxes["---------"] == "test"

def test_get_matchbox_creates_matchbox():
    menace = Menace()
    board = Board()

    matchbox = menace.get_matchbox(board)

    assert matchbox.state == "---------"
    assert matchbox.beads == {
        0: 4,
        1: 4,
        4: 4
    }

def test_get_matchbox_reuses_existing_matchbox():
    menace = Menace()
    board = Board()

    matchbox1 = menace.get_matchbox(board)
    matchbox2 = menace.get_matchbox(board)

    assert matchbox1 is matchbox2
    assert len(menace.matchboxes) == 1

def test_symmetric_boards_use_same_matchbox():
    menace = Menace()

    board1 = Board()
    board1.make_move(0)

    board2 = Board()
    board2.make_move(2)

    matchbox1 = menace.get_matchbox(board1)
    matchbox2 = menace.get_matchbox(board2)

    assert matchbox1 is matchbox2
    assert len(menace.matchboxes) == 1

def test_menace_can_generate_all_matchboxes():
    menace = Menace()

    menace.generate_matchboxes()

    assert len(menace.matchboxes) == 304

def test_generated_matchboxes_have_beads():
    menace = Menace()

    menace.generate_matchboxes()

    for matchbox in menace.matchboxes.values():
        assert len(matchbox.beads) > 0
        assert all(count > 0 for count in matchbox.beads.values())

def test_generated_initial_matchbox():
    menace = Menace()

    menace.generate_matchboxes()

    matchbox = menace.matchboxes["---------"]

    assert matchbox.beads == {
        0: 4,
        1: 4,
        4: 4
    }

