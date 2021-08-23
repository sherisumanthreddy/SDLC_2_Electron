from .SudokuCompanion import SudokuGrid, SudokuSolver, FileIOHandler

def JustPrintSudoku(SudokuStr):
        stringObj = SudokuStr
        if not FileIOHandler.ValidateCleanedData(stringObj):
            print("MegaError!!!!!!!!")

        print("-"*25)
        for i in range(9):
            print("|", end = " ")
            for j in range(9):
                print(stringObj[j+i*9], end=" ")
                if (j+1)%3 == 0:
                    print("|", end=" ")
            print("\n", end="")
            if (i+1)%3 == 0:
                print("-"*25)

        return

def ConsoleFront():
    path_to_puzzle = input("Enter the path to txt file containing the puzzle: ")
    GridObj = SudokuGrid(FileIOHandler, path_to_puzzle)

    try:
        GridObj.Read()
    except ValueError:
        print(f"[ERR]: \"{path_to_puzzle}\" - Input file does not contain sudoku puzzle in the right format!")
        print("Try Again :-( ")
        return
    except IOError as exception_here:
        print(exception_here)
        print("Try Again :-( ")
        return

    print("PUZZLE:")
    GridObj.PrintSudoku()
    print()
    gotNotChoice = True

    while gotNotChoice:
        choice = input("Following Options are available:\n 1. Check if puzzle has a soln?\n 2. Provide Hint\n 3. Solve Puzzle\nEnter Option [1,2,3] or q to quit: ")

        if choice in ["1", "2", "3", "q"]:
            gotNotChoice = False
        else:
            print()
            print("="*80)
            print("Invalid Option...Try Again")
            print("="*80)
            print()

    SolverObj = SudokuSolver(GridObj)

    if choice == "1":
        value = "" if SolverObj.IsSolvable() else "NOT "
        print(f"The given sudoku puzzle can {value}be solved!")

    elif choice == "2":
        hintStr = SolverObj.GetHintString()
        print("HINT:")
        JustPrintSudoku(hintStr)

    elif choice == "3":
        print("SOLUTION:")
        answer = SolverObj.Solve()
        answer.PrintSudoku()

        wanna_save = input("Do you want to save solution to a file? [y/N]")
        if wanna_save == 'y':
            error = True
            while error:
                output_file = input("Enter output filename: ")
                try:
                    answer.setIODestination(output_file)
                    if answer.Save():
                        print("File Saved Succesfully!")
                except FileExistsError:
                    print("File already exists!...Try again")
                else:
                    error = False
        else:
            return
    elif choice == "q":
        return

    else:
        print("MAJOR ERROR!!!")

if __name__ == "__main__":
    ConsoleFront()

