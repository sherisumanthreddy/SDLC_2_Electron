import winnercheck

def test_who_is_winner():
    play_board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
    assert winnercheck.who_is_winner() == None
   # assert winnercheck.who_is_winner() == False
        # row
    #play_board[1] = play_board[2] = play_board[3] != '-'
    #assert winnercheck.who_is_winner() == play_board[1]
    # column
    #play_board[1] = play_board[4] = play_board[7] = 'O'
    #assert winnercheck.who_is_winner() == True
    # diagonal
    #play_board[1] = play_board[5] = play_board[9] = 'O'
    #assert winnercheck.who_is_winner() == True
    # row
    #play_board[1] = play_board[2] = play_board[3] = 'X'
    #assert winnercheck.who_is_winner() == True
    # column
    #play_board[1] = play_board[4] = play_board[7] = 'X'
    #assert winnercheck.who_is_winner() == True
    # diagonal
    #play_board[1] = play_board[5] = play_board[9] = 'X'
    #assert winnercheck.who_is_winner() == True'''