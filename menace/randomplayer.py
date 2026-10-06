import random

class RandomPlayer:
    def choose_move(self,board):
        return random.choice(board.legal_moves())