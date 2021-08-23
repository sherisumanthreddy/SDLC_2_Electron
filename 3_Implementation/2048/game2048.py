#libraries imports
import turtle
import random
import pickle
import tic_tac_toe


#our main grid 
gameboard = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


#grid colors
colors = {
        0: "white",
        2: "yellow",
        4: "orange",
        8: "pink",
        16: "red",
        32: "light green",
        64: "green",
        128: "#6C1592",
        256: "purple",
        512: "gold",
        1024: "silver",
        2048: "#ABB5AC"
    }
	
values = [0,1,2,3,4,5,6,7,8]
text_colors = {
	0:"#006600", 1:"#3498DB", 2:"#996633", 3:"#993366", 4:"#5D3AF8", 5:"#22D133", 6:"#C055D4", 7:"#55D4CE", 8:"#0066FF" 
}

#setting uo the screen
window = turtle.Screen()
window.title("Mini arcade games")
window.bgcolor("black")
window.setup(width=450, height=600)
window.tracer(0)

#general purpose pen turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()  # an invisible turtle for drawing buttons

#some constants
CURSOR_SIZE = 20
FONT_SIZE = 16
FONT = ('Arial', FONT_SIZE, 'bold')
ARCADE_FONT = ('Arcade Interlaced', FONT_SIZE, 'bold')

#some multifile bool flags
TESTING = False
IN_MENU = True
TICTAC = False 



## 
#  @brief this adds a number(2 or 4) at a random position in the gameboard grid
#  
#  @return nothing
#  
#  @details 
#  
def pick_random_tile():

    valid = []
    for j in range(4):
        for i in range(4):
            if gameboard[j][i] == 0:
                valid.append((j, i))

    pos = random.choice(valid)
    n = random.random()
    if n >= 0.7: #difficulty selector 
        gameboard[pos[0]][pos[1]] = 4
    else:
        gameboard[pos[0]][pos[1]] = 2
		

## 
#  @brief menu, asks what game you wanna play 
#  
#  @return nothing
#  
#  @details 
#  
def menu():
	global IN_MENU
	IN_MENU = True	#in menu
	
	pen.penup()
	pen.clear()
	tic_tac_toe.new.pen.clear()
	#pen.goto(100, 100)
	window.bgcolor("black")
	window.setup(width = 500, height=450)
	window.title("Mini Arcade Games")
	
	pen.color("white")
	pen.goto(-200,180)
	pen.sety(pen.ycor()-100)
	title = "Mini Arcade Games"
	
	for letters in title:
		index = random.choice(values)
		pen.color(text_colors[index])
		pen.write(str(letters), font=ARCADE_FONT)
		pen.setx(pen.xcor()+FONT_SIZE+8)
	pen.penup()
	#pen.setx(pen.xcor()+300)
	
	turtle.bgpic("bg.png")
	
	#2048 game 
	pen.goto(-100, -95)	#with reference to the drawn canvas
	pen.write("2048 Game", font=ARCADE_FONT)
	pen.penup()
	
	#tictac game
	pen.goto(-140,-165)
	pen.write("TicTacToe Game", font=ARCADE_FONT)
	pen.penup()
	
	#sudoku game
	pen.goto(-120, -130)
	pen.write("Sudoku Game", font=ARCADE_FONT)
	pen.penup()
	
	pen.goto(90, 90)	#back to default position

## 
#  @brief displays the score
#  
#  @return nothing
#  
#  @details 
#  
def draw_score():

	pen.goto(-185, 150)
	pen.color("black")
	pen.write("SCORE: ", font=('Arcade Interlaced', 12))
	pen.goto(-95, 150)
	pen.write(str(score), font=('Arcade Interlaced', 12))
	pen.penup()
	
	pen.goto(-40, 150)
	pen.color("black")
	pen.write("HIGHSCORE: ", font=('Arcade Interlaced', 12))
	pen.goto(120, 150)
	pen.write(str(high_score), font=('Arcade Interlaced', 12))
	pen.penup()
	


	
