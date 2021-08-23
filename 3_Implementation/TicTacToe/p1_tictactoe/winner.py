def is_winner(b, ch):
    """Function to check whether user won"""
    return ((b[1] == ch and b[2] == ch and b[3] == ch) or
            (b[4] == ch and b[5] == ch and b[6] == ch) or
            (b[7] == ch and b[8] == ch and b[9] == ch) or
            (b[1] == ch and b[4] == ch and b[7] == ch) or
            (b[2] == ch and b[5] == ch and b[8] == ch) or
            (b[3] == ch and b[6] == ch and b[9] == ch) or
            (b[1] == ch and b[5] == ch and b[9] == ch) or
            (b[3] == ch and b[5] == ch and b[7] == ch))
