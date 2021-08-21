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
