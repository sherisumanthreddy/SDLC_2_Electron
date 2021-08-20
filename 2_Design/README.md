# DESIGN MD FILE


design:

High Level:
1) gameboard
2) game logic
3) scoring system
4) UI

Low Level:
1) collision detection
2) adding new numbers to the board
3) addition of tiles of the same number
4) randomly selecting where the new tiles appear (one way to implement this is to select a random number from 0 till 2 and then randomly select the positions from the empty tiles, and place either 2 or 4 (or 8 based on difficulty)  randomly on those spots)
5) game over detection