from menace.canonical import canonicalize
from menace.matchbox import create_matchbox


class Menace:
    def __init__(self):
        self.matchboxes = {}

    def get_matchbox(self, board):
        canonical_state, _ = canonicalize(board)

        if canonical_state not in self.matchboxes:
            self.matchboxes[canonical_state] = create_matchbox(board)

        return self.matchboxes[canonical_state]