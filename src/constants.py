# We create game constants here

import colorama
from colorama import Fore, Back, Style,init

#Time
FPS = 90
T = 1/FPS

#Board dimensions
ROWS_V = 20
COLS_V = 20

#King position
X_KING = 1
Y_KING = 1
HP_KING = 50

#Wall class
ROWS_W = 1
COLS_W = 1
HP_WALL = 10
CHAR_WALL = '| W |'
WALLS = [[10,10,10],[10,11,10]]
NEW_WALLS = [[[5,4]],[[2,10]]]

#Town Hall
X_TH = 12
Y_TH = 12
HP_TH = 10
CHAR_TH = '| T |'
TH_BLOCKS = [[X_TH,Y_TH],[X_TH,Y_TH+1],[X_TH,Y_TH+2],[X_TH,Y_TH+3],[X_TH+1,Y_TH],[X_TH+1,Y_TH+1],[X_TH+1,Y_TH+2],[X_TH+1,Y_TH+3],
[X_TH+2,Y_TH],[X_TH+2,Y_TH+1],[X_TH+2,Y_TH+2],[X_TH+2,Y_TH+3]]

#HUT 1
X_H1 = 3
Y_H1 = 3
HP_H1 = 10
CHAR_H1 = '| H |'
H1_BLOCKS = [[X_H1,Y_H1],[X_H1, Y_H1+1]]

#Spawn locations
X_SPAWN = [ROWS_V-2,1,ROWS_V-2]
Y_SPAWN = [2,COLS_V-2,COLS_V-2]
SPAWN_POINTS = [[ROWS_V-2,2],[1,COLS_V-2],[ROWS_V-2,COLS_V-2]]

#Defender class
CHAR_C1 = '| C |'
X_C1 = 16
Y_C1 = 16
HP_C1 = 10
C1_BLOCKS = [[X_C1,Y_C1]]
C1_ATTACK = 1
C1_HEALTH = 10


#Barbs
BARB_HP = 10
BARB_CHAR = '| B |'
BARB_ATTACK = 1

#clock
clock = 0