from SudokuCompanion import sudoku_companion_main
from TicTacToe.p1_tictactoe import one_player_ttt

if __name__ == "__main__":
    print("Welcome To MiniArcade Game!")

    print("Select from the following:")
    print("1. 2048 (Gui)")
    print("2. Sudoku Companion (Console)")
    print("3. Tic-Tac-Toe - 1 Player (Console)")
    print("4. Tic-Tac-Toe - 2 player (Console)")

    console_or_gui = input("Enter your selection [1, 2, 3, 4] or q to quit: ")
    if console_or_gui == '1':
        print("This should launch gui")
    elif console_or_gui == '2':
        sudoku_companion_main.ConsoleFront()
    elif console_or_gui == '3':
        one_player_ttt.ConsoleFront()
    else:
        print("EXITING")
