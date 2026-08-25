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