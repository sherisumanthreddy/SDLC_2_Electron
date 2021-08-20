from copy import deepcopy

class FileIOHandler:
    """ 
    This class handles reading sudoku puzzle from a text file 
    and saving the same to the text file.
    """
    pass

class SudokuGrid:
    """
    This class is representation of a sudoku puzzle as a python object.
    Some features of this class are:
        1. access to FileIOHandler object so it can read and write data to file.
        2. this object handles displaying this object.
        3. this object is required by Sudoku Solver Object.
    """
    pass

class SudokuSolver:
    """
    This takes a SudokuGrid object and provides the solution and other stuff required.
        * Backtracking reccursive algorithm for solving.
    """
    pass