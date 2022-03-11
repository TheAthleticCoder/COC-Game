import colorama
import time
from colorama import Fore, Back, Style

from constants import *

#Create Class Building and wall in order to build inorder to inherit other components from it
class Building:
    def __init__(self, game, coords, health, char, attack_mode, attack_damage, timeT):
        self.game = game
        self.coords = coords
        self.king_hit = False
        self.damage_taken = 0
        self.bu_char = char
        self.actual_char = char
        self.attack_mode = attack_mode
        self.attack_damage = attack_damage
        self.bu_health = health
        self.building_time = timeT
        self.display()

    #Use the building to attack troops and king
    def bu_attack(self):
        if self.attack_mode == True:
            build_list = self.coords.tolist()
            #check if self.game.troops is empty
            if bool(self.game.troops) == True:
                for troop in self.game.troops:
                    coord_list = troop.coords.tolist()
                    if (abs(coord_list[0]-build_list[0][0]) <= 5 and abs(coord_list[1]-build_list[0][1]) <= 5):
                        troop.troop_health -= self.attack_damage
                        troop.display()
                        self.display()
                        break
                    #add elif case if needed, else leave it
        #else attack the king using the king's attack damage
            elif self.game.king != '':
                if (abs(build_list[0][0]-self.game.king.x) <= 5 and abs(build_list[0][1]-self.game.king.y) <= 5):
                    self.game.king.health -= self.attack_damage
                    self.game.king.colour_change_king()
                    self.display()
        
    #change grid value when display function is called
    def display(self):
        self.bu_char = self.actual_char
        if self.bu_health >= HP_TH*0.5:
            self.colour = Fore.BLACK + Back.GREEN
        elif self.bu_health >= HP_TH*0.2 and self.bu_health < HP_TH*0.5:
            self.colour = Fore.BLACK + Back.YELLOW
        elif self.bu_health < HP_TH*0.2:
            self.colour = Fore.BLACK + Back.RED
        self.bu_char = self.colour + self.bu_char + Fore.RESET + Back.RESET
        for build in self.coords.tolist():
            self.game.board[build[0]][build[1]] = self.bu_char

    #check for building health 
    def check_bu(self):
        if self.bu_health <= 0:
            return True
    
    #remove building
    def remove_bu(self):
        for build in self.coords.tolist():
            self.game.board[build[0]][build[1]] = CHAR_DEA
class Wall:
    def __init__(self, game, x, y, health):
        self.game = game
        self.x = x
        self.y = y
        self.king_hit = False
        self.damage_taken = 0
        self.char = CHAR_WALL
        self.actual_char = CHAR_WALL
        self.wall_health = health
        self.display()
    
    #display wall by changing grid value
    def display(self):
        #colorama style reset
        self.char = self.actual_char
        health = self.wall_health
        if health >= HP_WALL*0.5:
            self.colour = Fore.BLACK + Back.GREEN
        elif health >= HP_WALL*0.2 and self.wall_health < HP_WALL*0.5:
            self.colour = Fore.BLACK + Back.YELLOW
        elif health < HP_WALL*0.2:
            self.colour = Fore.BLACK + Back.RED
        self.char = self.colour + self.char + Fore.RESET + Back.RESET
        self.game.board[self.x][self.y] = self.char

    #check if wall is destroyed
    def check_wall(self):
        if self.wall_health <= 0:
            return True


