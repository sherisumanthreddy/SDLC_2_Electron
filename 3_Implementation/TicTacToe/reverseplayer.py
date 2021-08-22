import check
# Flip the current player from X to O, or O to X

def reverse_player():
  # Global variables we needed
  
  global first_player
  # If the current player was X, make it O
  if check.first_player == "X":
    check.first_player = "O"
  # Or if the current player was O, make it X
  elif check.first_player == "O":
    check.first_player = "X"
