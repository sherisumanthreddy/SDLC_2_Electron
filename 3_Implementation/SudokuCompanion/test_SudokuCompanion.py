from SudokuCompanion import FileIOHandler, SudokuGrid, SudokuSolver
import os

puzz_path = "3_Implementation/SudokuCompanion/puzzle.txt"
Unsolve_puzz = "3_Implementation/SudokuCompanion/UnsolvablePuzz.txt"

def test_FileIOHandler_ReadSudokuFromTxt():
    path_ = puzz_path

    IO_Obj = FileIOHandler()
    assert IO_Obj.ReadSudokuFromTxt(path_)


def test_FileIOHandler_CleanReadData():
    var = "123\n4343,444###,##331231\n"
    var2 = "qwertyuiop"
    assert FileIOHandler.CleanReadData(var) == "1234343444.....331231"
    assert FileIOHandler.CleanReadData(var2) == ".........."

def test_FileIOHandler_ValidateCleanedData():
    var = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.....1"
    var2 = "9..21.4...32.4..A..4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.....1"
    var3 = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.."
    assert FileIOHandler.ValidateCleanedData(var)
    assert not FileIOHandler.ValidateCleanedData(var2)
    assert not FileIOHandler.ValidateCleanedData(var3)

def test_FileIOHandler_SaveSudokuToTxt():
    path_ = "save.txt"

    var = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.....1"

    IO_Obj = FileIOHandler()
    assert IO_Obj.SaveSudokuToTxt(var, path_)
    assert IO_Obj.ReadSudokuFromTxt(path_)
    os.remove(path_)

def test_SudokuGrid_StrAndRead():
    myGridSudoku = SudokuGrid(FileIOHandler, puzz_path)
    assert str(myGridSudoku) == "." * 81

    var = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.....1"
    assert myGridSudoku.Read()
    assert str(myGridSudoku) == var

def test_Sudoku_Save():
    myGridSudoku = SudokuGrid(FileIOHandler, puzz_path)
    myGridSudoku.Read()

    path_ = "save.txt"
    myGridSudoku.setIODestination(path_)

    assert myGridSudoku.Save()
    os.remove(path_)

    # print("\n")
    # myGridSudoku.PrintSudoku()
    # print("\n")

def test_SudokuSolver_IsValidEntry():
    myGridSudoku = SudokuGrid(FileIOHandler, puzz_path)
    myGridSudoku.Read()

    Solver1 = SudokuSolver(myGridSudoku)

    assert not Solver1.IsValidEntry(0, 1, 3)
    assert Solver1.IsValidEntry(0, 1, 5)

    assert not Solver1.IsValidEntry(2,2,9)
    assert Solver1.IsValidEntry(2, 2, 5)

    assert Solver1.IsValidEntry(4, 4, 9)
    assert not Solver1.IsValidEntry(4, 4, 5)
    assert not Solver1.IsValidEntry(4, 4, 3)
    assert not Solver1.IsValidEntry(4, 4, 1)

def test_SudokuSolver_Solve():
    myGridSudoku = SudokuGrid(FileIOHandler, puzz_path)
    myGridSudoku.Read()

    Solver1 = SudokuSolver(myGridSudoku)

    soln = Solver1.Solve()

    ans = "976215438832947615145863927427351869681792354359486172514679283793128546268534791"
    assert ans == str(soln)

    assert str(soln) != "97621543883333947615145863927427351869681792354359486172514679283793128546268534791"
    assert str(soln) != "986215437832947615145863927427351869681792354359486172514679283793128546268534791"

    print(Solver1.count)

def test_SudokuSolver_IsSolvable():
    myGridSudoku = SudokuGrid(FileIOHandler, puzz_path)
    myGridSudoku.Read()
    Solver1 = SudokuSolver(myGridSudoku)
    assert Solver1.IsSolvable()

    myGridSudoku2 = SudokuGrid(FileIOHandler, Unsolve_puzz)
    myGridSudoku2.Read()
    Solver2 = SudokuSolver(myGridSudoku2)
    assert not Solver2.IsSolvable()

def test_SudokuSolver_GetHintString():
    myGridSudoku = SudokuGrid(FileIOHandler, puzz_path)
    myGridSudoku.Read()
    Solver1 = SudokuSolver(myGridSudoku)

    assert Solver1.GetHintString() != str(myGridSudoku)

    myGridSudoku2 = SudokuGrid(FileIOHandler, Unsolve_puzz)
    myGridSudoku2.Read()
    Solver2 = SudokuSolver(myGridSudoku2)
    assert Solver2.GetHintString() == str(myGridSudoku2)

