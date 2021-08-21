

import turtle
import random





gameboard = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

grid_merged = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]

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
		
		
def menu():
	#turtle.Screen().clear()
	pen.clear()
	#pen.goto(100, 100)
	window.bgcolor("white")
	window.setup(width = 300, height=450)
	window.title("Mini Arcade Games")
	
	pen.color("black")
	pen.forward(90)
	pen.left(90)	#now torn 90dergrees clock wise 
	pen.forward(30)
	pen.left(90)
	pen.penup()
	pen.goto(7, 6)	#with reference to the drawn canvas
	pen.write("2048 game", font=FONT)
	pen.penup()
	
	

	
	
def draw_grid():
	#turtle.Screen().clear()
	pen.clear()
	MOVE = 60
	board_x = 0
	board_y = 0
	#pen.setx(pen.xcor()-60)
	#pen.sety(pen.ycor()+60)
	pen.goto(-50, 80)
	
	for row in gameboard:
		board_y = 0
		for column in gameboard:
			_color = colors[gameboard[board_x][board_y]]
			pen.fillcolor(_color)
			pen.begin_fill()
			for _ in range(4):
				pen.forward(50)
				pen.right(90)
			pen.end_fill()
			
			pen.goto(pen.xcor()-27, pen.ycor()+10)
			pen.color("blue")
			number = gameboard[board_x][board_y]
			if number == 0:
				number = ""
			pen.write(str(number), align="center", font=FONT)
			pen.goto(pen.xcor()+27, pen.ycor()-10)
			
			board_y += 1
			pen.setx(pen.xcor()+MOVE)
		
		pen.setx(pen.xcor()-240)
		pen.sety(pen.ycor()-MOVE)
		board_x +=1
		pen.penup()
		#_x += 60

	
def btnclick_2048(x, y):
	if x > 0 and x < 81 and y > 0 and y<30:
		#pen.clear()	#clearing the buttons from menu
		window.bgcolor("black")
		window.setup(width = 400, height=400)
		window.title("2048")
		
		
		pen.clear()
		draw_grid()
	
	
def transpose(board):
    interim_board = [[board[j][i] for j in range(4)] for i in range(4)]
    return interim_board


def reverse(board):
    interim_board = [row[::-1] for row in board]
    return interim_board


def slam_left():
    for j in range(4):
        for _ in range(3):
            for i in range(3):
                if gameboard[j][i] == 0:
                    gameboard[j][i] = gameboard[j][i + 1]
                    gameboard[j][i + 1] = 0


def compress_left():
    for j in range(4):
        for i in range(3):
            if gameboard[j][i] != 0 and gameboard[j][i] == gameboard[j][i + 1]:
                gameboard[j][i] = gameboard[j][i] * 2
                gameboard[j][i + 1] = 0

def raw_move_left():
    slam_left()
    compress_left()
    slam_left()


def move_left():
    
    raw_move_left()
    pick_random_tile()
    draw_grid()


def move_up():
    
    global gameboard
    gameboard = transpose(gameboard)
    raw_move_left()
    gameboard = transpose(gameboard)
    pick_random_tile()
    draw_grid()


def move_right():
    
    global gameboard
    gameboard = reverse(gameboard)
    raw_move_left()
    gameboard = reverse(gameboard)
    pick_random_tile()
    draw_grid()


def move_down():
    
    global gameboard
    gameboard = transpose(gameboard)
    gameboard = reverse(gameboard)
    raw_move_left()
    gameboard = reverse(gameboard)
    gameboard = transpose(gameboard)
    pick_random_tile()
    draw_grid()


def main():
	menu()


	window.listen()
	window.onkeyrelease(menu, "e")
	window.onkeyrelease(move_left, "a")
	window.onkeyrelease(move_right, "d")
	window.onkeyrelease(move_up, "w")
	window.onkeyrelease(move_down, "s")
	
	turtle.onscreenclick(btnclick_2048, 1)
	window.mainloop()



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


