# **COC-Game**
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/contains-tasty-spaghetti-code.svg)](https://forthebadge.com)

-----

This is a 2D Python3 (terminal-based) game, heavily inspired by Clash of clans where the user will control the king, move it up, down, forward and backwards while destroying buildings and fighting defences on its way. The game demonstrates concepts of object-oriented programming (OOPS) and simulates a basic version of Clash Of Clans. 

**This game was created as part of the Spring 2021 Design and Analysis of Software Systems course.**

-----
## **Objective Of The Game:**
The objective of the game is to destroy as many buildings as possible and collect the maximum
amount of loot while doing so. There will be an army of troops to help the king clean up.

-----

## **Running the game**

1. Clone the repository: `git clone https://github.com/TheAthleticCoder/COC-Game.git`
1. To run the game, \
   `python3 main.py` \
   For best results, have your terminal window in full screen mode.
2. To run the replay, \
   `python3 replay.py` 
---
## **Controls**
**In `main.py`, in the beginning, you need to choose your hero:**
- `k` to choose the King as the Hero.
- `q` to choose the Queen as the Hero.

**In `main.py`, the controls are:**
- `w` to make the king or queen **move up**.
- `a` to make the king or queen **move left**.
- `d` to make the king or queen **move right**.
- `s` to make the king or queen **move down**.
- `r` to use **rage spell**.
- `h` to use **heal spell**.
- `c`,`v`,`b` to **spawn barbarian troops** on the board.
- `g`,`j`,`k` to **spawn archer troops** on the board.
- `y`,`u`,`i` to **spawn balloon troops** on the board.
- `z` to use Kings **leviathan axe** which is the kings special attack (Particular to the King ONLY).
- `x` to use **ranged attack** which is the either the king's or the queen's special attack. 
- `q` to quit the game

**In `replay.py`, the controls are:**
- `<Numeral Input>` to choose the **replay number** for simulation.
- `1`,`2`,`3` to change the **replay speed**.

---
## **File Structure**

1. `README.md`: This is the README :) 
2. `game.py`: The main game file which is run to play the game.
3. `src`: folder containing any other code files.
4. `replays`: folder storing the necessary files for the replay.
5. `replay.py` : Python file needed for rendering a replay.

-----
