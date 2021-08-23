from . import check
from . import playermove
from . import printboard
from . import winner
from . import computermove
from . import insertletter


def main_function(board):
    """Function of main program"""
    print("Welcome to tic-tac-toe game!")
    printboard.print_board(board)
    if check.is_board_full(board):
        print("Tie game")
    while not (check.is_board_full(board)):
        if not (winner.is_winner(board, 'O')):
            playermove.player_move(board)
            printboard.print_board(board)

            if check.is_board_full(board):
                print("Tie game")
                break
        else:
            print("You loose! try again")
            break

        if not (winner.is_winner(board, 'X')):
            move = computermove.computer_move(board)

            if move == 0:
                print(" ")
            else:
                insertletter.insert_letter(board, 'O', move)
                print('computer placed an o on position', move, ':')
                printboard.print_board(board)
                if check.is_board_full(board):
                    print("Tie game")
                    break
        else:
            print("You win!")
            break
