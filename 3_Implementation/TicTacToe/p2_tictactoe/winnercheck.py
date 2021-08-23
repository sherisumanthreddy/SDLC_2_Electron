from . import printboard
from . import tiecheck

# Tells us who the winner is
# --------- Global Variables -----------
winner = None

# Check to see if somebody has won 
def who_is_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  
  winner_row = check_rows()
  
  winner_column = check_columns()
  
  winner_digonal = check_diagonals()
  # Get the winner
  
  if winner_row:
    winner = winner_row
  
  elif winner_column:
    winner = winner_column
  
  elif winner_digonal:
    winner = winner_digonal
  else:
    winner = None
    
# Check the rows for a win

def check_rows():
  # Set global variables
  
  global game_status
  # Check if any of the rows have all the same value (and is not empty)
  
  row_1 = printboard.play_board[0] == printboard.play_board[1] == printboard.play_board[2] != "-"
  row_2 = printboard.play_board[3] == printboard.play_board[4] == printboard.play_board[5] != "-"
  row_3 = printboard.play_board[6] == printboard.play_board[7] == printboard.play_board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    
    tiecheck.game_status = False
  # Return the winner
  if row_1:
    
    return printboard.play_board[0] 
  elif row_2:
    
    return printboard.play_board[3] 
  elif row_3:
    
    return printboard.play_board[6] 
  # Or return None if there was no winner
  else:
    return None

# Check the columns for a win
def check_columns():
  # Set global variables
  
  global game_status
  # Check if any of the columns have all the same value (and is not empty)
  
  column_1 = printboard.play_board[0] == printboard.play_board[3] == printboard.play_board[6] != "-"
  column_2 = printboard.play_board[1] == printboard.play_board[4] == printboard.play_board[7] != "-"
  column_3 = printboard.play_board[2] == printboard.play_board[5] == printboard.play_board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    
    tiecheck.game_status = False
  # Return the winner
  if column_1:
    
    return printboard.play_board[0] 
  elif column_2:
    
    return printboard.play_board[1] 
  elif column_3:
    
    return printboard.play_board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  
  global game_status
  # Check if any of the columns have all the same value (and is not empty)
  
  diagonal_1 = printboard.play_board[0] == printboard.play_board[4] == printboard.play_board[8] != "-"
  diagonal_2 = printboard.play_board[2] == printboard.play_board[4] == printboard.play_board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    
    tiecheck.game_status = False
  # Return the winner
  if diagonal_1:
    
    return printboard.play_board[0] 
  elif diagonal_2:
    
    return printboard.play_board[2]

  # Or return None if there was no winner
  else:
    return None