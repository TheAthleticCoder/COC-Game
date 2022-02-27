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
        self.troops = []
        self.build_dict = ''
        self.printer = ''
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

        #initilaizing lists to make a dictionary of buildings
        dict_keys = []
        dict_values = []

        for wall in WALLS:
            self.walls.append(Wall(self,wall[0],wall[1],wall[2]))

        #add town hall to the board
        self.buildings.append(Building(self,np.array(TH_BLOCKS),10,CHAR_TH))
        #add HUT1 to the board
        self.buildings.append(Building(self,np.array(H1_BLOCKS),10,CHAR_H1))


        #put building coordinates and cuilding class into a dictionary
        for building in self.buildings:
            if building.actual_char != CHAR_WALL:
                for i in building.coords.tolist():
                    dict_keys.append(tuple(i))
                    dict_values.append(building)
                self.build_dict = dict(zip(dict_keys,dict_values))
        
    #print board
    def print_board(self):
        # for row in self.board:
        #     # print(''.join(row))
        #     print(*row, sep='')
        print('\n'.join(map(''.join, self.board)))
        #print king health bar
        print("\n")
        print("Kings Health Bar: " + self.health_bar)
        print(self.printer)
        #print all dictionary values
        # for wall in self.walls:
        #     print("Wall " + str(wall.x) + " " + str(wall.y) + " " + str(wall.wall_health) + ' ' + str(wall.char))
        # #print buildings health
        for building in self.buildings:
            print("Building " + str(building.bu_health) + ' ' + str(building.bu_char))

        

    


