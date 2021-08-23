from . import playttt
from . import takeinput
from . import printboard
from . import tiecheck
from . import winnercheck
# ------------ Start Execution -------------
# Play a game of tic tac toe
def ConsoleFront():
  while True:
      X = takeinput.take_input()
      if X.lower() == 'y':
      
        printboard.play_board = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
        tiecheck.game_status = True
      #check.first_player = "x"
        winnercheck.winner = None
        playttt.play_ttt()
      else:
        break
if __name__ == "__main__":
    ConsoleFront()