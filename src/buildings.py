import colorama
from colorama import Fore, Back, Style

from constants import *

class Building:
    def __init__(self, game, coords, health, char):
        self.game = game
        self.coords = coords
        self.king_hit = False
        self.damage_taken = 0
        self.bu_char = char
        self.actual_char = char
        self.bu_health = health
        self.display()

    def king_attack(self):
        # if self.king_hit == True:
        self.bu_health -= self.damage_taken
        self.bu_char = self.actual_char
        self.king_hit = False
        self.damage_taken = 0
        self.display()

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


