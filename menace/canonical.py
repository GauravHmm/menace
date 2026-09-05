from menace.symmetry import transform, TRANSFORMATIONS,inverse_mapping
from menace.board import Board

def canonicalize(board):
    best_state = None
    best_mapping = None

    for mapping in TRANSFORMATIONS:
        transformed = transform(board, mapping)

        state = transformed.serialize()

        if best_state is None or state < best_state:
            best_state = state
            best_mapping = mapping

    return best_state, best_mapping

def canonical_to_actual_move(canonical_move, mapping):
    inverse = inverse_mapping(mapping)
    return inverse[canonical_move]

def canonical_moves(board):
    seen_states = set()
    moves=[]
    for position in board.legal_moves():
        cells = list(board.cells)
        cells[position] = board.current_player
        next_player = "O" if board.current_player == "X" else "X"
        temp = Board.from_cells(cells, next_player)
        canonical_state,_=canonicalize(temp)
        if canonical_state not in seen_states:
            seen_states.add(canonical_state)
            moves.append(position)

    return moves


        
