from pickle import FALSE
from re import X
import time
import os
import numpy as np

from constants import *
from king import King
from queen import Queen
# from walls import Wall
from buildings import Building, Wall
from spells import Spells

class Game():
    def __init__(self,hero,level):
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
        self.aerial_troops = []
        self.hero = ''
        self.king = ''
        self.queen = ''
        self.build_dict = ''
        self.new_build_dict = ''
        self.wall_dict = ''
        self.troop_list = []
        self.printer = ''
        self.start_time = 0
        self.aerial_troops_list = []
        self.queen_time = 1
        self.queen_state = False
        self.hero_state = 0
        self.troop_move_time = TR_AT_TIME
        self.build_att_time = BU_AT_TIME
        self.spell = ''
        #calling functions
        #troop counts
        self.algo_arr = [[0 for i in range(ROWS_V)] for j in range(COLS_V)]
        self.temp = ''
        self.barb_count = 0
        self.arch_count = 0
        self.ball_count = 0
        self.curr_level = level
        self.create_board(hero,level)

    #create board
    def create_board(self, hero,level):
        if level == 1:
            for i in range(ROWS_V):
                # self.board.append([])
                for j in range(COLS_V):
                    self.board[i][j] = CHAR_DEA
            # self.board[X_KING][Y_KING] = self.king_note
            #create walls into the board
            # if self.game_hero == 'k':
            #     self.king = King(self)
            if hero == 'k':
                self.hero_state = 1
                self.king = King(self)
                self.hero = 'k'
            elif hero == 'q':
                self.hero_state = 2
                self.queen = Queen(self)
                self.hero = 'q'
            
            
            # elif self.game_hero == 'q':
            #     self.queen = Queen(self)

            self.spell = Spells(self)
            #initilaizing lists to make a dictionary of buildings
            dict_keys_b = []
            dict_values_b = []
            dict_keys_w = []
            dict_values_w = []

            for wall in TH_BLOCKS_AROUND:
                self.walls.append(Wall(self,wall[0],wall[1],wall[2])) 
                self.algo_arr[wall[0]][wall[1]] = -1
                dict_keys_w.append(tuple([wall[0],wall[1]]))
                dict_values_w.append(self.walls[-1])
            self.wall_dict = dict(zip(dict_keys_w,dict_values_w))

            
            #add town hall to the board
            self.buildings.append(Building(self,np.array(TH_BLOCKS),10,CHAR_TH,False,0,self.start_time))
            #add HUT1 to the board
            self.buildings.append(Building(self,np.array(H1_BLOCKS),10,CHAR_H1,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H2_BLOCKS),10,CHAR_H2,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H3_BLOCKS),10,CHAR_H3,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H4_BLOCKS),10,CHAR_H4,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H5_BLOCKS),10,CHAR_H5,False,0,self.start_time))

            #add defender to the board
            # self.buildings.append(Defender(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,C1_ATTACK,C1_HEALTH))
            self.buildings.append(Building(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,True,C1_ATTACK,self.start_time)) 
            self.buildings.append(Building(self,np.array(C2_BLOCKS),C2_HEALTH,CHAR_C2,True,C2_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W1_BLOCKS),W1_HEALTH,CHAR_W1,True,W1_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W2_BLOCKS),W2_HEALTH,CHAR_W2,True,W2_ATTACK,self.start_time))
            #put building coordinates and cuilding class into a dictionary
            new_dict_keys_b = []
            new_dict_values_b = []
            for building in self.buildings:
                if building.actual_char != CHAR_WALL:
                    for i in building.coords.tolist():
                        self.algo_arr[i[0]][i[1]] = -1
                        dict_keys_b.append(tuple(i))
                        dict_values_b.append(building)
                    if building.attack_mode == True:
                        for i in building.coords.tolist():
                            new_dict_keys_b.append(tuple(i))
                            new_dict_values_b.append(building)
                    self.build_dict = dict(zip(dict_keys_b,dict_values_b))
                    self.new_build_dict = dict(zip(new_dict_keys_b,new_dict_values_b))
        elif level == 2:
            for i in range(ROWS_V):
                # self.board.append([])
                for j in range(COLS_V):
                    self.board[i][j] = CHAR_DEA
            # self.board[X_KING][Y_KING] = self.king_note
            #create walls into the board
            # if self.game_hero == 'k':
            #     self.king = King(self)
            if hero == 'k':
                self.king = King(self)
                self.hero = 'k'
            elif hero == 'q':
                self.queen = Queen(self)
                self.hero = 'q'
            
            
            # elif self.game_hero == 'q':
            #     self.queen = Queen(self)

            self.spell = Spells(self)
            #initilaizing lists to make a dictionary of buildings
            dict_keys_b = []
            dict_values_b = []
            dict_keys_w = []
            dict_values_w = []

            for wall in TH_BLOCKS_AROUND:
                self.walls.append(Wall(self,wall[0],wall[1],wall[2]))
                self.algo_arr[wall[0]][wall[1]] = -1 
                dict_keys_w.append(tuple([wall[0],wall[1]]))
                dict_values_w.append(self.walls[-1])
            self.wall_dict = dict(zip(dict_keys_w,dict_values_w))

            
            #add town hall to the board
            self.buildings.append(Building(self,np.array(TH_BLOCKS),10,CHAR_TH,False,0,self.start_time))
            #add HUT1 to the board
            self.buildings.append(Building(self,np.array(H1_BLOCKS),10,CHAR_H1,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H2_BLOCKS),10,CHAR_H2,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H3_BLOCKS),10,CHAR_H3,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H4_BLOCKS),10,CHAR_H4,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H5_BLOCKS),10,CHAR_H5,False,0,self.start_time))

            #add defender to the board
            # self.buildings.append(Defender(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,C1_ATTACK,C1_HEALTH))
            self.buildings.append(Building(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,True,C1_ATTACK,self.start_time)) 
            self.buildings.append(Building(self,np.array(C2_BLOCKS),C2_HEALTH,CHAR_C2,True,C2_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(C3_BLOCKS),C3_HEALTH,CHAR_C3,True,C3_ATTACK,self.start_time))
            
            self.buildings.append(Building(self,np.array(W1_BLOCKS),W1_HEALTH,CHAR_W1,True,W1_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W2_BLOCKS),W2_HEALTH,CHAR_W2,True,W2_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W3_BLOCKS),W3_HEALTH,CHAR_W3,True,W3_ATTACK,self.start_time))
            #put building coordinates and cuilding class into a dictionary
            new_dict_keys_b = []
            new_dict_values_b = []
            for building in self.buildings:
                if building.actual_char != CHAR_WALL:
                    for i in building.coords.tolist():
                        self.algo_arr[i[0]][i[1]] = -1
                        dict_keys_b.append(tuple(i))
                        dict_values_b.append(building)
                    if building.attack_mode == True:
                        for i in building.coords.tolist():
                            new_dict_keys_b.append(tuple(i))
                            new_dict_values_b.append(building)
                    self.build_dict = dict(zip(dict_keys_b,dict_values_b))
                    self.new_build_dict = dict(zip(new_dict_keys_b,new_dict_values_b))
        elif level == 3:
            for i in range(ROWS_V):
                # self.board.append([])
                for j in range(COLS_V):
                    self.board[i][j] = CHAR_DEA
            # self.board[X_KING][Y_KING] = self.king_note
            #create walls into the board
            # if self.game_hero == 'k':
            #     self.king = King(self)
            if hero == 'k':
                self.king = King(self)
                self.hero = 'k'
            elif hero == 'q':
                self.queen = Queen(self)
                self.hero = 'q'
            
            
            # elif self.game_hero == 'q':
            #     self.queen = Queen(self)

            self.spell = Spells(self)
            #initilaizing lists to make a dictionary of buildings
            dict_keys_b = []
            dict_values_b = []
            dict_keys_w = []
            dict_values_w = []

            for wall in TH_BLOCKS_AROUND:
                self.walls.append(Wall(self,wall[0],wall[1],wall[2])) 
                self.algo_arr[wall[0]][wall[1]] = -1
                dict_keys_w.append(tuple([wall[0],wall[1]]))
                dict_values_w.append(self.walls[-1])
            self.wall_dict = dict(zip(dict_keys_w,dict_values_w))

            
            #add town hall to the board
            self.buildings.append(Building(self,np.array(TH_BLOCKS),10,CHAR_TH,False,0,self.start_time))
            #add HUT1 to the board
            self.buildings.append(Building(self,np.array(H1_BLOCKS),10,CHAR_H1,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H2_BLOCKS),10,CHAR_H2,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H3_BLOCKS),10,CHAR_H3,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H4_BLOCKS),10,CHAR_H4,False,0,self.start_time))
            self.buildings.append(Building(self,np.array(H5_BLOCKS),10,CHAR_H5,False,0,self.start_time))

            #add defender to the board
            # self.buildings.append(Defender(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,C1_ATTACK,C1_HEALTH))
            self.buildings.append(Building(self,np.array(C1_BLOCKS),C1_HEALTH,CHAR_C1,True,C1_ATTACK,self.start_time)) 
            self.buildings.append(Building(self,np.array(C2_BLOCKS),C2_HEALTH,CHAR_C2,True,C2_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(C3_BLOCKS),C3_HEALTH,CHAR_C3,True,C3_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(C4_BLOCKS),C4_HEALTH,CHAR_C4,True,C4_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W1_BLOCKS),W1_HEALTH,CHAR_W1,True,W1_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W2_BLOCKS),W2_HEALTH,CHAR_W2,True,W2_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W3_BLOCKS),W3_HEALTH,CHAR_W3,True,W3_ATTACK,self.start_time))
            self.buildings.append(Building(self,np.array(W4_BLOCKS),W4_HEALTH,CHAR_W4,True,W4_ATTACK,self.start_time))
            #put building coordinates and cuilding class into a dictionary
            new_dict_keys_b = []
            new_dict_values_b = []
            for building in self.buildings:
                if building.actual_char != CHAR_WALL:
                    for i in building.coords.tolist():
                        self.algo_arr[i[0]][i[1]] = -1
                        dict_keys_b.append(tuple(i))
                        dict_values_b.append(building)
                    if building.attack_mode == True:
                        for i in building.coords.tolist():
                            new_dict_keys_b.append(tuple(i))
                            new_dict_values_b.append(building)
                    self.build_dict = dict(zip(dict_keys_b,dict_values_b))
                    self.new_build_dict = dict(zip(new_dict_keys_b,new_dict_values_b))
    #print board
    def print_board(self):
        print('\n'.join(map(''.join, self.board)))
        print('\n')
        #print king health bar
        #print current level
        print('Level: ' + str(self.curr_level))
        if self.king != '':
            print("Kings Health Bar: " + self.king.health_bar_calc())
        elif (self.hero_state == 1):
            print("King is Dead!")

        if self.queen != '':
            print("Queens Health Bar: " + self.queen.health_bar_calc())
        elif (self.hero_state == 2):
            print("Queen is Dead!")

        #print size of algo_arr
        # print('Size of algo_arr: ' + str(sum([i.count(-1) for i in self.algo_arr])))
        #print the number of -1s in algo_arr

        # print('Number of -1s in algo_arr: ' + str(self.algo_arr.count(-1)))
        # # if self.hero != '':
        # #     print("Heros Health Bar: " + self.hero.health_bar_calc())

        print("Barbarians Deployed: " + str(self.barb_count))
        print("Archers Deployed: " + str(self.arch_count))
        print("Balloons Deployed: " + str(self.ball_count))



        

    


