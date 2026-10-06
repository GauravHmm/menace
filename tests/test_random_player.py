from menace.board import Board
from menace.randomplayer import RandomPlayer

def test_random_player_chooses_legal_move():
    player = RandomPlayer()
    board = Board()

    move = player.choose_move(board)

    assert move in board.legal_moves()

def test_random_player_does_not_choose_occupied_square():
    player = RandomPlayer()
    board = Board()

    board.make_move(4)

    move = player.choose_move(board)

    assert move in board.legal_moves()
    assert move != 4