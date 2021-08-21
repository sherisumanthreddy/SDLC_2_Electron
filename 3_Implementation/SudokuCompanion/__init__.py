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
