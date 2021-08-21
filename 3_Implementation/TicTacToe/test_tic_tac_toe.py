import tic_tac_toe

board = tic_tac_toe.board

def test_insertletter():
    Letter = 'X'
    Pos = 0

    tic_tac_toe.insertLetter(Letter, Pos)

    assert board[Pos] == 'X'
    assert board[Pos] != 'O'

""" 
THis is how you write test.
* Note you need to cd into TicTacToe Folder and 
* execute " pytest -s " inside this folder
* if pytest is not installed you can try opening cmd and running "pip install pytest"
"""