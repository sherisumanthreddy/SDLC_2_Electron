#libraries imports
import turtle
import random


<<<<<<< HEAD
# Seting up the screen
window = turtle.Screen()
window.title("Mini arcade games")
window.bgcolor("black")
window.setup(width=450, height=600)
window.tracer(0)

#general purpose pen turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()	#an invisible turtle for drawing buttons

#some constants 
CURSOR_SIZE = 20
FONT_SIZE = 15
FONT = ('Arial', FONT_SIZE, 'bold')
ARCADE_FONT = ('Arcade Interlaced', FONT_SIZE, 'bold')
=======

>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f


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
	#turtle.Screen().clear()
	pen.penup()
	pen.clear()
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
	pen.forward(110)
	pen.left(90)	#now torn 90dergrees clock wise 
	pen.forward(30)
	pen.left(90)
	pen.penup()
	pen.goto(7, 6)	#with reference to the drawn canvas
	pen.setx(pen.xcor()-100)
	pen.sety(pen.ycor()-100)
	pen.write("2048 game", font=ARCADE_FONT)
	pen.setx(pen.xcor()+100)
	pen.sety(pen.ycor()+100)
	pen.penup()
	
	

	
## 
#  @brief this function draws the graphics on the window 
#  
#  @return nothing
#  
#  @details 
#  
def draw_grid():
	#turtle.Screen().clear()
	pen.clear()	#clear all the previously drawn stuff
	MOVE = 60	#some distnace btw two blocks
	board_x = 0	#indexes
	board_y = 0	
	#pen.setx(pen.xcor()-60)
	#pen.sety(pen.ycor()+60)
	pen.goto(-50, 80)	#statying in middle
	
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
			
			pen.goto(pen.xcor()-27, pen.ycor()+10)	#going inside to enter the value of the gameboard[x][y] in middle of the blocks
			pen.color("black")
			number = gameboard[board_x][board_y]
			if number == 0:	#if 0? leave empty string
				number = ""
			pen.write(str(number), align="center", font=FONT)
			pen.goto(pen.xcor()+27, pen.ycor()-10)
			
			board_y += 1
			pen.setx(pen.xcor()+MOVE)	#increment 1 block of distance to make another one next to it
		
		pen.setx(pen.xcor()-240)	#come to next row
		pen.sety(pen.ycor()-MOVE)	#come down a bit
		board_x +=1
		pen.penup()	#finish writing
		#_x += 60


## 
#  @brief this function checks wheather you click on the right button 
#  
#  @param [in] x mouse click x coordinate
#  @param [in] y mouse click y coordinate
#  @return nothing
#  
#  @details 
#  
def btnclick_2048(x, y):
	if x > -93 and x < 81 and y > -94 and y < -64:	#clicked properly?
		#pen.clear()	#clearing the buttons from menu
		window.bgcolor("black")
		window.setup(width = 400, height=400)
		window.title("2048")
		
		
		pen.clear()	#just clearing in case
		draw_grid()	#lets game!
	
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
<<<<<<< HEAD
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
=======


def reverse(board):
    interim_board = [row[::-1] for row in board]
    return interim_board


>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f
def slam_left():
    for j in range(4):
        for _ in range(3):
            for i in range(3):
                if gameboard[j][i] == 0:
                    gameboard[j][i] = gameboard[j][i + 1]
                    gameboard[j][i + 1] = 0
<<<<<<< HEAD
## 
#  @brief merges the blocks if similar
#  
#  @return nothing
#  
#  @details 
#  
=======


>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f
def compress_left():
    for j in range(4):
        for i in range(3):
            if gameboard[j][i] != 0 and gameboard[j][i] == gameboard[j][i + 1]:
                gameboard[j][i] = gameboard[j][i] * 2
                gameboard[j][i + 1] = 0
<<<<<<< HEAD
## 
#  @brief moves left
#  
#  @return nothing
#  
#  @details 
#  
def move_left():
    pick_random_tile()
=======

def raw_move_left():
>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f
    slam_left()
    compress_left()
    slam_left()


def move_left():
    
    raw_move_left()
    pick_random_tile()
    draw_grid()
<<<<<<< HEAD
## 
#  @brief moves up
#  
#  @return nothing
#  
#  @details 
#  
=======


>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f
def move_up():
    
    global gameboard
    gameboard = transpose(gameboard)
    raw_move_left()
    gameboard = transpose(gameboard)
    pick_random_tile()
    draw_grid()
<<<<<<< HEAD
## 
#  @brief moves right
#  
#  @return nothing
#  
#  @details 
#  
=======


>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f
def move_right():
    
    global gameboard
    gameboard = reverse(gameboard)
    raw_move_left()
    gameboard = reverse(gameboard)
    pick_random_tile()
    draw_grid()
<<<<<<< HEAD
## 
#  @brief moves down
#  
#  @return nothing
#  
#  @details 
#  
=======


>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f
def move_down():
    
    global gameboard
    gameboard = transpose(gameboard)
    gameboard = reverse(gameboard)
    raw_move_left()
    gameboard = reverse(gameboard)
    gameboard = transpose(gameboard)
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
<<<<<<< HEAD
	
	window.listen()	#listen to the anykeyboad key pressess
	window.onkeyrelease(menu, "e")	#exit to the menu 
	window.onkeyrelease(move_left, "a")	#move left
	window.onkeyrelease(move_right, "d")	#move right
	window.onkeyrelease(move_up, "w")	#move up
	window.onkeyrelease(move_down, "s")	#move down
=======


	window.listen()
	window.onkeyrelease(menu, "e")
	window.onkeyrelease(move_left, "a")
	window.onkeyrelease(move_right, "d")
	window.onkeyrelease(move_up, "w")
	window.onkeyrelease(move_down, "s")
>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f
	
	turtle.onscreenclick(btnclick_2048, 1)	#if mouse is clicked? check weather its inside the button's boundaries
	window.mainloop()	#run the windown thread parallely



<<<<<<< HEAD
if __name__ == "__main__":	
	main()
=======
if __name__ == "__main__":

    # Set up the screen
    window = turtle.Screen()
    window.title("Mini arcade games")
    window.bgcolor("black")
    window.setup(width=450, height=600)
    window.tracer(0)
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()  # an invisible turtle for drawing buttons
    
    CURSOR_SIZE = 20
    FONT_SIZE = 12
    FONT = ('Arial', FONT_SIZE, 'bold')
    
    x_2048 = 0
    y_2048 = 0
    pick_random_tile()
    pick_random_tile()
    main()
>>>>>>> eaa9309d8d54080e75f0664e9d021191be6aeb7f


