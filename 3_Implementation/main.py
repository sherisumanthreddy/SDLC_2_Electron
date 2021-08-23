from SudokuCompanion import sudoku_companion_main

if __name__ == "__main__":
    print("Welcome To MiniArcade Game!")

    print("Select from the following:")
    print("1. 2048 (Gui)")
    print("2. Sudoku Companion (Console)")
    print("3. Tic-Tac-Toe")

    console_or_gui = input("Enter your selection [1, 2, 3] or q to quit: ")
    if console_or_gui == '1':
        print("This should launch gui")
    elif console_or_gui == '2':
        sudoku_companion_main.ConsoleFront()
    else:
        print("EXITING")
