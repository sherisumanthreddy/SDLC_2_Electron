# Will hold our game board data

play_board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Display the game board to the screen

def print_board():
  global print_board
  print("\n")
  print(play_board[0] + " | " + play_board[1] + " | " + play_board[2] + "     1 | 2 | 3")
  print(play_board[3] + " | " + play_board[4] + " | " + play_board[5] + "     4 | 5 | 6")
  print(play_board[6] + " | " + play_board[7] + " | " + play_board[8] + "     7 | 8 | 9")
  print("\n")