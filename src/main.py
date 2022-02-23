import colorama
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style

# custom modules
from constants import *
from input import input_to
from king import King
from gamecreate import *
from walls import Wall
from buildings import Building
colorama.init()

#initialise gaming constraints

game = Game()
king = King(game)

while True:
    #keep it running smoothly
    # os.system('cls' if os.name == 'nt' else 'clear')
    #print board and take input key from input file
    #put walls on board
    for wa in game.walls:
        wa.display()
    
    #PUT buildings on board
    for bu in game.buildings:
        bu.display()

    #print slower to make it smooth
    # time.sleep(T)
    board = game.print_board()
    print("\033[H\033[J", end="")
    #allow king to make move every 1 second
    key = input_to()
    #move king
    king.move(key)
    #allow king to attack wall multiple times
    king.attack_wall(key)
    king.attack_building(key)
    #check if wall is hit
    for wa in game.walls:
        if(wa.king_hit == True):
            wa.king_attack()
            if(wa.check_wall() == True):
                game.walls.remove(wa)
                game.board[wa.x][wa.y] = '|   |'
    #check if building is hit
    for bu in game.buildings:
        if(bu.king_hit == True):
            bu.king_attack()
            if(bu.check_bu() == True):
                game.buildings.remove(bu)
                for bu_co in bu.coords:
                    game.board[bu_co[0]][bu_co[1]] = '|   |'


    #update colour of wall after each attack
    #if wall is hit change colour
    #remove destroyed wall:
    # for wa in game.walls:
    #     if(wa.check_wall()):
    #         game.walls.remove(wa)
    #         game.board[wa.x][wa.y] = '|   |'


    #exit code by pressing button 'q'
    if(key == 'q'):
        sys.exit()
    # print("\033[0;0H")


