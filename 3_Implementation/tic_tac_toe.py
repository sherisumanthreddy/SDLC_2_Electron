"""import random module"""
import random
import turtle
import game2048 as new


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
    #move = input("Select a position to enter the X between 1 to 9 : ")
    #new.pen.penup()
	#new.pen.clear()
	
	
    return 1

def space_is_free(pos):
    """Function to check whether space is free or not"""
    return board[pos] == ' '

def print_board(board):
	new.pen.color("white")
	new.pen.penup()
	increment = 0
	for i in range(1, 4):
		new.pen.goto(-110+increment, 60)
		new.pen.write(board[i], font=('Arial', 35, 'bold'))
		increment += 85
	new.pen.penup()
	new.pen.goto(-110, -130)
	increment = 0
	for j in range(4, 7):
		new.pen.goto(-110+increment, -30)
		new.pen.write(board[j], font=('Arial', 35, 'bold'))
		increment += 85
	new.pen.penup()
	new.pen.goto(-110, 200)
	increment = 0
	for k in range(7, 10):
		new.pen.goto(-110+increment, -110)
		new.pen.write(board[k], font=('Arial', 35, 'bold'))
		increment += 85

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

def player_move(Xmark):
    """Function for player move"""
    move = int(Xmark)
    if 0 < move < 10:
        if space_is_free(move):
            run = False
            insert_letter('X', move)
    print_board(board)

def computer_move():
    """Function for computer move"""
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    #print(possible_moves)
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
	
	

#---------------------------------#
def draw_hashtag():
	new.pen.clear()
	new.pen.penup()
	new.pen.fillcolor("white")	#start filling color, finish it when there is a complete closed boundary
	new.pen.begin_fill()
	new.pen.goto(-60, 120)
	for _ in range(2):	#forming a square
		new.pen.forward(15)
		new.pen.right(90)
		new.pen.forward(250)
		new.pen.right(90)
	new.pen.end_fill()	#boundary complete, fill the color)
	new.pen.penup()
	new.pen.goto(30, 120)
	new.pen.fillcolor("white")
	new.pen.begin_fill()
	for _ in range(2):	#forming a square
		new.pen.forward(15)
		new.pen.right(90)
		new.pen.forward(250)
		new.pen.right(90)
	new.pen.end_fill()
	new.pen.penup()
	
	new.pen.goto(-130, 50)
	new.pen.fillcolor("white")
	new.pen.begin_fill()
	for _ in range(2):	#forming a square
		new.pen.forward(250)
		new.pen.right(90)
		new.pen.forward(15)
		new.pen.right(90)
	new.pen.end_fill()
	new.pen.penup()
	new.pen.goto(-130, -40)
	new.pen.fillcolor("white")
	new.pen.begin_fill()
	for _ in range(2):	#forming a square
		new.pen.forward(250)
		new.pen.right(90)
		new.pen.forward(15)
		new.pen.right(90)
	
	new.pen.end_fill()	#boundary complete, fill the color)
	new.pen.penup()
	
	new.pen.goto(-90, -150)
	new.pen.color("white")
	new.pen.write("'E' for menu", font=('Arcade Interlaced', 12))
	new.pen.penup()

def draw_tictac_grid(Xmark=0, testing=False):
	new.IN_MENU = False
	new.TICTAC = True	#jsut in case
	
	new.window.bgcolor("black")
	draw_hashtag()	#draw that hashtag XD
	
	if not(is_board_full(board)):
		if not(is_winner(board, 'O')):
			player_move(Xmark)
			print_board(board)
			if is_board_full(board):	#TIE!!
				if not testing:
					print("Tie game")
		else:
			if not testing:
				print("You loose! try again")
			
			
		if not (is_winner(board, 'X')):
			move = computer_move()
			insert_letter('O', move)
			print_board(board)
			if is_board_full(board):
				if not testing:
					print("Tie game")
		else:
			if not testing:
				print("You win!")
	#print(new.TESTING)
	
	
	# player_move(Xmark)
	# print_board(board)
	# move = computer_move()
	# insert_letter('O', move)
	# print_board(board)

    # while not (is_board_full(board)):
        # if not (is_winner(board, 'O')):
            # player_move()
            # print_board(board)
            # if is_board_full(board):
                # print("Tie game")
                # break
        # else:
            # print("You loose! try again")
            # break

        # if not (is_winner(board, 'X')):
            # move = computer_move()
            # if move == 0:
                # print(" ")
            # else:
                # insert_letter('O', move)
                # print('computer placed an o on position', move, ':')
                # print_board(board)
                # if is_board_full(board):
                    # print("Tie game")
                    # break
        # else:
            # print("You win!")
            # break





#---------------------------------#



    

# while True:
    # x = take_input()
    # if x.lower() == 'y':
        # board = [' ' for x in range(10)]
        # print('--------------------')
        # main()
    # else:
        # break
