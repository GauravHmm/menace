def initial_bead_count(board):
    menace_moves = 0

    for cell in board.cells:
        if cell == "X":
            menace_moves += 1

    return [4, 3, 2, 1][menace_moves]