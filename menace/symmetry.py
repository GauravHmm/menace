from menace.board import Board
def transform(board,mapping):
    cells=[None]*9
    for i in range(9):
        cells[mapping[i]]=board.get(i)
    new_board=Board.from_cells(cells,board.current_player)
    return new_board

IDENTITY = (0, 1, 2, 3, 4, 5, 6, 7, 8)

ROTATE_90 = (2, 5, 8, 1, 4, 7, 0, 3, 6)
