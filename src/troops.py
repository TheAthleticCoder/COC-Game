import time
import colorama
import numpy as np
from colorama import Fore, Back, Style
from time import ctime, perf_counter

from numpy import full

from constants import *

class Troop:
    def __init__(self,game, coords, health, char, attack, tot_health,start_time):
        self.game = game
        self.coords = coords
        self.troop_time = start_time
        self.damage_taken = 0
        self.attack_given = attack
        self.troop_char = char
        self.actual_char = char
        self.troop_health = health
        self.tot_health = tot_health
        self.display()

    #compare distance between troop and building and move towards it
    def move(self):
        if bool(self.game.build_dict) == True:
            dicti = self.game.build_dict
            full_attack_x = False
            full_attack_y = False
            #sort dictionary based on difference between key and coords
            sorted_dict = dict(sorted(dicti.items(), key=lambda x: abs(x[0][0]-self.coords[0])+abs(x[0][1]-self.coords[1])))
            #get first key and value of the dictionary
            f_key, f_value = list(sorted_dict.items())[0]
            x_dest = f_key[0]
            y_dest = f_key[1]
            b = list(sorted_dict.values())[0]
            # reset current position in the board to empty
            self.game.board[self.coords[0]][self.coords[1]] = '|   |'

            #move troop towards x_dest and y_dest only if the next block of the troop is empty or occupied by another troop
            #if troop is unable to move to next block, attack the building
            #check if all blocks arround the troop are empty or occupied by another troop

            # if self.coords[0] < x_dest and self.game.board[self.coords[0]+1][self.coords[1]] == '|   |':
            #     if self.coords[1] < y_dest and self.game.board[self.coords[0]+1][self.coords[1]+1] == '|   |':
            #         self.coords[0] += 1
            #         self.coords[1] += 1
            #     elif self.coords[1] > y_dest and self.game.board[self.coords[0]+1][self.coords[1]-1] == '|   |':
            #         self.coords[0] += 1
            #         self.coords[1] -= 1
            # elif self.coords[0] > x_dest and self.game.board[self.coords[0]-1][self.coords[1]] == '|   |':
            #     if self.coords[1] < y_dest and self.game.board[self.coords[0]-1][self.coords[1]+1] == '|   |':
            #         self.coords[0] -= 1
            #         self.coords[1] += 1
            #     elif self.coords[1] > y_dest and self.game.board[self.coords[0]-1][self.coords[1]-1] == '|   |':
            #         self.coords[0] -= 1
            #         self.coords[1] -= 1
            # else:
            #     #search if there is a wall in that direction
            #     for wall in self.game.wall_dict:
            #         if wall[0] == self.coords[0] and wall[1] == self.coords[1]:
            #             if wall[2] == 'x':
            #                 full_attack_x = True
            #             elif wall[2] == 'y':
            #                 full_attack_y = True

            if self.coords[0] < x_dest and self.game.board[self.coords[0]+1][self.coords[1]] == '|   |' or self.game.board[self.coords[0]+1][self.coords[1]] == '| B |':
#                if a wall comes in between, break the wall

                self.coords[0] += 1
            elif self.coords[0] > x_dest and self.game.board[self.coords[0]-1][self.coords[1]] == '|   |' or self.game.board[self.coords[0]-1][self.coords[1]] == '| B |':
                self.coords[0] -= 1
            else:
                full_attack_x = True
            if self.coords[1] < y_dest and self.game.board[self.coords[0]][self.coords[1]+1] == '|   |' or self.game.board[self.coords[0]][self.coords[1]+1] == '| B |':
                self.coords[1] += 1
            elif self.coords[1] > y_dest and self.game.board[self.coords[0]][self.coords[1]-1] == '|   |' or self.game.board[self.coords[0]][self.coords[1]-1] == '| B |':
                self.coords[1] -= 1
            else:
                full_attack_y = True
            if full_attack_x == True and full_attack_y == True:
                self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
            self.game.buildings[int(self.game.buildings.index(b))].display()
            self.display()


        #print first value in the dictionary
        # b = list(sorted_dict.values())[0]
        # self.game.printer = self.game.buildings[int(self.game.buildings.index(b))].coords

        #sort dictionary and list based on list
        #move diagonally towards 
        



    def display(self):
        self.troop_char = self.actual_char
        if self.troop_health >= self.tot_health*0.5:
            self.colour = Fore.GREEN
        elif self.troop_health >= self.tot_health*0.2 and self.troop_health < self.tot_health*0.5:
            self.colour = Fore.YELLOW
        elif self.troop_health < self.tot_health*0.2:
            self.colour = Fore.RED
        self.troop_char = self.colour + self.troop_char + Fore.RESET
        self.game.board[self.coords[0]][self.coords[1]] = self.troop_char

    def check_troop(self):
        if self.troop_health <= 0:
            return True

        