from pickle import FALSE
import colorama
from colorama import Fore, Back, Style

from constants import *

class Wall:
    def __init__(self, game, x, y, health):
        self.game = game
        self.x = x
        self.y = y
        self.king_hit = False
        self.damage_taken = 0
        self.char = '| W |'
        self.wall_health = health
        self.display()
        
    def reset_wall(self):
        self.wall_health = HP_WALL
        self.char = '| W |'

    def king_attack(self):
        # if self.king_hit == True:
        self.wall_health -= self.damage_taken
        self.char = '| W |'
        self.king_hit = False
        self.damage_taken = 0
        self.display()
    

    def display(self):
        #colorama style reset
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

    

        
