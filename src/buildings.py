import colorama
import time
from colorama import Fore, Back, Style

from constants import *

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

    def king_attack(self):
        # if self.king_hit == True:
        self.bu_health -= self.damage_taken
        self.bu_char = self.actual_char
        self.king_hit = False
        self.damage_taken = 0
        self.display()

    def bu_attack(self):
        if self.attack_mode == True:
            for troop in self.game.troops:
                coord_list = troop.coords.tolist()
                build_list = self.coords.tolist()
                if (abs(coord_list[0]-build_list[0][0]) <= 5 and abs(coord_list[1]-build_list[0][1]) <= 5):
                    troop.troop_health -= self.attack_damage
                    troop.display()
                    self.display()
                    break
        

    def display(self):
        #display based on health
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

    def check_bu(self):
        if self.bu_health <= 0:
            return True
    
    #remove building
    def remove_bu(self):
        for build in self.coords.tolist():
            self.game.board[build[0]][build[1]] = '|  |'