## 
#  @brief this function draws the graphics on the window 
#  
#  @return nothing
#  
#  @details 
#  
def draw_grid():
	IN_MENU = False	#not in menu anymore
	
	tic_tac_toe.new.pen.clear()
	pen.clear()	#clear all the previously drawn stuff
	MOVE = 60	#some distnace btw two blocks
	board_x = 0	#indexes
	board_y = 0	
	
	pen.goto(-90, -150)
	pen.color("white")
	pen.write("'E' for menu", font=('Arcade Interlaced', 12))
	pen.penup()
	
	
	pen.goto(-110, 110)	#statying in middle
	
	for row in gameboard:
		board_y = 0
		for column in gameboard:
			_color = colors[gameboard[board_x][board_y]]	#selecting the color depending on the value of the gameboard[x][y]
			pen.fillcolor(_color)	#start filling color, finish it when there is a complete closed boundary
			pen.begin_fill()
			for _ in range(4):	#forming a square
				pen.forward(50)
				pen.right(90)
			pen.end_fill()	#boundary complete, fill the color
			
			pen.goto(pen.xcor()+25, pen.ycor()-35)	#going inside to enter the value of the gameboard[x][y] in middle of the blocks
			pen.color("black")
			number = gameboard[board_x][board_y]
			if number == 0:	#if 0? leave empty string
				number = ""
			pen.write(str(number), align="center", font=FONT)
			pen.goto(pen.xcor()-25, pen.ycor()+35)
			
			board_y += 1
			pen.setx(pen.xcor()+MOVE)	#increment 1 block of distance to make another one next to it
		
		pen.setx(pen.xcor()-240)	#come to next row
		pen.sety(pen.ycor()-MOVE)	#come down a bit
		board_x +=1
		pen.penup()	#finish writing
		#_x += 60
		

	draw_score()

## 
#  @brief this function checks wheather you click on the right button 
#  
#  @param [in] x mouse click x coordinate
#  @param [in] y mouse click y coordinate
#  @return nothing
#  
#  @details 
#  
def btnclick(x, y):
	global IN_MENU
	global TICTAC
	#2048
	#print(x,y)
	if (x > -93) and (x < 81) and (y > -94) and (y < -64) and IN_MENU:	#clicked at 2048?
		window.bgcolor("black")
		window.setup(width=400, height=400)
		window.title("2048")
		IN_MENU = False	#not in menu anymore
		
		pen.clear()	#just clearing in case
		pick_random_tile()
		pick_random_tile()
		draw_grid()	#lets game!
		
	#tictactoe
	if (x > -139) and (x < 100) and (y > -174) and (y < -140) and IN_MENU:
		window.bgcolor("black")
		window.setup(width=400, height=400)
		window.title("TicTacToe")
		
		IN_MENU = False	#not in menu anymore
		TICTAC = True 	# we are in TicTacToe! 
		
		pen.clear()	#just clearing in case
		
		tic_tac_toe.draw_tictac_grid()
	
	#tictactoe clicks
	#global TIC_MOVE
	if (x > -129) and (x < -60) and (y < 120) and (y > 50) and TICTAC:
		tic_tac_toe.draw_tictac_grid(1)
	elif (x > -44) and (x < 27) and (y < 120) and (y > 50) and TICTAC:
		tic_tac_toe.draw_tictac_grid(2)
	elif (x > 45) and (x < 117) and (y < 120) and (y > 50) and TICTAC:
		tic_tac_toe.draw_tictac_grid(3)
	elif (x > -129) and (x < -60) and (y < 36) and (y > -36) and TICTAC:
		tic_tac_toe.draw_tictac_grid(4)
	elif (x > -45) and (x < 30) and (y < 36) and (y > -36) and TICTAC:
		tic_tac_toe.draw_tictac_grid(5)
	elif (x > 45) and (x < 120) and (y < 36) and (y > -36) and TICTAC:
		tic_tac_toe.draw_tictac_grid(6)
	elif (x > -129) and (x < -60) and (y < -54) and (y > -129) and TICTAC:
		tic_tac_toe.draw_tictac_grid(7)
	elif (x > -45) and (x < 27) and (y < -54) and (y > -129) and TICTAC:
		tic_tac_toe.draw_tictac_grid(8)
	elif (x > 45) and (x < 117) and (y < -54) and (y > -129) and TICTAC:
		tic_tac_toe.draw_tictac_grid(9)
	
		
	
	if (x > -139) and (x < 100) and (y > -129) and (y < -100) and IN_MENU:
		
		
		IN_MENU = False	#not in menu anymore
	
		
	
