# DESIGN MD FILE

### 2048
design:

High Level:
1) gameboard
2) game logic - done
3) scoring system
4) UI

Low Level:
1) collision detection - done
2) adding new numbers to the board - done
3) addition of tiles of the same number - done
4) randomly selecting where the new tiles appear (one way to implement this is to select a random number from 0 till 2 and then randomly select the positions from the empty tiles, and place either 2 or 4 (or 8 based on difficulty)  randomly on those spots) - okay slight change here, upon research it was discovered that only one new tile appears randomly and there is a chance that it is either 2 or 4, difficulty dictates this split
5) game over detection - ya kind of works needs concrete logic