from menace.symmetry import transform, TRANSFORMATIONS,inverse_mapping


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

