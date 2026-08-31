from menace.board import Board
def transform(board,mapping):
    cells=[None]*9
    for i in range(9):
        cells[mapping[i]]=board.get(i)
    new_board=Board.from_cells(cells,board.current_player)
    return new_board

IDENTITY = (0, 1, 2, 3, 4, 5, 6, 7, 8)

ROTATE_90 = (2, 5, 8, 1, 4, 7, 0, 3, 6)

ROTATE_180=(8,7,6,5,4,3,2,1,0)

ROTATE_270 = (6, 3, 0, 7, 4, 1, 8, 5, 2)

REFLECT_HORIZONTAL = (6, 7, 8, 3, 4, 5, 0, 1, 2)

REFLECT_VERTICAL = (2, 1, 0, 5, 4, 3, 8, 7, 6)

REFLECT_MAIN_DIAGONAL = (0, 3, 6, 1, 4, 7, 2, 5, 8)

REFLECT_ANTI_DIAGONAL = (8, 5, 2, 7, 4, 1, 6, 3, 0)
