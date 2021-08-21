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
    def ValidateCleanedData(string):
        """
        Checks if read data(sudokuTxt) is valid.
        Input: string
        Returns: True or False
        """
        return

    def SaveSudokuToTxt(self, sudokuGridObject, pathToSolTxt):
        """
        Takes SudokuGrid object and saves it to a file
        Input: SudokuGrid object, path to txt
        Returns: True or False
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
    def __init__(self, IOHandlerObj, puzz_source, sol_destination = None):
        self.Grid = [[]] # 9 x 9 List
        self.IOHandler = IOHandlerObj
        self.IOSource = puzz_source
        self.IODestination = sol_destination

    def setIODestination(self, path_):
        self.IODestination = path_

    def Read(self):
        self.IOHandler.ReadSudokuFromTxt(self.IOSource)

    def StringToGrid(self):
        pass
        
    def Save(self):
        self.IOHandler.SaveSudokuToTxt(self, self.IODestination)
        

    def __str__(self):
        """
        This converts grid to compatible string or can be called GridToString
        Input: self
        Returns: string
        """


class SudokuSolver:
    """
    This takes a SudokuGrid object and provides the solution and other stuff required.
        * Backtracking reccursive algorithm for solving.
    """
    def __init__(self, sudokuGridObj):
        self.Puzz = sudokuGridObj
        self.Soln = None
    
    def IsValidEntry(self, row, col, val):
        """
        This checks if the value entered is right or wrong
        Input: row number,column number, value
        Returns: True or False
        """
        pass

    def SolverHelper(self):
        pass

    def Solve(self):
        """
        This function provides the entire solution
        Input: self
        Returns: String
        """
        pass
