from menace.board import Board
from menace.symmetry import (
    IDENTITY,
    ROTATE_90,
    ROTATE_180,
    ROTATE_270,
    transform,
)


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

def test_rotate_180():
    board = Board()

    board.make_move(0)  # X
    board.make_move(1)  # O

    transformed = transform(board, ROTATE_180)

    assert transformed.serialize() == "-------OX"

def test_two_rotate_90_equals_rotate_180():
    board = Board()

    board.make_move(0)  # X
    board.make_move(4)  # O
    board.make_move(1)  # X

    rotated_twice = transform(
        transform(board, ROTATE_90),
        ROTATE_90
    )

    rotated_180 = transform(board, ROTATE_180)

    assert rotated_twice.serialize() == rotated_180.serialize()

def test_four_rotate_90_returns_original():
    board = Board()

    board.make_move(0)  # X
    board.make_move(1)  # O
    board.make_move(4)  # X

    transformed = board

    for _ in range(4):
        transformed = transform(transformed, ROTATE_90)

    assert transformed.serialize() == board.serialize()
    assert transformed.current_player == board.current_player

def test_rotate_270_equals_three_rotate_90():
    board = Board()

    board.make_move(0)  # X
    board.make_move(4)  # O
    board.make_move(1)  # X

    rotated_270 = transform(board, ROTATE_270)

    rotated_90_three_times = board

    for _ in range(3):
        rotated_90_three_times = transform(
            rotated_90_three_times,
            ROTATE_90
        )

    assert rotated_270.serialize() == rotated_90_three_times.serialize()

