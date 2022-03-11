from pickle import FALSE
from re import X
import time
import os
import numpy as np

from constants import *
from king import King
from walls import Wall
from buildings import Building
from spells import Spells

class Game():
    def __init__(self):
        self.run = True
        self.replay = False
        self.game_frames = 0
        self.key = ''
        self.game_mov_frame_dict = {}
        self.board = np.zeros((ROWS_V,COLS_V), dtype=object)
        #king vals
        self.walls = []
        self.buildings = []
        self.troops = []
        self.king = ''
        self.build_dict = ''
        self.wall_dict = ''
        self.troop_list = []
        self.printer = ''
        self.start_time = 0
        self.troop_move_time = TR_AT_TIME
        self.build_att_time = BU_AT_TIME
        self.spell = ''
        #calling functions
        self.create_board()

    #create board
    def create_board(self):
        for i in range(ROWS_V):
            # self.board.append([])
            for j in range(COLS_V):
                self.board[i][j] = CHAR_DEA
        # self.board[X_KING][Y_KING] = self.king_note
        #create walls into the board
        self.king = King(self)
        self.spell = Spells(self)
        #initilaizing lists to make a dictionary of buildings
        dict_keys_b = []
        dict_values_b = []
        dict_keys_w = []
        dict_values_w = []

        for wall in TH_BLOCKS_AROUND:
            self.walls.append(Wall(self,wall[0],wall[1],wall[2])) 
            dict_keys_w.append(tuple([wall[0],wall[1]]))
            dict_values_w.append(self.walls[-1])
        self.wall_dict = dict(zip(dict_keys_w,dict_values_w))

        
        #add town hall to the board
        self.buildings.append(Building(self,np.array(TH_BLOCKS),10,CHAR_TH,False,0,self.start_time))
        #add HUT1 to the board
        self.buildings.append(Building(self,np.array(H1_BLOCKS),10,CHAR_H1,False,0,self.start_time))
        self.buildings.append(Building(self,np.array(H2_BLOCKS),10,CHAR_H2,False,0,self.start_time))
        self.buildings.append(Building(self,np.array(H3_BLOCKS),10,CHAR_H3,False,0,self.start_time))

        #add defender to the board
        # self.buildings.append(Defender(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,C1_ATTACK,C1_HEALTH))
        self.buildings.append(Building(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,True,C1_ATTACK,self.start_time)) 
        self.buildings.append(Building(self,np.array(C2_BLOCKS),C2_HEALTH,CHAR_C2,True,C2_ATTACK,self.start_time))
        #put building coordinates and cuilding class into a dictionary
        for building in self.buildings:
            if building.actual_char != CHAR_WALL:
                for i in building.coords.tolist():
                    dict_keys_b.append(tuple(i))
                    dict_values_b.append(building)
                self.build_dict = dict(zip(dict_keys_b,dict_values_b))
        
    #print board
    def print_board(self):
        # for row in self.board:
        #     # print(''.join(row))
        #     print(*row, sep='')
        print('\n'.join(map(''.join, self.board)))
        #print king health bar
        print("\n")
        if self.king != '':
            print("Kings Health Bar: " + self.king.health_bar_calc())
        else:
            print("King is Dead!")

        # print(self.key)
        print(self.game_frames)
        # print(self.game_mov_frame_dict)
        # print(self.key)
        # print(self.game_mov_tim_dict)
        #print wall dictionary
        # print(self.troops)
        #print kings health bar
        # print(self.king[0].health)
        #print health of troops
        # print("\n")
        # for tr in self.troops:
        #     print(tr.troop_health)
        #print all dictionary values
        # for wall in self.walls:
        #     print("Wall " + str(wall.x) + " " + str(wall.y) + " " + str(wall.wall_health) + ' ' + str(wall.char))
        # #print buildings health
        # for building in self.buildings:
        #     print("Building " + str(building.bu_health) + ' ' + str(building.bu_char))

        

    


