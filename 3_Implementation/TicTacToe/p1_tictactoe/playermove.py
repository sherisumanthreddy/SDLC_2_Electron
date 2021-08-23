from . import insertletter
from . import spacefree
from . import takemove


def player_move(board):
    """Function to check whether the position is occupied"""
    run = True
    while run:
        move = takemove.take_move()
        if move > 100:
            move = int(move)
            if 0 < move < 10:
                if spacefree.space_is_free(board, move):
                    run = False
                    insertletter.insert_letter(board, 'X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Select a number between 1 and 9 : ')

        else:
            print('Please type a number')
