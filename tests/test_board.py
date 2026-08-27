import pytest

from menace.board import Board


def test_empty_board():
    board = Board()

    assert board.legal_moves() == list(range(9))
    assert board.current_player == "X"


def test_moves_alternate():
    board = Board()

    board.make_move(0)
    board.make_move(4)

    assert board.cells[0] == "X"
    assert board.cells[4] == "O"
    assert board.current_player == "X"


def test_occupied_position():
    board = Board()

    board.make_move(0)

    with pytest.raises(ValueError):
        board.make_move(0)


def test_invalid_position():
    board = Board()

    with pytest.raises(ValueError):
        board.make_move(9)

    with pytest.raises(ValueError):
        board.make_move(-1)


def test_x_wins():
    board = Board()

    board.make_move(0)  # X
    board.make_move(3)  # O
    board.make_move(1)  # X
    board.make_move(4)  # O
    board.make_move(2)  # X

    assert board.winner() == "X"
    assert board.is_draw() is False
    assert board.is_game_over() is True


def test_o_wins():
    board = Board()

    board.make_move(0)  # X
    board.make_move(3)  # O
    board.make_move(1)  # X
    board.make_move(4)  # O
    board.make_move(8)  # X
    board.make_move(5)  # O

    assert board.winner() == "O"
    assert board.is_draw() is False
    assert board.is_game_over() is True


def test_diagonal_win():
    board = Board()

    board.make_move(0)  # X
    board.make_move(1)  # O
    board.make_move(4)  # X
    board.make_move(2)  # O
    board.make_move(8)  # X

    assert board.winner() == "X"
    assert board.is_game_over() is True


def test_draw():
    board = Board()

    moves = [0, 1, 2, 4, 3, 5, 6, 8, 7]

    for move in moves:
        board.make_move(move)

    assert board.winner() =='X'
    assert board.is_draw() is False
    assert board.is_game_over() is True

def test_game_still_running():
    board = Board()

    board.make_move(0)
    board.make_move(4)

    assert board.winner() is None
    assert board.is_draw() is False
    assert board.is_game_over() is False

def test_empty_board_serialization():
    board = Board()

    assert board.serialize() == "---------"


def test_board_serialization():
    board = Board()

    board.make_move(0)  # X
    board.make_move(4)  # O
    board.make_move(8)  # X

    assert board.serialize() == "X---O---X"