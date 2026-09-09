from menace.game import Game


def test_game_starts_with_empty_board():
    game = Game()

    assert game.board.serialize() == "---------"


def test_game_starts_with_x_turn():
    game = Game()

    assert game.board.current_player == "X"


def test_game_starts_with_empty_history():
    game = Game()

    assert game.history == []