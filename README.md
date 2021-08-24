# SDLC Mini Arcade Game
| Unit Test | Code Quality| Git Inspector|
|-----------|-------------|--------------|
|[![Pytest-Miniarcade](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/unittest.yml/badge.svg)](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/unittest.yml)|[![Flake8](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/flake8.yml/badge.svg)](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/flake8.yml)|[![Contribution Check - Git Inspector](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/gitinspector.yml/badge.svg)](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/gitinspector.yml)|
|[![Pytest-2048 ](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/2048ptest.yml/badge.svg)](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/2048ptest.yml)|
|[![Pytest-TicTacToe](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/ptesttictactoe.yml/badge.svg)](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/ptesttictactoe.yml)|
|[![Pytest-Sudoku](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/ptestsudoku.yml/badge.svg)](https://github.com/yasirfaizahmed/SDLC_2_Electron/actions/workflows/ptestsudoku.yml)|

## Demo
![Demo gif](https://github.com/yasirfaizahmed/SDLC_2_Electron/blob/master/6_ImagesAndVideos/demo.gif)


## Running the program
Navigate to the directory containing this project after cloning from the terminal. Run the following commands:
* `cd 3_Implementation/`
* `python game2048.py` to launch GUI games, includes all 2 GUI games + 1 console game
* `python main.py` to launch console game seperately

### Note:
1. Please install the `ARCADE_I.TTF` font present in the `3_Implementation/` directory, just open the font file to install it.
2. Install the following pip packages: `turtle`, `pickle`, `mock`.

        pip install pickle-mixin
    
        pip install turtle
        
        pip install mock

4. For Sudoku Companion have the sudoku game as comma separated text file like `3_Implementation/SudokuCompanion/puzzle.txt`.
## Folder Structure

|         Folder    	  | 			Description 		    |
| ----------------------- | ----------------------------------------------  |
| 	1_Requirements    | Documents detailing requirements and research   |
| 	2_Design	  | Documents specifying design details        	    |
| 	3_Implementation  | All code and documentation        		    |
| 	4_test_plan	  | Documents with test plans and procedures        |
| 5_Report       | Folder consisting of documentation of the project 
| 6_ImagesAndVideos   | Images and Videos 
## Contributors List and Summary

PS No. |  Name   |    Features    | Issues Raised |Issues Resolved|No Test Cases|Test Case Pass
-------|-------------|----------------|----------------|---------------|-------------|--------------
`99005667` | Swathi  Ramachandran |  Tic-Tac-Toe 1 Player : Multifile, Unit tests, Testplan, Low level requirement, Object diagram |      | 1 | 7  | 7
`99005660` | Bhargav  R | SudokuCompanion: FileI/O, Grid Representation and Providing Hint Feature Few, Unit Tests and Few HLR and LLR | 1    |    | 8  | 8  
`99005364` | Prakhar  Deep |  Tic-Tac-Toe 2 player : Multifile, flowchart, low level requirement  |      |   1 |   2|   2 
`99005468` | Ayush  Bishnoi |  2048 game engine and binary score keeper   |      |    |11    | 11    
`99005584` | Saurav  Raja  |SudokuComapanion:Usecase UML,Flowchart,Testplan and Implementation     |      | 1   |   |
`99005637` | Prajwal  M| Tic-Tac-Toe : Requirements,Class diagram UML, Testplan and Implementation     |      |    | 1  | 1
`99005638` | Kamarthi Vignesh  Sai | Tic Tac Toe game, Activity diagram, Flowchart     |      |    | 1  | 1   
`99005688` | Tankasala  Gaanalola  | Tic Tac Toe, Requiements - SWOT Analysis, 4 W's 1H     |      |    |   |  
`99005679` | Annappa  M | SudokuCompanion: Sudoku Grid Issolvable logic, Solver Logic, Usecase UML,Testplan,few LLR and 2 unit tests   |      | 1   |2    |2    
`99005635` | Yaseer Faiz Ahmed |Menu GUI, 2048 GUI, TicTacToe GUI, integrating all game files to work together |      |    |0   | 0
## Challenges Faced and How Was It Overcome

1. Faced issues with integrating the modules because each of us had a different coding style. But eventually, reading through code and undersanding it helped us modify it and integrate it accordingly.
2. Testing was something new to each and everyone of us in Python. We had to start from scratch and learn how to write test files for python programs.
3. Following and keeping track of every process in SDLC was very difficult. With constant support and hardwork, we were able to atleast keep up with atleast half of it.
4. Working within the time constraint was difficult.
