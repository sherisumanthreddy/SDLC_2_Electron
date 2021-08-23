from copy import deepcopy
import random


class FileIOHandler:
    """
    This class handles reading sudoku puzzle from a text file
    and saving the same to the text file.
    """
    def __init__(self):
        self.sudokuTxt = ""  # the data read from file is stored as string

    def ReadSudokuFromTxt(self, pathToPuzzle):
        """
        Reads the formatted puzzle txt file and stores it as text.
        (sudokuTxt<-Puzzle.txt)
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
                self.sudokuTxt = data
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
            if i not in [".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                retvar = retvar.replace(i, ".")
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

    @staticmethod
    def SaveSudokuToTxt(sudokuGridObjectStr, pathToSolTxt):
        """
        Takes SudokuGrid object and saves it to a file
        Input: SudokuGrid object, path to txt
        Returns: True or False
        """
        if not FileIOHandler.ValidateCleanedData(sudokuGridObjectStr):
            return False

        file = open(pathToSolTxt, "x")

        savestring = ""
        for i in range(0, 81):
            savestring += sudokuGridObjectStr[i]
            if (i + 1) % 9 == 0:
                savestring += "\n"
            else:
                savestring += ","

        file.write(savestring)
        file.close()

        return True


class SudokuGrid:
    """
    This class is representation of a sudoku puzzle as a python object.
    Some features of this class are:
        1. access to FileIOHandler object so it can read/write data to file.
        2. this object handles displaying this object.
        3. this object is required by Sudoku Solver Object.
    """
    def __init__(self, IOHandlerObj, puzz_source, sol_destination=None):
        self.Grid = [['.' for _ in range(9)] for _ in range(9)]  # 9 x 9 List
        self.IOHandler = IOHandlerObj()
        self.IOSource = puzz_source
        self.IODestination = sol_destination

    def setIODestination(self, path_):
        self.IODestination = path_

    def Read(self):
        if not self.IOHandler.ReadSudokuFromTxt(self.IOSource):
            return False
        try:
            for i in range(9):
                for j in range(9):
                    if self.IOHandler.sudokuTxt[j+9*i] == ".":
                        self.Grid[i][j] = self.IOHandler.sudokuTxt[j+9*i]
                    else:
                        self.Grid[i][j] = int(self.IOHandler.sudokuTxt[j+9*i])
        except Exception as e:
            print(e)
            return False
        return True

    def Save(self):
        if not self.IOHandler.SaveSudokuToTxt(str(self), self.IODestination):
            return False
        else:
            return True

    def __str__(self):
        """
        This converts grid to compatible string or can be called GridToString
        Input: self
        Returns: string
        """
        retvar = ""
        for i in self.Grid:
            for j in i:
                retvar += str(j)
        return retvar

    def PrintSudoku(self):
        stringObj = str(self)
        if not FileIOHandler.ValidateCleanedData(stringObj):
            print("MegaError!!!!!!!!")

        print("-"*25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(stringObj[j+i*9], end=" ")
                if (j+1) % 3 == 0:
                    print("|", end=" ")
            print("\n", end="")
            if (i+1) % 3 == 0:
                print("-"*25)

        return


class SudokuSolver:
    """
    This takes a SudokuGrid object and provides the solution
    and other stuff required.
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
            if self.Puzz.Grid[row][i] == val:
                return False
        for i in range(9):
            if self.Puzz.Grid[i][col] == val:
                return False
        for i in range(3):
            for j in range(3):
                if self.Puzz.Grid[(row//3)*3 + i][(col//3)*3 + j] == val:
                    return False
        return True

    def SolverHelper(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.Puzz.Grid[i][j] == '.':
                    for val in range(1, 10):
                        if self.IsValidEntry(i, j, val):
                            self.Puzz.Grid[i][j] = val
                            self.Solve()
                            self.Puzz.Grid[i][j] = '.'
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

    def IsSolvable(self):
        soln = self.Solve()
        if self.count >= 1 and (str(soln) != str(self.Puzz)):
            return True
        else:
            return False

    def GetHintString(self):
        if not self.IsSolvable():
            return str(self.Puzz)
        else:
            soln = list(str(self.Solve()))
            puzz = list(str(self.Puzz))
            for i in range(81):
                if random.random() >= 0.8 and puzz[i] == ".":
                    puzz[i] = soln[i]
            return "".join(puzz)
