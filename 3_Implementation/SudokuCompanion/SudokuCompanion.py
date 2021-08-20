from copy import deepcopy

class FileIOHandler:
    """ 
    This class handles reading sudoku puzzle from a text file 
    and saving the same to the text file.
    """
    def __init__(self):
        self.sudokuTxt = "" # the data read from file is stored as string with no space or any delimiters

    def ReadSudokuFromTxt(self, pathToPuzzle):
        """
        Reads the formatted puzzle txt file and stores it as text (sudokuTxt<-Puzzle.txt).
        Input: Path to puzzle file
        Returns: True or False
        """
        return 
    
    @staticmethod
    def CleanReadData(stringObject):
        """
        This reads the puzzle file and removes unnecessary stuff.
        Input: string
        Returns: string
        """
        return
    
    @staticmethod
    def validateCleanedData(string):
        """
        Checks if read data(sudokuTxt) is valid.
        Input: string
        Returns: True or False
        """
        return

    def SaveSudokuToTxt(self, sudokuGridObject):
        """
        Takes SudokuGrid object and saves it to a file
        Input: SudokuGrid object
        Returns: True or False
        """
        return

    @staticmethod
    def FormatGridToTxt(sudokuGridObject):
        """ 
        This is complementary to cleanData function this converts grid to compatible string
        Input: sudokuGrid Object
        Returns: string
        """
        return


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