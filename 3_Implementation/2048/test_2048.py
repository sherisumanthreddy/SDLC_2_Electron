import game2048

def test_slam_left():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]

    game2048.slam_left()

    assert game2048.gameboard == [[2, 2, 0, 0],
                                  [8, 0, 0, 0],
                                  [4, 0, 0, 0],
                                  [2, 4, 0, 0]]

def test_compress_left():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.compress_left()

    assert game2048.gameboard == [[2, 0, 2, 0],
                                  [0, 0, 0, 8],
                                  [4, 0, 0, 0],
                                  [0, 0, 4, 0]]


def test_transpose():

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]

    assert game2048.transpose(game2048.gameboard) == [[2, 0, 4, 0],
                                                      [0, 0, 0, 0],
                                                      [2, 0, 0, 2],
                                                      [0, 8, 0, 4]]

def test_reverse():

    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 4]]

    assert game2048.reverse(game2048.gameboard) == [[0, 2, 0, 2],
                                                    [8, 0, 0, 0],
                                                    [0, 0, 0, 4],
                                                    [4, 2, 0, 0]]

def test_move_left():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_left(True)
    
    assert game2048.gameboard == [[4, 0, 0, 0],
                                  [8, 0, 0, 0],
                                  [4, 0, 0, 0],
                                  [4, 0, 0, 0]]


def test_move_up():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_up(True)

    assert game2048.gameboard == [[2, 0, 4, 8],
                                  [4, 0, 0, 2],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]]


def test_move_right():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_right(True)

    assert game2048.gameboard == [[0, 0, 0, 4],
                                  [0, 0, 0, 8],
                                  [0, 0, 0, 4],
                                  [0, 0, 0, 4]]


def test_move_down():
    game2048.gameboard = [[2, 0, 2, 0],
                          [0, 0, 0, 8],
                          [4, 0, 0, 0],
                          [0, 0, 2, 2]]

    game2048.move_down(True)

    assert game2048.gameboard == [[0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [2, 0, 0, 8],
                                  [4, 0, 4, 2]]
