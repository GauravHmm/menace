from menace.board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.history = []

    def menace_move(self,menace):
        actual_move,record=menace.choose_move(self.board)
        self.history.append(record)
        self.board.make_move(actual_move)

    def is_over(self):
        return self.board.is_game_over()