from menace.board import Board
from menace.symmetry import IDENTITY, ROTATE_90, transform


def test_identity():
    board = Board()

    board.make_move(0)  # X
    board.make_move(4)  # O
    board.make_move(8)  # X

    transformed = transform(board, IDENTITY)

    assert transformed.serialize() == board.serialize()
    assert transformed.current_player == board.current_player
    assert transformed is not board


def test_rotate_90():
    board = Board()

    board.make_move(0)  # X
    board.make_move(4)  # O

    transformed = transform(board, ROTATE_90)

    assert transformed.serialize() == "--X-O----"


def test_current_player_preserved():
    board = Board()

    board.make_move(0)  # X

    transformed = transform(board, ROTATE_90)

    assert transformed.current_player == board.current_player


def test_original_board_unchanged():
    board = Board()

    board.make_move(0)  # X
    board.make_move(4)  # O

    original_state = board.serialize()

    transform(board, ROTATE_90)

    assert board.serialize() == original_state