# REQUIREMENT MD FILE

## Introduction

### Tic-Tac-Toe 
Tic-Tac-Toe is a well known game played by two
persons who alternately place X's and O's upon a 3x3 playing field.
The players first decide who will mark his moves
with an X and who will go first. Play proceeds with the opponents
alternately placing their marks in any unoccupied cell 
The object of the game is to be the first player with 3
marks in a row, where a row can be either vertical, horizontal, or
diagonal. If all the cells become filled the game is a draw.

## Tic Tac Toe Detail requirements
## High Level Requirements

  ID |  Description  |    Category    |     Status    |
  -------|---------|----------------|----------------|
  HR01 | Display board  | Technical | |
  HR02 | Player move  |  Technical | |
  HR03 | Computer move |  Technical | |
  HR04 | Winner finder  |  Technical | |

##  Low level Requirements:
  ID  | Description                   | HLR ID | Status 
  ----|-------------------------------|--------|---------------------------
 LR01 | User shoud be able to input | HR02 | 
 LR02 | User should be able to take move | HR02 | 
 LR03 | Space is checked whether it is free  | HR02 | 
 LR04 | User should be able to insert letter | HR02 | 
 LR05 | Selection of random no | HR03 | 
 LR06 | Winner is decided   | HR03 | 



### 2048
2048 requirements:

functional:
1) movement physics - done
2) 2048 detector 
3) full board detector - partially done
4) score counter
5) difficulty selector - doable through changing distribution of 2 and 4
6) input sanitation

non functional:
1) sounds
2) timer
3) pretty UI
4) high score

### Sudoku Companion
Sudoku is a logic-based, combinatorial number-placement puzzle. Sudoku Companion is a mini-application which can be used to solve Sudoku puzzles more conveniently. It provides the following functions:
1. checking if a solution exists
2. provide hints 
3. solve puzzle entirely

## Research

### Cost and features
The cost requires only for software development and implementation of the software.

### Defining Our System


## SWOT Analysis
![swot analysis](https://user-images.githubusercontent.com/81503646/130212472-be28520b-a495-451c-972e-28a45c8b0101.png)


## 4W's and 1'H

### Who:
* Individuals looking for fun activities.
* Game lovers irrespective of their age group.
* These games are played between students and even experts to check their logical thinking.
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

## Detailed Requirements

### High Level Requirements

ID |  Description  |     Status    
---|---------------|----------------
HL03| **Sudoku Companion** : Provide tools to solve sudoku puzzle like hints, possible solution and check if a puzzle has a solution | ❌ 

### Low Level Requirements

ID  | Description                   | HLR ID | Status 
----|-------------------------------|--------|-------
LL0X | **Sudoku Puzzle Input / Output** : Read or Save a sudoku grid from or to a file | HL03 | ❌ 
LL0X | **Sudoku Puzzle Display**: Display Sudoku grid to the user | HL03 | ❌
LL0X | **Sudoku Puzzle Message**: Find if solution exists for the given puzzle or not | HL03 | ❌
LL0X | **Sudoku Puzzle Solve**: Solve the puzzle and display the same | HL03 | ❌
