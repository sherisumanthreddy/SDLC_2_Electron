import playttt
import takeinput
import printboard
import tiecheck
import winnercheck
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
