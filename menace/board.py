class Board:
    def __init__(self):
        self.cells = [None] * 9
        self.current_player = "X"

    def legal_moves(self):
        return [i for i, cell in enumerate(self.cells) if cell is None]

    def make_move(self, position):
        if position not in range(9):
            raise ValueError("Position must be between 0 and 8")

        if self.cells[position] is not None:
            raise ValueError("Position is already occupied")

        self.cells[position] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"
