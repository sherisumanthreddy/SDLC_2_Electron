class SudokuSolver:
    def __init__(self, sudoku_grid: SudokuGrid):
        self.sudoku_grid = sudoku_grid
        self.solution_grid = None
        self.count = 0

    def is_valid_entry(self, row, col, entry):
        for i in range(9):
            if self.sudoku_grid.grid[row][i] == entry:
                return False
        for i in range(9):
            if self.sudoku_grid.grid[i][col] == entry:
                return False
        for i in range(3):
            for j in range(3):
                if self.sudoku_grid.grid[(row//3)*3 + i][(col//3)*3 + j] == entry:
                    return False
        return True
