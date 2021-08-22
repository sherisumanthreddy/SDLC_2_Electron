import winner


def test_is_winner():
    b = [' ' for x in range(10)]
    assert winner.is_winner(b, 'o') == False
    assert winner.is_winner(b, 'x') == False
    # row
    b[1] = b[2] = b[3] = 'o'
    assert winner.is_winner(b, 'o') == True
    # column
    b[1] = b[4] = b[7] = 'o'
    assert winner.is_winner(b, 'o') == True
    # diagonal
    b[1] = b[5] = b[9] = 'o'
    assert winner.is_winner(b, 'o') == True
    # row
    b[1] = b[2] = b[3] = 'x'
    assert winner.is_winner(b, 'x') == True
    # column
    b[1] = b[4] = b[7] = 'x'
    assert winner.is_winner(b, 'x') == True
    # diagonal
    b[1] = b[5] = b[9] = 'x'
    assert winner.is_winner(b, 'x') == True
