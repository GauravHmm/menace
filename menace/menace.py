from menace.canonical import canonicalize
from menace.matchbox import create_matchbox
from menace.board import Board

class Menace:
    def __init__(self):
        self.matchboxes = {}

    def get_matchbox(self, board):
        canonical_state, _ = canonicalize(board)

        if canonical_state not in self.matchboxes:
            self.matchboxes[canonical_state] = create_matchbox(board)

        return self.matchboxes[canonical_state]
    
    def generate_matchboxes(self):
        self._generate_matchboxes(Board())

    def _generate_matchboxes(self,board):
        if board.is_game_over():
            return
        if board.current_player == "X" and board.cells.count("X") < 4:
            canonical_state,_=canonicalize(board)

            if canonical_state not in self.matchboxes:
                matchbox=create_matchbox(board)
                self.matchboxes[canonical_state]=matchbox

        for position in board.legal_moves():
            cells = list(board.cells)

            cells[position]=board.current_player

            if board.current_player=="X":
                next_player = "O"
            else:
                next_player = "X"

            next_board=Board.from_cells(cells,next_player)

            self._generate_matchboxes(next_board)


