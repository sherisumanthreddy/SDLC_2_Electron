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
        try:
            file = open(pathToPuzzle, 'r')
            data = ""
            for i in file.readlines():
                data += i
            file.close()
            data = FileIOHandler.CleanReadData(data)
            if FileIOHandler.ValidateCleanedData(data):
                return True
            else:
                return False
    
        except Exception as e:
            print(e)
            return False
        
    
    @staticmethod
    def CleanReadData(stringObject):
        """
        This reads the puzzle file and removes unnecessary stuff.
        Input: string
        Returns: string
        """
        retvar = stringObject
        retvar = retvar.replace("\n", ",")
        retvar = retvar.replace(",", "")
        retvar = retvar.replace("#", ".")
        for i in retvar:
            if i not in [".","1","2","3","4","5","6","7","8","9"]:
                retvar = retvar.replace(i,".")
        return retvar

    @staticmethod
    def ValidateCleanedData(stringObj):
        """
        Checks if read data(sudokuTxt) is valid.
        Input: string
        Returns: True or False
        """
        if len(stringObj) != 81:
            return False
        
        for i in stringObj:
            if i.isdigit():
                if int(i) < 1 and int(i) > 9:
                    return False
            else:
                if i != ".":
                    return False

        return True

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
        self.count = 0
    
    def IsValidEntry(self, row, col, val):
        """
        This checks if the value entered is right or wrong
        Input: row number,column number, value
        Returns: True or False
        """
        for i in range(9):
            if self.Puzz.grid[row][i] == val:
                return False
        for i in range(9):
            if self.Puzz.grid[i][col] == val:
                return False
        for i in range(3):
            for j in range(3):
                if self.Puzz.grid[(row//3)*3 + i][(col//3)*3 + j] == val:
                    return False
        return True

    def SolverHelper(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.Puzz.grid[i][j] == '#':
                    for val in range(1, 10):
                        if self.IsValidEntry(i, j, val):
                            self.Puzz.grid[i][j] = val
                            self.Solve()
                            self.Puzz.grid[i][j] = '#'
                    return
        if self.count == 0:
            self.Soln = deepcopy(self.Puzz)
            self.count += 1
  

    def Solve(self):
        """
        This function provides the entire solution
        Input: self
        Returns: String
        """
        self.SolverHelper()
        return self.Soln
        

"""
class SudokuSolver:
    def __init__(self, sudoku_grid: SudokuGrid):
        self.sudoku_grid = sudoku_grid
        self.solution_grid = None
        self.count = 0

    def IsValidEntry(self, row, col, val):
        for i in range(9):
            if self.sudoku_grid.grid[row][i] == val:
                return False
        for i in range(9):
            if self.sudoku_grid.grid[i][col] == val:
                return False
        for i in range(3):
            for j in range(3):
                if self.sudoku_grid.grid[(row//3)*3 + i][(col//3)*3 + j] == val:
                    return False
        return True

    def SolverHelper(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudoku_grid.grid[i][j] == '#':
                    for val in range(1, 10):
                        if self.is_valid_entry(i, j, val):
                            self.sudoku_grid.grid[i][j] = val
                            self.solve()
                            self.sudoku_grid.grid[i][j] = '#'
                    return
        if self.count == 0:
            self.solution_grid = deepcopy(self.sudoku_grid)
            self.count += 1

    def Solve(self):
        self.SolverHelper()
        return self.solution_grid
"""
