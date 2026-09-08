from menace.board import Board
from menace.canonical import canonicalize, canonical_moves
from menace.menace_rules import initial_bead_count
import random

class Matchbox:
    def __init__(self,state,beads):
        self.state=state
        self.beads=beads

    def choose_move(self):
        moves=list(self.beads.keys())
        weights=list(self.beads.values())

        return random.choices(moves,weights=weights,k=1)[0]
    def remove_bead(self,move):
        self.beads[move]-=1
        


def create_matchbox(board):
    canonical_state,_=canonicalize(board)
    canonical_board = Board.from_serialized(
    canonical_state,
    board.current_player)
    moves = canonical_moves(canonical_board)
    bead_count = initial_bead_count(canonical_board)

    beads={}
    for move in moves:
        beads[move]=bead_count

    return Matchbox(canonical_state,beads)

    
        