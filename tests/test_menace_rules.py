from menace.board import Board
from menace.menace_rules import initial_bead_count


def test_first_menace_move_gets_four_beads():
    board = Board()

    assert initial_bead_count(board) == 4


def test_second_menace_move_gets_three_beads():
    board = Board()

    board.make_move(0)
    board.make_move(4)

    assert initial_bead_count(board) == 3


def test_third_menace_move_gets_two_beads():
    board = Board()

    board.make_move(0)
    board.make_move(4)
    board.make_move(1)
    board.make_move(8)

    assert initial_bead_count(board) == 2


def test_fourth_menace_move_gets_one_bead():
    board = Board()

    board.make_move(0)
    board.make_move(4)
    board.make_move(1)
    board.make_move(8)
    board.make_move(2)
    board.make_move(6)

    assert initial_bead_count(board) == 1