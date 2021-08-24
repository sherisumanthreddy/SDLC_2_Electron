# REQUIREMENT MD FILE

## Introduction

To design a Mini Arcade game system to play 2048, Sudoku and Tic-Tac-Toe(1 player and 2 player) games based on user choice.

## Research

It is an all-in one gaming platform for various games where user can access different types of games in single application.

### Tic-Tac-Toe 
Tic-Tac-Toe is a well known game played by two
persons who alternately place X's and O's upon a 3x3 playing field.
The players first decide who will mark his moves
with an X and who will go first. Play proceeds with the opponents
alternately placing their marks in any unoccupied cell 
The object of the game is to be the first player with 3
marks in a row, where a row can be either vertical, horizontal, or
diagonal. If all the cells become filled the game is a draw.

![image](https://user-images.githubusercontent.com/80813102/130335359-4401ea44-590e-4e5d-a1ff-3a60758bee6d.png)

### Sudoku Companion

Sudoku is a logic-based, combinatorial number-placement puzzle. Sudoku Companion is a mini-application which can be used to solve Sudoku puzzles more conveniently. It improves the concentration and logical thinking. It provides the following functions:
1. checking if a solution exists
2. provide hints 
3. solve puzzle entirely

![image](https://user-images.githubusercontent.com/80813102/130348527-e3109d9e-1138-434f-afff-b2c4bec762d7.png)


### 2048

2048 presents with with a 4×4 grid. When you start the game, there will be two “tiles” on the grid, each displaying the number 2 or 4. You hit the arrow keys on your keyboard to move the tiles around — and also to generate new tiles, which will also be valued at 2 or 4. When two equal tiles collide, they combine to give you one greater tile that displays their sum. The more you do this, obviously, the higher the tiles get and the more crowded the board becomes. Your objective is to reach 2048 before the board fills up.

![image](https://user-images.githubusercontent.com/80813102/130348395-033b57ea-d359-4b08-b460-1c1bd244c3ca.png)


### Cost and features
The cost requires only for software development and implementation of the software. We can play 3 games using single Mini arcade game application.
The user can play the following games:
* 2048
* Sudoku
* Tic-Tac-Toe (1 player and 2 player)

## Features
* User can play multiple games like sudoku, tic tac toe and 2048.
* It is simple to use.
* User friendly.
* It has high performance.
* Accuracy in results.

### Defining Our System

The Mini Arcade Game system will ask user to select which game he wants to play by selecting the options 1,2,3,4& 5(1-2048, 2-sudoku, 3- 1player_tictactoe, 4- 2player_tictactoe,5- Exit).And then user will able to play the selected game and display of that game will open.


## SWOT Analysis
![swot analysis](https://user-images.githubusercontent.com/81503646/130212472-be28520b-a495-451c-972e-28a45c8b0101.png)


## 4W's and 1'H

### Who:
* Individuals looking for fun activities.
* Game lovers irrespective of their age group.
* These games are played between students and even experts to check their logical thinking and concentration.
* People of any economical background having a hobby of playing games

### What:
* It provides multiple gaming options.
* User can choose any game of his choice from the given list.

### When:
* These games can be played in a short interval of time if the user wants to prevent boredom, for relaxation and enjoyment.

### Where:
* It is simple and user-friendly, so it can be used in many domains.
* It can be used anywhere around the world by anyone who loves playing games.

### How:
* The system aims to provide smooth experience for users and should be implemented in least possible cost and efficient way.
* Users can attempt to play the games through any of the online medium


## Detail requirements

### High Level Requirements

ID |  Description  |     Status    |
---|---------------|----------------|
HL01|**2048** : Provide tools like game board,movement physics,score counter,difficulty selector and non functional requirements(sounds,timer,pretty UI &high score)|Implemented|
HL02| **Sudoku Companion** : Provide tools to solve sudoku puzzle like hints, possible solution and check if a puzzle has a solution | Implemented  |
HL03|**Tic tac toe** : Provide tools for display board,player move,computer move and winner finder for both 1player and 2player game| Implemented |



###  Low level Requirements

ID  | Description                   | HLR ID | Status 
----|-------------------------------|--------|-------
LL01 | **Sudoku Puzzle Input / Output** : Read or Save a sudoku grid from or to a file | HL02 | Implemented |
LL02 | **Sudoku Puzzle Display**: Display Sudoku grid to the user | HL02 | Implemented 
LL03 | **Sudoku Puzzle Message**: Find if solution exists for the given puzzle or not | HL02 | Implemented |
LL04 | **Sudoku Puzzle Solve**: Solve the puzzle and display the same | HL02 | Implemented |
LL05 | **Sudoku Puzzle Hint**: Provide hints for solving the sudoku puzzle| HL02 | Implemented |
LL06 | **Tic tac toe take input** : Ask whether user wants to play game of 1 player or 2 players|HL03| Implemented|
LL07 | **Tic tac toe print board** : Provide 3X3 board to play|HL03|Implemented|
LL08 | **Tic tac toe computermove** : Check empty squares and move accordingly|HL03|Implemented|
LL09 | **Tic tac toe player move** : Player can check the empty squares and can play accordingly|HL03|Implemented|
LL10 | **Tic tac toe winner** : Winner is decided by checking the board conditions | HL03 | Implemented |
LL11 | **2048 Movement physics** : Used to move right,left,up and down | HL01| Implemented |
Ll12 | **2048 Game board** : Display 2048 game board to the user | HL01 | Implemented |
LL13 | **2048 detector** : Detect 2048 on the game board | HL01 | Implemented |
LL14 | **2048 Scoring system** : Display scores on the game board | HL01 | Implemented |
LL15 | **2048 Non functional system** : Provide sounds,timer,high score and pretty UI|HL01 |Implemented|





 



### 2048
2048 requirements:

functional:
1) movement physics - done
2) 2048 detector - done
3) full board detector - done
4) score counter - done
5) difficulty selector - doable through changing distribution of 2 and 4
6) input sanitation

non functional:
1) sounds
2) timer
3) pretty UI - done
4) high score - done



