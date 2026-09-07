from menace.board import Board
from menace.matchbox import Matchbox, create_matchbox
from menace.canonical import canonicalize, canonical_moves

def test_matchbox_stores_state():
    matchbox = Matchbox(
        "---------",
        {
            0: 4,
            1: 4,
            4: 4
        }
    )

    assert matchbox.state == "---------"


def test_empty_board_has_three_moves():
    matchbox = Matchbox(
        "---------",
        {
            0: 4,
            1: 4,
            4: 4
        }
    )

    assert matchbox.beads == {
        0: 4,
        1: 4,
        4: 4
    }

def test_bead_count_is_applied_to_each_move():
    beads = {0: 2, 1: 2, 4: 2}

    matchbox = Matchbox("X-------O", beads)

    assert all(count == 2 for count in matchbox.beads.values()) 

def test_create_matchbox_for_second_menace_move():
    board = Board()

    board.make_move(0)  # MENACE
    board.make_move(4)  # opponent

    matchbox = create_matchbox(board)

    assert matchbox.state == canonicalize(board)[0]

    assert all(count == 3 for count in matchbox.beads.values())
    assert all(move in canonical_moves(
        Board.from_serialized(matchbox.state, board.current_player)
    ) for move in matchbox.beads)

def test_create_matchbox_for_third_menace_move():
    board = Board()

    board.make_move(0)  # MENACE
    board.make_move(4)  # opponent
    board.make_move(1)  # MENACE
    board.make_move(8)  # opponent

    matchbox = create_matchbox(board)

    assert all(count == 2 for count in matchbox.beads.values())

def test_choose_move_returns_available_move():
    beads = {
        0: 4,
        1: 4,
        4: 4
    }

    matchbox = Matchbox("---------", beads)

    move = matchbox.choose_move()

    assert move in beads

def test_choose_move_never_selects_zero_bead_move():
    beads = {
        0: 0,
        1: 4,
        4: 4
    }

    matchbox = Matchbox("---------", beads)

    for _ in range(100):
        move = matchbox.choose_move()

        assert move != 0

    