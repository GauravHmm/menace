from menace.board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.history = []

    def menace_move(self,menace):
        move=menace.choose_move(self.board)
        self.board.make_move(move)