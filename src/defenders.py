import time
import colorama
import numpy as np
from colorama import Fore, Back, Style
from time import ctime, perf_counter

from numpy import full

from constants import *

class Defender:
    def __init__(self,game, coords, health, char, attack, tot_health):
        self.game = game
        self.coords = coords
        # self.defender_time = start_time
        self.king_hit = False
        self.damage_taken = 0
        self.attack_given = attack
        self.defender_char = char
        self.actual_char = char
        self.defender_health = health
        self.tot_health = tot_health
        self.display()

    # def attack_defender(self):
    #     # attack only 1 troop out of all troops in the range of 5 blocks of the defender
    #     for troop in self.game.troop_list:
    #         if abs(troop[0]-self.coords[0]) <= 5 and abs(troop[1]-self.coords[1]) <= 5:
    #             # troop_obj = self.game.troop_list[troop]
    #             # troop_obj.defender_health -= self.attack_given
    #             troop[3].defender_health -= self.attack_given
    #             self.damage_taken += self.attack_given
    #             if troop_obj.defender_health <= 0:
    #                 troop_obj.defender_health = 0
    #                 troop_obj.actual_char = 'X'
    #                 troop_obj.display()
    #                 del self.game.troop_list[troop]
    #             else:
    #                 troop_obj.display()
    #             break

    def check_bu(self):
        if self.defender_health <= 0:
            return True

    def display(self):
        if self.defender_health >= self.tot_health*0.5:
            self.colour = Fore.BLACK + Back.GREEN
        elif self.defender_health >= self.tot_health*0.2 and self.defender_health < self.tot_health*0.5:
            self.colour = Fore.BLACK + Back.YELLOW
        elif self.defender_health < self.tot_health*0.2:
            self.colour =  Fore.BLACK + Back.RED
        self.defender_char = self.colour + self.defender_char + Fore.RESET + Back.RESET
        for defe in self.coords.tolist():
            self.game.board[defe[0]][defe[1]] = self.defender_char
