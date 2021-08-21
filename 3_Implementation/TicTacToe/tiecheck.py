import printboard

# Lets us know if the game is over yet
# --------- Global Variables -----------
game_status = True

# Check if there is a tie

def tie_check():
  # Set global variables
  
  global game_status
  # If board is full
  
  if "-" not in printboard.play_board:
    
    game_status = False
    return True
  # Else there is no tie
  else:
    return False