"""import random module"""
import random
board = [' ' for x in range(10)]

def insert_letter(letter, pos):
    """Function to insert letter at particular position"""
    board[pos] = letter

def take_input():
    """Function to take input from user whether to play or not"""
    opt = input("Do you want to play? (y/n) : ")
    return opt

def take_move():
    """Function to select position on board by choosing numbers from 1 to 9"""
    move = input("Select a position to enter the X between 1 to 9 : ")
    return move

def space_is_free(pos):
    """Function to check whether space is free or not"""
    return board[pos] == ' '

def print_board(board):
    """Function to design tic-tac-toe board"""
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def is_board_full(board):
    """Function to check  board is full"""
    if board.count(' ') != 1:
        return False
    else:
        return True

def is_winner(b, ch):
    """Function for checking winner"""
    return ((b[1] == ch and b[2] == ch and b[3] == ch) or
            (b[4] == ch and b[5] == ch and b[6] == ch) or
            (b[7] == ch and b[8] == ch and b[9] == ch) or
            (b[1] == ch and b[4] == ch and b[7] == ch) or
            (b[2] == ch and b[5] == ch and b[8] == ch) or
            (b[3] == ch and b[6] == ch and b[9] == ch) or
            (b[1] == ch and b[5] == ch and b[9] == ch) or
            (b[3] == ch and b[5] == ch and b[7] == ch))

def player_move():
    """Function for player move"""
    run = True
    while run:
        move = take_move()
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Select a number between 1 and 9 : ')

        except:
            print('Please type a number')

def computer_move():
    """Function for computer move"""
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            boardcopy = board[:]
            boardcopy[i] = let
            if is_winner(boardcopy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
        return move

def select_random(list_num):
    """Function to select random number"""
    length = len(list_num)
    r_int = random.randrange(0, length)
    return list_num[r_int]

def main():
    """Function of main program"""
    print("Welcome to tic-tac-toe game!")
    print_board(board)
    if is_board_full(board):
        print("Tie game")
    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
            if is_board_full(board):
                print("Tie game")
                break
        else:
            print("You loose! try again")
            break

        if not (is_winner(board, 'X')):
            move = computer_move()
            if move == 0:
                print(" ")
            else:
                insert_letter('O', move)
                print('computer placed an o on position', move, ':')
                print_board(board)
                if is_board_full(board):
                    print("Tie game")
                    break
        else:
            print("You win!")
            break

while True:
    x = take_input()
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
