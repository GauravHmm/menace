class Board:
    def __init__(self):
        self._cells = [None] * 9
        self.current_player = "X"

    def legal_moves(self):
        return [i for i, cell in enumerate(self._cells) if cell is None]

    def make_move(self, position):
        if position not in range(9):
            raise ValueError("Position must be between 0 and 8")

        if self._cells[position] is not None:
            raise ValueError("Position is already occupied")

        self._cells[position] = self.current_player
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
            first=self._cells[x[0]]
            second=self._cells[x[1]]
            third=self._cells[x[2]]
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

    def serialize(self):
        result=''
        for cell in self._cells:
            if cell is None:
                result+='-'
            else:
                result+=cell
        return result
    def get(self,position):
        if position not in range(9):
            raise ValueError("Position must be between 0 and 8")
        return self._cells[position]
    @classmethod
    def from_cells(cls,cells,current_player):
        if len(cells)!=9:
            raise ValueError("There must be 9 cells")
        for cell in cells:
            if cell not in("X","O",None):
                raise ValueError("Cell contents must contain X,O or None")
        if current_player not in("X","O"):
            raise ValueError("current player must be either X or O")

        new_board=cls()
        new_board._cells=list(cells)
        new_board.current_player=current_player
        return new_board

    @property
    def cells(self):
        return tuple(self._cells)

    @classmethod
    def from_serialized(cls,state, current_player):
        if len(state)!=9:
            raise ValueError("State must contain exactly 9 characters")
        cells=[]

        for cell in state:
            if cell=='-':
                cells.append(None)
            elif cell in ("X",'O'):
                cells.append(cell)
            else:
                raise ValueError("State can only contain X,O or -")

        return cls.from_cells(cells,current_player)
