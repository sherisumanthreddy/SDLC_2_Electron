import check

b = [' ' for x in range(10)]
B = ['x' for x in range(10)]


def test_is_board_full():
    assert check.is_board_full(b) == 0
    assert check.is_board_full(B) == 1
