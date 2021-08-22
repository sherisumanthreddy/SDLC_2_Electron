import printboard
import check
import takeinput
import reverseplayer
import tiecheck
import winnercheck
import gameover

# ------------- Functions ---------------

# Play a game of tic tac toe
def play_ttt():

  # Show the initial game board
  printboard.print_board()
  
  # Loop until the game stops (winner or tie)
  
  while tiecheck.game_status:

    # Handle a turn
    check.manage_turn(check.first_player)
    
    # Check if the game is over
    gameover.game_over()
    
    # Flip to the other player
    reverseplayer.reverse_player()
      
  # Since the game is over, print the winner or tie
  if winnercheck.winner == "X" or winnercheck.winner == "O":
    print(winnercheck.winner + " have won.")
  elif winnercheck.winner == None:
    print(" tie between X and O.")

# ------------ Start Execution -------------
# Play a game of tic tac toe
while True:
    X = takeinput.take_input()
    if X.lower() == 'y':
      
      printboard.play_board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
      tiecheck.game_status = True
      #check.first_player = "x"
      winnercheck.winner = None
      play_ttt()
    else:
      break
