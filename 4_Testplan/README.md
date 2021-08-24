# TESTPLAN MD FILE HERE


## Table no 1: High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  HL_01       | **Tic-Tac-Toe** : 1 player Game |Number from 1 to 9|Win/loss/Draw|Win/loss/Draw|Requirement based |
|  HL_02       | **Tic-Tac-Toe** : 2 player Game |Number from 1 to 9|Win/loss/tie|Win/loss/tie|Requirement based |
|  HL_03       | **Sudoku Companion Input/Output**: Test basic input/output function| Path to txt file containing puzzle|SudokuGrid|SudokuGrid|Requirement based |
|  HL_04       |**Sudoku Puzzle Solver**: Test to verify the solution provided by solver function|Path to txt file containing puzzle| Solved grid as a string|Solved grid as a string|Requirement based   |
|  HL_05      |**Sudoku Puzzle Issolvable**: Test to verify if given puzzle is sovable |Path to txt file containing puzzle|True or False| Can/cannot be solved|Requirement based |
|  HL_06      |**2048 Move Left**: Test to verify if all functions are performed correctly on a left move |gameboard |gameboard with left movement| gameboard with left movement|movement |
|  HL_07      |**2048 Move Up**: Test to verify if all functions are performed correctly on an up move |gameboard |gameboard with up movement| gameboard with up movement|movement |
|  HL_08      |**2048 Move Right**: Test to verify if all functions are performed correctly on a right move |gameboard |gameboard with right movement| gameboard with right movement|movement |
|  HL_09      |**2048 Move Down**: Test to verify if all functions are performed correctly on a down move |gameboard |gameboard with down movement| gameboard with down movement|movement |


## Table no 2: Low level test plan

| **Test ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  LL_01  | **Tic-Tac-Toe** :Test to verify whether user wants to play the game or not| user input('y' or 'n') | 'y' or 'n' | y' or 'n' as expected | Requirement based |
|  LL_02   | **Tic-Tac-Toe** :Test to verify the position in playboard|Number from 1 to 9| Corresponding position occupied |Position occupied as expected|Requirement based |
|  LL_03  | **Tic-Tac-Toe** :Test to verify letter in particular position| Number from 1 to 9 |'X' or 'O' at particular position |Playboard with 'X' or  'O' at particular position as expected| Requirement based|
|  LL_04   | **Tic-Tac-Toe** :Test to verify whether playboard is occupied completely| Playboard |True or False|True or False as expected | Requirement based |
|  LL_05   | **Tic-Tac-Toe** :Test to verify whether given location is occupied or not| Number from 1 to 9 |True or False|True or False as expected|Requirement based |
|  LL_06   | **Tic-Tac-Toe** :Test to verify the winner of the game| 'X' or 'O' |True or False|True or False as expected|Requirement based |
|  LL_07   | **Tic-Tac-Toe** :Test to verify computer move| From 1 to 9 |1 or 0|1 or 0 as expected|Requirement based |
|  LL_08   | **Tic-Tac-Toe** :Test to verify whether game is over or not| from 1 to 9 |True or False|True or False as expected|Requirement based |
|  LL_09  |**Sudoku Puzzle Cleanread data**: Test to verify if data is read correctly from file| String containing values |Modified String   |Modified String as desired |Scenario based |
|  LL_10   |**Sudoku Puzzle Hint**: Test to verify if provided hint is valid|Path to txt file containing puzzle|Partially solved grid |Partially solved grid as expected|Requirement based |
|  LL_11  |**Sudoku Puzzle Value**: Test to verify if value entered is right or wrong| row,column and value |True or False |True or false as expected|Scenario based |
|  LL_12   |**Sudoku Puzzle ValidateCleanedData**: Test to validate if given data is in right format| String containing values |True or False|True or False as expected | Scenario based |
|  LL_13   |**Sudoku Puzzle Save**: Test to verify if file is saved successfully|Path to txt file  |File containing puzzle |File saved as expected|Scenario based |
|  LL_14   |**2048 slam left**: Test to move all elements to the left|gameboard |gameboard with the correct moves |gameboard with the correct moves |core move test |
|  LL_15   |**2048 compress left**: Test to combine all similar elements to the left|gameboard |gameboard with the correct moves |gameboard with the correct moves |core move test |
|  LL_16   |**2048 transpose**: Test to swap rows and coloumns to perform further functions|gameboard |gameboard with rows as coloums |gameboard with the correct moves |core move test |
|  LL_17   |**2048 reverse**: Test to mirror rows|gameboard |gameboard with flipped rows |gameboard with the correct moves |core move test |
|  LL_18   |**2048 scoring**: Test to add tile values to score if the tile merges |gameboard |score |score |score tracker |
|  LL_19   |**2048 game over detection**: Test to check if there is 2048 in the gameboard|gameboard |True/False |True/False |game over |
