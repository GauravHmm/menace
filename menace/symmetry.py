def trasnform(board,mapping):
    new_board=[None]*9

    for i in range(9):
        new_board[mapping[i]]=board[i]

    return new_board