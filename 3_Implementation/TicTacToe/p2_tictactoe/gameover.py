from . import winnercheck
from . import tiecheck

# Check if the game is over
def game_over():
  winnercheck.who_is_winner()
  tiecheck.tie_check()