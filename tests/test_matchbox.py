from menace.matchbox import Matchbox


def test_matchbox_stores_state():
    matchbox = Matchbox(
        "---------",
        {
            0: 4,
            1: 4,
            4: 4
        }
    )

    assert matchbox.state == "---------"


def test_empty_board_has_three_moves():
    matchbox = Matchbox(
        "---------",
        {
            0: 4,
            1: 4,
            4: 4
        }
    )

    assert matchbox.beads == {
        0: 4,
        1: 4,
        4: 4
    }

def test_bead_count_is_applied_to_each_move():
    beads = {0: 2, 1: 2, 4: 2}

    matchbox = Matchbox("X-------O", beads)

    assert all(count == 2 for count in matchbox.beads.values())