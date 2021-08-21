class SudokuSolver:
    def __init__(self, sudoku_grid: SudokuGrid):
        self.sudoku_grid = sudoku_grid
        self.solution_grid = None
        self.count = 0
