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
            self.game.board[self.coords[0]][self.coords[1]] = CHAR_DEA

            diff_x = abs(x_dest-self.coords[0])
            diff_y = abs(y_dest-self.coords[1])

            move_or_wall = False
            if diff_x == 0:
                if y_dest > self.coords[1]:
                    for wall in self.game.walls:
                        if wall.x == self.coords[0] and wall.y == self.coords[1]+1:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[1]+1 == y_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[1] += 1
                elif y_dest < self.coords[1]:
                    for wall in self.game.walls:
                        if wall.x == self.coords[0] and wall.y == self.coords[1]-1:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[1]-1 == y_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[1] -= 1
            elif diff_y == 0:
                if x_dest > self.coords[0]:
                    for wall in self.game.walls:
                        if wall.x == self.coords[0]+1 and wall.y == self.coords[1]:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[0]+1 == x_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[0] += 1
                elif x_dest < self.coords[0]:
                    for wall in self.game.walls:
                        if wall.x == self.coords[0]-1 and wall.y == self.coords[1]:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[0]-1 == x_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[0] -= 1
            else:
                if x_dest > self.coords[0] and y_dest > self.coords[1]:
                    #check if there is a wall in the way
                    for wall in self.game.walls:
                        if self.coords[0]+1 == wall.x and self.coords[1]+1 == wall.y:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[0]+1 == x_dest and self.coords[1]+1 == y_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[0] += 1
                        self.coords[1] += 1
                elif x_dest > self.coords[0] and y_dest < self.coords[1]:
                    #check if there is a wall in the way
                    for wall in self.game.walls:
                        if self.coords[0]+1 == wall.x and self.coords[1]-1 == wall.y:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[0]+1 == x_dest and self.coords[1]-1 == y_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[0] += 1
                        self.coords[1] -= 1
                elif x_dest < self.coords[0] and y_dest > self.coords[1]:
                    #check if there is a wall in the way
                    for wall in self.game.walls:
                        if self.coords[0]-1 == wall.x and self.coords[1]+1 == wall.y:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[0]-1 == x_dest and self.coords[1]+1 == y_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[0] -= 1
                        self.coords[1] += 1
                elif x_dest < self.coords[0] and y_dest < self.coords[1]:
                    #check if there is a wall in the way
                    for wall in self.game.walls:
                        if self.coords[0]-1 == wall.x and self.coords[1]-1 == wall.y:
                            move_or_wall = True
                            wall.wall_health -= self.attack_given
                            wall.display()
                            break
                    if self.coords[0]-1 == x_dest and self.coords[1]-1 == y_dest:
                        self.game.buildings[int(self.game.buildings.index(b))].bu_health -= self.attack_given
                    elif move_or_wall == False:
                        self.coords[0] -= 1
                        self.coords[1] -= 1
            
            self.game.buildings[int(self.game.buildings.index(b))].display()
            self.display()

    #display the position of the troop on the grid of the board
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

    #check for troops health in order to remove him from the board if dead
    def check_troop(self):
        if self.troop_health <= 0:
            return True

        