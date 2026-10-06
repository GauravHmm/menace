from menace.game import Game
from menace.menace import Menace
from menace.board import Board
import pytest

def test_game_starts_with_empty_board():
    game = Game()

    assert game.board.serialize() == "---------"


def test_game_starts_with_x_turn():
    game = Game()

    assert game.board.current_player == "X"


def test_game_starts_with_empty_history():
    game = Game()

    assert game.history == []

def test_game_can_make_menace_move():
    game = Game()
    menace = Menace()

    game.menace_move(menace)

    assert len(game.board.legal_moves()) == 8

def test_game_records_menace_move():
    game = Game()
    menace = Menace()

    game.menace_move(menace)

    assert len(game.history) == 1

def test_game_starts_not_over():
    game=Game()

    assert game.is_over()==False

def test_game_result_when_x_wins():
    game = Game()

    game.board = Board.from_serialized(
        "XXXOO----",
        "X"
    )

    assert game.result() == "win"
def test_game_result_when_o_wins():
    game = Game()

    game.board = Board.from_serialized(
        "OOOXX----",
        "X"
    )

    assert game.result() == "loss"

def test_game_result_when_draw():
    game = Game()

    game.board = Board.from_serialized(
        "XOXOOXXXO",
        "X"
    )

    assert game.result() == "draw"

def test_game_can_teach_menace_after_game():
    game = Game()
    menace = Menace()

    game.board = Board.from_serialized(
        "XXXOO----",
        "X"
    )

    game.history = [
        ("---------", 0)
    ]

    matchbox = menace.get_matchbox(Board())

    before = matchbox.beads[0]

    game.learn(menace)

    assert matchbox.beads[0] == before + 3

def test_game_cannot_teach_menace_before_game_is_over():
    game = Game()
    menace = Menace()

    with pytest.raises(ValueError):
        game.learn(menace)