from . import printboard

# --------- Global Variables -----------
# Tells us who the current player is (X goes first)
first_player = "X"
# Handle a turn for an arbitrary player
def manage_turn(player):
  # Get position from player
  print(player + " has next move.")
  place = input("Choose a place from 1-9: ")
  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  validity = False
  while not validity:
    # Make sure the input is valid    
    while place not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      place = input("Choose a place from 1-9: ") 
    # Get correct index in our board list  
    place = int(place) - 1
    # Then also make sure the spot is available on the board
    if printboard.play_board[place] == "-":
      validity = True
    else:
      print("wrong input please try again")
  # Put the game piece on the board
  printboard.play_board[place] = player
  # Show the game board
  printboard.print_board()