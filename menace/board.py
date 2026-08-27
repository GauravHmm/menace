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

    def winner(self):
        winning_lines = [(0, 1, 2),
                         (3, 4, 5),
                         (6, 7, 8),
                         (0, 3, 6),
                         (1, 4, 7),
                         (2, 5, 8),
                         (0, 4, 8),
                         (2, 4, 6),]
        for x in winning_lines:
            first=self.cells[x[0]]
            second=self.cells[x[1]]
            third=self.cells[x[2]]
            if first is not None:
                if first==second and first==third:
                    return first
        return

    def is_draw(self):
        if self.winner():
            return False
        if(len(self.legal_moves())) == 0:
            return True
        return False

    def is_game_over(self):
        if self.winner():
            return True

        if self.is_draw():
            return True

        return False

    