#
#  @brief Transpose of grid
#  
#  @param [in] board grid 2d array
#  @return nothing 
#  
#  @details 
#  
def transpose(board):
    interim_board = [[board[j][i] for j in range(4)] for i in range(4)]
    return interim_board
## 
#  @brief missor image the grid
#  
#  @param [in] board grid 2d array
#  @return nothing
#  
#  @details 
#  
def reverse(board):
    interim_board = [row[::-1] for row in board]
    return interim_board
## 
#  @brief slam left, no combining of the blocks
#  
#  @return nothing
#  
#  @details 
#  
def slam_left():
    for j in range(4):
        for _ in range(3):
            for i in range(3):
                if gameboard[j][i] == 0:
                    gameboard[j][i] = gameboard[j][i + 1]
                    gameboard[j][i + 1] = 0
## 
#  @brief merges the blocks if similar
#  
#  @return nothing
#  
#  @details 
#  
def compress_left(TESTING = False):

    for j in range(4):
        for i in range(3):
            if gameboard[j][i] != 0 and gameboard[j][i] == gameboard[j][i + 1]:
                gameboard[j][i] = gameboard[j][i] * 2
                if not TESTING:
                    global score
                    global high_score
                    score = score + gameboard[j][i]
                    if score > high_score:
                        high_score = score
                        h = {}
                        h['score'] = high_score
                        high_score_pickle = open('highscorepickle.pkl', 'wb')
                        pickle.dump(h , high_score_pickle)
                        #print(high_score)
                        high_score_pickle.close()

                gameboard[j][i + 1] = 0
## 
#  @brief moves left
#  
#  @return nothing
#  
#  @details 
#  
def raw_move_left(TESTING = False):
    slam_left()
    compress_left(TESTING)
    slam_left()



def move_left(TESTING = False):

    raw_move_left(TESTING)
    if not TESTING:
        pick_random_tile()
        draw_grid()
## 
#  @brief moves up
#  
#  @return nothing
#  
#  @details 
#  
def move_up(TESTING = False):

    global gameboard
    gameboard = transpose(gameboard)
    raw_move_left(TESTING)
    gameboard = transpose(gameboard)
    if not TESTING:
        pick_random_tile()
        draw_grid()
## 
#  @brief moves right
#  
#  @return nothing
#  
#  @details 
#  
def move_right(TESTING = False):

    global gameboard
    gameboard = reverse(gameboard)
    raw_move_left(TESTING)
    gameboard = reverse(gameboard)
    if not TESTING:
        pick_random_tile()
        draw_grid()
## 
#  @brief moves down
#  
#  @return nothing
#  
#  @details 
#  
def move_down(TESTING = False):

    global gameboard
    gameboard = transpose(gameboard)
    gameboard = reverse(gameboard)
    raw_move_left(TESTING)
    gameboard = reverse(gameboard)
    gameboard = transpose(gameboard)
    if not TESTING:
        pick_random_tile()
        draw_grid()



## 
#  @brief main
#  
#  @return nothing
#  
#  @details 
#  
def main():
	menu()
	
	window.listen()	#listen to the anykeyboad key pressess
	window.onkeyrelease(menu, "e")	#exit to the menu 
	window.onkeyrelease(move_left, "a")	#move left
	window.onkeyrelease(move_right, "d")	#move right
	window.onkeyrelease(move_up, "w")	#move up
	window.onkeyrelease(move_down, "s")	#move down
	
	turtle.onscreenclick(btnclick, 1)	#if mouse is clicked? check weather its inside the button's boundaries
	window.mainloop()	#run the windown thread parallely

if __name__ == "__main__":	

    global high_score
    global score

    try:
        high_score_pickle = open('highscorepickle.pkl', 'rb')
        h = pickle.load(high_score_pickle)
        high_score = h['score']
        high_score_pickle.close()

    except FileNotFoundError:
        high_score = 0
        h = {}
        h['score'] = high_score
        high_score_pickle = open('highscorepickle.pkl', 'wb')
        pickle.dump(h, high_score_pickle)
        high_score_pickle.close()
    
    print('high score 2048 is: ' + str(high_score))
    score = 0




# Setting up the screen
    

    
    
    
	
    main()
