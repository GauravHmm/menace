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

    def result(self):
        if not self.is_over():
            raise ValueError("Game is not over")
        if self.board.is_draw():
            return "draw"
        if self.board.winner() == "X":
            return "win"
        return "loss"

    def learn(self,menace):
        result=self.result()
        menace.learn(self.history,result)