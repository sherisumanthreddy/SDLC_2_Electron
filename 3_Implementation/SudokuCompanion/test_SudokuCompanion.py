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
    var3 = "123232\n43###43331231\n"
    var4 = "ahs6384d.fgjh"
    var5 = "1234,.hg67*53"
    var6 = "12aeq[hw7"
    var7 = "asedsf3455.,'..#"
    assert FileIOHandler.CleanReadData(var) == "1234343444.....331231"
    assert FileIOHandler.CleanReadData(var2) == ".........."
    assert FileIOHandler.CleanReadData(var3) == "12323243...43331231"
    assert FileIOHandler.CleanReadData(var4) == "...6384......"
    assert FileIOHandler.CleanReadData(var5) == "1234...67.53"
    assert FileIOHandler.CleanReadData(var6) == "12......7"
    assert FileIOHandler.CleanReadData(var7) == "......3455....."


def test_FileIOHandler_ValidateCleanedData():
    var = "9..21.4...32.4.....4.8....7..7.5...9..17"\
          ".23..3...8.17.5....9.8.....2854...8.....1"
    var2 = "9..21.4...32.4..A..4.8....7..7.5...9..17.23."\
           ".3...8.17.5....9.8.....2854...8.....1"
    var3 = "9..21.4...32.4.....4.8....7..7.5...9..17.42..3.."\
           ".8.17.5....9.8.....2854...8.."
    var4 = "8..34.4...32.4.....4.8....7..7.5...9..19.67..3.."\
           ".8.17.5....9.8.....2854...8.."
    var5 = "9..56.4...32.4.....4.9....7..7.5...9..45.28..3.."\
           ".8.17.5....9.8.....2854...8.."
    var6 = "34..21.4...32.4.....5.8....7..7.5...9..54.56..3.."\
           ".8.17.5....9.8.....2854...8.."
    var7 = "9..61.4...32.4.....4.8....7..7.5...9..17.83..3.."\
           ".8.17.5....9.8.....2854...8.."
    var8 = "34..21.4...32.4.....4.8....7..7.5...9..17.643..3.."\
           ".8.17.5....9.8.....2854...8.."
    var9 = "32..21.4...32.4.....4.8....7..7.5...9..17.23..3.."\
           ".8.17.5....9.8.....2854...8.."
    var10 = "454..21.4...32.4..A...9..17.23."\
           ".34...8.17.5....9.8.....2..8.....1"
    var11 = "2324...5.35.4.3.4344..17.23."\
           ".3...8.17.5....9.8.....2854...8.....1"
    var12 = "4..34...75...23...8..2.5..17.23."\
           ".34...8.17.5....9.8.....2..8.....1"
    var13 = "23...86....45...23..17.23."\
           ".343...8.17.5....549.8.....2854...8.....1"
    var14 = "9..21.4...32.4..A..4.8....7..7.5...9..17.23."\
           ".753...8.17.5....9.468.....2854..46.8.....1"
    var15 = "9..21.4...32.4..A..4.8....7..7.5...9..17.23."\
           ".463...8.1657.5....9.8..46...243854...8.....1"
    var16 = "9.34.21.4...32.4..64A..4.8....7..7.5...9..17.23."\
           ".3...8.17.5....9.8.....2854...8.....1"
    var17 = "93..21.4...32.4..BC..4.8....7..7.5...9..17.23."\
           ".3t5...8.17.5....9.8y.....2854.e5..8.....1"
    assert FileIOHandler.ValidateCleanedData(var)
    assert not FileIOHandler.ValidateCleanedData(var2)
    assert not FileIOHandler.ValidateCleanedData(var3)
    assert not FileIOHandler.ValidateCleanedData(var4)
    assert not FileIOHandler.ValidateCleanedData(var5)
    assert not FileIOHandler.ValidateCleanedData(var6)
    assert not FileIOHandler.ValidateCleanedData(var7)
    assert not FileIOHandler.ValidateCleanedData(var8)
    assert not FileIOHandler.ValidateCleanedData(var9)
    assert not FileIOHandler.ValidateCleanedData(var10)
    assert not FileIOHandler.ValidateCleanedData(var11)
    assert not FileIOHandler.ValidateCleanedData(var12)
    assert not FileIOHandler.ValidateCleanedData(var13)
    assert not FileIOHandler.ValidateCleanedData(var14)
    assert not FileIOHandler.ValidateCleanedData(var15)
    assert not FileIOHandler.ValidateCleanedData(var16)
    assert not FileIOHandler.ValidateCleanedData(var17)


def test_FileIOHandler_SaveSudokuToTxt():
    path_ = "save.txt"

    var = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3."\
          "..8.17.5....9.8.....2854...8.....1"

    IO_Obj = FileIOHandler()
    assert IO_Obj.SaveSudokuToTxt(var, path_)
    assert IO_Obj.ReadSudokuFromTxt(path_)
    os.remove(path_)


def test_SudokuGrid_StrAndRead():
    myGridSudoku = SudokuGrid(FileIOHandler, puzz_path)
    assert str(myGridSudoku) == "." * 81

    var = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5..."\
          ".9.8.....2854...8.....1"
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

    assert not Solver1.IsValidEntry(2, 2, 9)
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

    ans = "97621543883294761514586392742735186968179235"\
          "4359486172514679283793128546268534791"
    assert ans == str(soln)

    assert str(soln) != "9762154388333394761514586392742735186968"\
                        "1792354359486172514679283793128546268534791"
    assert str(soln) != "98621543783294761514586392742735186968179235"\
                        "4359486172514679283793128546268534791"

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
