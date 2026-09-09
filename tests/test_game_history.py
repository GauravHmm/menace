def test_history_stores_matchbox_state_and_move():
    history = []

    history.append(("---------", 0))

    assert history == [
        ("---------", 0)
    ]


def test_history_can_store_multiple_moves():
    history = []

    history.append(("---------", 0))
    history.append(("X---O----", 1))

    assert history == [
        ("---------", 0),
        ("X---O----", 1)
    ]