from menace.board import Board
from menace.canonical import canonicalize


def test_empty_board_is_canonical():
    board = Board()

    state, mapping = canonicalize(board)

    assert state == "---------X"
    assert mapping == (0, 1, 2, 3, 4, 5, 6, 7, 8)


def test_rotated_boards_have_same_canonical_state():
    board1 = Board()
    board1.make_move(0)

    board2 = Board()
    board2.make_move(2)

    state1, _ = canonicalize(board1)
    state2, _ = canonicalize(board2)

    assert state1 == state2


def test_reflected_boards_have_same_canonical_state():
    board1 = Board()
    board1.make_move(0)

    board2 = Board()
    board2.make_move(2)

    state1, _ = canonicalize(board1)
    state2, _ = canonicalize(board2)

    assert state1 == state2


def test_canonicalization_does_not_modify_board():
    board = Board()

    board.make_move(0)
    board.make_move(4)

    original = board.serialize()
    player = board.current_player

    canonicalize(board)

    assert board.serialize() == original
    assert board.current_player == player


def test_current_player_is_part_of_canonical_state():
    board1 = Board.from_cells(
        ["X", None, None,
         None, "O", None,
         None, None, None],
        "X"
    )

    board2 = Board.from_cells(
        ["X", None, None,
         None, "O", None,
         None, None, None],
        "O"
    )

    state1, _ = canonicalize(board1)
    state2, _ = canonicalize(board2)

    assert state1 != state2