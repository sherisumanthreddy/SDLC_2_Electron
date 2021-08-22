def is_board_full(board):
    """Function to check whether board if full or not"""
    if board.count(' ') != 1:
        return False
    else:
        return True