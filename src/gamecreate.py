from re import X
import time
import os
import numpy as np

from constants import *
from king import King
from walls import Wall
from buildings import Building

class Game():
    def __init__(self):
        self.run = True
        self.board = np.zeros((ROWS_V,COLS_V), dtype=object)
        #king vals
        self.health_bar = ''
        self.king_note = ''

        self.walls = []
        self.buildings = []
        #calling functions
        self.create_board()

    #create board
    def create_board(self):
        for i in range(ROWS_V):
            # self.board.append([])
            for j in range(COLS_V):
                self.board[i][j] = '|   |'
        self.board[X_KING][Y_KING] = self.king_note
        #create walls into the board
        for wall in WALLS:
            self.walls.append(Wall(self,wall[0],wall[1],wall[2]))

        #add town hall to the board
        self.buildings.append(Building(self,np.array(TH_BLOCKS),10,CHAR_TH))
        
        # for i in X_SPAWN:
        #     for j in Y_SPAWN:
        #         self.board[i][j] = '| S |'            

    #print board
    def print_board(self):
        # for row in self.board:
        #     # print(''.join(row))
        #     print(*row, sep='')
        print('\n'.join(map(''.join, self.board)))
        #print king health bar
        print("\n")
        print("Kings Health Bar: " + self.health_bar)
        #print walls health 
        for wall in self.walls:
            print("Wall " + str(wall.x) + " " + str(wall.y) + " " + str(wall.wall_health) + ' ' + str(wall.char))
        #print buildings health
        for building in self.buildings:
            print("Building " + str(building.bu_health) + ' ' + str(building.bu_char))

        

    


