from SudokuCompanion import SudokuGrid, SudokuSolver, FileIOHandler

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
        choice = input("Following Options are available:\n 1. Check if puzzle has a soln?\n 2. Provide Hint\n 3. Solve Puzzle\nEnter Option [1,2,3]: ")

        if choice in ["1", "2", "3"]:
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
        print(f"The given sudoku puzzle is can {value}be solved!")
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    else:
        print("MAJOR ERROR!!!")

if __name__ == "__main__":
    ConsoleFront()

