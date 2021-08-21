from SudokuCompanion import FileIOHandler, SudokuGrid, SudokuSolver

def test_FileIOHandler_ReadSudokuFromTxt():
    path_ = "puzzle.txt"

    IO_Obj = FileIOHandler()
    assert IO_Obj.ReadSudokuFromTxt(path_)


def test_CleanReadData():
    var = "123\n4343,444###,##331231\n"
    var2 = "qwertyuiop"
    assert FileIOHandler.CleanReadData(var) == "1234343444.....331231"
    assert FileIOHandler.CleanReadData(var2) == ".........."

def test_ValidateCleanedData():
    var = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.....1"
    var2 = "9..21.4...32.4..A..4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.....1"
    var3 = "9..21.4...32.4.....4.8....7..7.5...9..17.23..3...8.17.5....9.8.....2854...8.."
    assert FileIOHandler.ValidateCleanedData(var)
    assert not FileIOHandler.ValidateCleanedData(var2)
    assert not FileIOHandler.ValidateCleanedData(var3)
