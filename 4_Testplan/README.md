# TESTPLAN MD FILE HERE

## Tic-Tac-Toe

###  High level test plan

|Test ID | Description | Exp I/P | Exp O/P |
|--------|-------------|---------|---------|
|H_01    |  Check if the 3X3 playing field is created or not           |    NA     |      3X3 playing field   |
|H_02    |Check if any player get 3 of his marks.             |   'X' or 'o' i/p from the user      |The player 1/2 won the game.|
|H_03    | Check if all the 9 squares are full.            |   9 inputs from the users      |     The game is over    |



###  Low level test plan

|Test ID | Description | Exp I/P | Exp O/P |
|--------|-------------|---------|---------|
|L_01    | Check if the basic requirement to the game  (3x3 playing field) is created or not.This 3X3 squares is the first step in the program to play the game |    Not expected                   any input from the user |  3X3 playing field  |
|L_02    |  Play proceeds with the opponents alternately placing their marks in any unoccupied cell. check if any player finishes  with 3 marks in a row, where a row can be either                  vertical, horizontal, or diagonal. |   'X' or 'o' i/p from the two players alternatively      |   The player 1/2 won the game.      |
|L_03    |   Check if all the 9 squares are full,the game is over and no player can get the 3 marks in a row the game is draw , if any one of the player get the 3 marks in a row                     that player will win the game           |  9 inputs from the users.       |                The game is over/Ended.       The player 1/2 won the game or The game is draw/tie |

## Table no 1: High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  HL_01       | **Sudoku Companion Input/Output**: Test basic input/output function| Path to txt file containing puzzle|SudokuGrid|SudokuGrid|Requirement based |
|  HL_02       |**Sudoku Puzzle Solver**: Test to verify the solution provided by solver function|Path to txt file containing puzzle| Solved grid as a string|Solved grid as a string|Requirement based   |
|  HL_03      |**Sudoku Puzzle Issolvable**: Test to verify if given puzzle is sovable |Path to txt file containing puzzle|True or False| Can/cannot be solved|Requirement based |


## Table no 2: Low level test plan

| **Test ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  LL_01  |**Sudoku Puzzle Cleanread data**: Test to verify if data is read correctly| String containing values |Modified String   |Modified String as desired |Scenario based |
|  LL_02   |**Sudoku Puzzle Hint**: Test to verify if provided hint is valid|Path to txt file containing puzzle|Partially solved grid |Partially solved grid as expected|Requirement based |
|  LL_03  |**Sudoku Puzzle Value**: Test to verify if value entered is right or wrong| row,column and value |True or False |True or false as expected|Scenario based |
|  LL_04   |**Sudoku Puzzle ValidateCleanedData**: Test to validate if given data is in right format| String containing values |True or False|True or False as expected | Scenario based |
|  LL_05   |**Sudoku Puzzle Save**: Test to verify if file is saved successfully|Path to txt file  |File containing puzzle |File saved as expected|Scenario based |


