from . import selectrandom
from . import winner


def computer_move(board):
    """Function to take computer move"""
    possible_moves = [x for x, letter in enumerate(board)
                      if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner.is_winner(boardcopy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = selectrandom.select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = selectrandom.select_random(edges_open)
        return move
