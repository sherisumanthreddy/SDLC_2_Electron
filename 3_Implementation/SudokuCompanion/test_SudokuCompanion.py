from SudokuCompanion import FileIOHandler, SudokuGrid, SudokuSolver
import os

def test_FileIOHandler_ReadSudokuFromTxt():
    path_ = "puzzle.txt"

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
    myGridSudoku = SudokuGrid(FileIOHandler, "puzzle.txt")
    assert str(myGridSudoku) == "." * 81

    var = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.....1"
    assert myGridSudoku.Read()
    assert str(myGridSudoku) == var
    
def test_Sudoku_Save():
    myGridSudoku = SudokuGrid(FileIOHandler, "puzzle.txt")
    myGridSudoku.Read()

    path_ = "save.txt"
    myGridSudoku.setIODestination(path_)

    assert myGridSudoku.Save()
    os.remove(path_)

    print("\n")
    myGridSudoku.PrintSudoku()
    print("\n")

    
