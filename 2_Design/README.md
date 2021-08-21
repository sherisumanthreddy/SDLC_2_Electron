# DESIGN MD FILE

### 2048
design:

High Level:
1) gameboard - done
2) game logic - done
3) scoring system
4) UI - gameboard done

Low Level:
1) collision detection - done
2) adding new numbers to the board - done
3) addition of tiles of the same number - done
4) randomly selecting where the new tiles appear (one way to implement this is to select a random number from 0 till 2 and then randomly select the positions from the empty tiles, and place either 2 or 4 (or 8 based on difficulty)  randomly on those spots) - okay slight change here, upon research it was discovered that only one new tile appears randomly and there is a chance that it is either 2 or 4, difficulty dictates this split
5) game over detection - ya kind of works needs concrete logic

## High Level Design

### Tic-Tac-Toe
### Usecase Diagram
![UseCase](https://user-images.githubusercontent.com/66193894/130224628-59df5222-5c62-4bf4-9e64-b2c190b3cb96.png)

### Activity Diagram
![ActivityDiagram](https://user-images.githubusercontent.com/66193894/130256678-15037fb4-0fbd-49c7-ab79-75bc213cf870.png)

### Class Diagram
![classdiagram](https://user-images.githubusercontent.com/80813102/130295145-c7d964d0-6ede-4646-bc94-ac79d09e312c.png)



## Low Level Design
### Flowchart
![Flowchart](https://user-images.githubusercontent.com/80392588/130255510-3240d7fc-7770-42f2-8274-bdd6b534d432.png)
