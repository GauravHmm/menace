from menace.board import Board
from menace.canonical import canonicalize
from menace.symmetry import transform,TRANSFORMATIONS


def test_empty_board_is_canonical():
    board = Board()

    state, mapping = canonicalize(board)

    assert state == "---------"
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

def test_all_symmetries_have_same_canonical_state():
    board = Board()

    board.make_move(0)
    board.make_move(4)
    board.make_move(1)

    canonical_state, _ = canonicalize(board)

    for mapping in TRANSFORMATIONS:
        transformed = transform(board, mapping)

        state, _ = canonicalize(transformed)

        assert state == canonical_state

