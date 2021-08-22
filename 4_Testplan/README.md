# TESTPLAN MD FILE HERE

## Tic-Tac-Toe

### Table no 1: High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  HL_01       | Tic-Tac-Toe : 1 player Game |Number from 1 to 9|Win/loss/Draw|Win/loss/Draw|Requirement based |
|  HL_02       | Tic-Tac-Toe : 2 player Game |Number from 1 to 9|Win/loss/tie|Win/loss/tie|Requirement based |




### Table no 2: Low level test plan

| **Test ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  LL_01  |Test to verify whether user wants to play the game or not| NA | 'y' or 'n' | y' or 'n' as expected | Requirement based |
|  LL_02   |Test to verify the position in playboard|Number from 1 to 9| Corresponding position occupied |Position occupied as expected|Requirement based |
|  LL_03  |Test to verify letter in particular position| NA |'X' or 'O' at particular position |Playboard with 'X' or  'O' at particular position as expected| Requirement based|
|  LL_04   |Test to verify whether playboard is occupied completely| Playboard |True or False|True or False as expected | Requirement based |
|  LL_05   |Test to verify whether given location is occupied or not| Number from 1 to 9 |True or False  |True or false as expected|Requirement based |


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


