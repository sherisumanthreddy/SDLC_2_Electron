from SudokuCompanion import FileIOHandler, SudokuGrid, SudokuSolver

def test_FileIOHandler_ReadSudokuFromTxt():
    path_ = "puzzle.txt"

    IO_Obj = FileIOHandler()
    assert IO_Obj.ReadSudokuFromTxt(path_)
