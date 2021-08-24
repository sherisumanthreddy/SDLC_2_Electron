from SudokuCompanion import sudoku_companion_main
from TicTacToe.p1_tictactoe import one_player_ttt
from TicTacToe.p2_tictactoe import two_player_ttt

if __name__ == "__main__":
    print("Welcome To MiniArcade Game!")

    print("Select from the following:")
    print("1. Sudoku Companion (Console)")
    print("2. Tic-Tac-Toe - 1 Player (Console)")
    print("3. Tic-Tac-Toe - 2 player (Console)")

    console_or_gui = input("Enter your selection [1, 2, 3 or q to quit: ")
    if console_or_gui == '1':
        sudoku_companion_main.ConsoleFront()
    elif console_or_gui == '2':
        one_player_ttt.ConsoleFront()
    elif console_or_gui == '3':
        two_player_ttt.ConsoleFront()
    else:
        print("EXITING")
