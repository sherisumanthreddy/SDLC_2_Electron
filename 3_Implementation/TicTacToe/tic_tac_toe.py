board = [' ' for x in range(10)]

def insert_letter(letter,pos):
    board[pos] = letter

def take_input():
    opt = input("Do you want to play? (y/n) : ")
    return opt

def take_move():
    move = input("Select a position to enter the X between 1 to 9 : ")
    return move

def space_is_free(pos):
    return board[pos] == ' '

def print_board(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7]  + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def is_board_full(board):
    if board.count(' ') != 1:
        return False
    else:
        return True

def is_winner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def player_move():
    run = True
    while run:
        move = take_move()
        try:
            move = int(move)
            if move > 0 and move < 10:
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
        if i in [2,4,6,8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
        return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to tic-tac-toe game!")
    print_board(board)
    if is_board_full(board):
        print("Tie game")
    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
            if is_board_full(board):
                print("Tie game")
                break
        else:
            print("You loose! try again")
            break

        if not(is_winner(board, 'X')):
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
