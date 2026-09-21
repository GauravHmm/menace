from menace.menace import Menace
from menace.board import Board
from menace.canonical import canonicalize, canonical_to_actual_move

def test_menace_starts_with_no_matchboxes():
    menace = Menace()

    assert menace.matchboxes == {}


def test_menace_can_store_matchbox():
    menace = Menace()

    menace.matchboxes["---------"] = "test"

    assert menace.matchboxes["---------"] == "test"

def test_get_matchbox_creates_matchbox():
    menace = Menace()
    board = Board()

    matchbox = menace.get_matchbox(board)

    assert matchbox.state == "---------"
    assert matchbox.beads == {
        0: 4,
        1: 4,
        4: 4
    }

def test_get_matchbox_reuses_existing_matchbox():
    menace = Menace()
    board = Board()

    matchbox1 = menace.get_matchbox(board)
    matchbox2 = menace.get_matchbox(board)

    assert matchbox1 is matchbox2
    assert len(menace.matchboxes) == 1

def test_symmetric_boards_use_same_matchbox():
    menace = Menace()

    board1 = Board()
    board1.make_move(0)

    board2 = Board()
    board2.make_move(2)

    matchbox1 = menace.get_matchbox(board1)
    matchbox2 = menace.get_matchbox(board2)

    assert matchbox1 is matchbox2
    assert len(menace.matchboxes) == 1

def test_menace_can_generate_all_matchboxes():
    menace = Menace()

    menace.generate_matchboxes()

    assert len(menace.matchboxes) == 304

def test_generated_matchboxes_have_beads():
    menace = Menace()

    menace.generate_matchboxes()

    for matchbox in menace.matchboxes.values():
        assert len(matchbox.beads) > 0
        assert all(count > 0 for count in matchbox.beads.values())

def test_generated_initial_matchbox():
    menace = Menace()

    menace.generate_matchboxes()

    matchbox = menace.matchboxes["---------"]

    assert matchbox.beads == {
        0: 4,
        1: 4,
        4: 4
    }

def test_generation_does_not_revisit_same_state():
    menace = Menace()

    visited = set()
    menace._generate_matchboxes(Board(), visited)

    assert len(visited) > 0

def test_generation_matchbox_distribution_valid():
    menace=Menace()
    x_moves={0:0,1:0,2:0,3:0}
    menace.generate_matchboxes()
    for matchbox in menace.matchboxes.values():
        x_moves[matchbox.state.count("X")]+=1

    assert x_moves[0]==1
    assert x_moves[1]==12
    assert x_moves[2]==108
    assert x_moves[3]==183

def test_menace_can_choose_move():
    menace = Menace()
    board = Board()

    move,_ = menace.choose_move(board)

    assert move in board.legal_moves()

def test_menace_maps_canonical_move_to_actual_move():
    menace = Menace()

    board = Board.from_serialized(
        "X--------",
        "O"
    )

    matchbox = menace.get_matchbox(board)

    matchbox.choose_move = lambda: 0

    _, mapping = canonicalize(board)

    expected_move = canonical_to_actual_move(0, mapping)

    actual_move,_ = menace.choose_move(board)

    assert actual_move == expected_move

def test_menace_returns_move_and_learning_record():
    menace=Menace()
    board=Board()

    move,record=menace.choose_move(board)

    state,canonical_move=record

    assert move in board.legal_moves()
    assert state=="---------"
    assert canonical_move in (0,1,4)

def test_menace_rewards_moves_after_win():
    menace=Menace()
    board=Board()

    move,record=menace.choose_move(board)

    state,canonical_move=record
    matchbox=menace.matchboxes[state]

    before=matchbox.beads[canonical_move]

    menace.learn([record],"win")

    assert matchbox.beads[canonical_move]==before+3

def test_menace_rewards_moves_after_draw():
    menace=Menace()
    board=Board()

    move,record=menace.choose_move(board)

    state,canonical_move=record
    matchbox=menace.matchboxes[state]

    before=matchbox.beads[canonical_move]

    menace.learn([record],"draw")

    assert matchbox.beads[canonical_move]==before+1

def test_menace_penalizes_moves_after_loss():
    menace=Menace()
    board=Board()

    move,record=menace.choose_move(board)

    state,canonical_move=record
    matchbox=menace.matchboxes[state]

    before=matchbox.beads[canonical_move]

    menace.learn([record],"loss")

    assert matchbox.beads[canonical_move]==before-1