import time
import colorama
from colorama import Fore, Back, Style

from constants import *

class King:
    def __init__(self,game):
        self.game = game
        self.x = X_KING
        self.y = Y_KING
        # self.coords = [(self.x,self.y)]
        self.kill = False
        self.health = HP_KING
        self.attack = 2
        self.curr_move = ''
        self.char = '|K|'
        self.actual_char = '|K|'
        self.health_bar = ''
        self.colour_change_king()
        # self.health_bar()
    
    def colour_change_king(self):
        self.char = self.actual_char
        if self.health >= HP_KING*0.5:
            self.colour = Fore.GREEN
        elif self.health >= HP_KING*0.2 and self.health < HP_KING*0.5:
            self.colour = Fore.YELLOW
        elif self.health < HP_KING*0.2:
            self.colour = Fore.RED
        self.char = self.colour + self.char + Fore.RESET 
        self.game.board[self.x][self.y] = self.char


    def health_bar_calc(self):
        self.health_bar = ''
        temp = int(self.health/5)
        self.health_bar = '|'
        for i in range(temp):
            self.health_bar += '■■'
        for i in range(int(HP_KING/5) - temp):
            self.health_bar += ' '
        self.health_bar += '|'
        self.health_bar = self.colour + self.health_bar  + Fore.RESET
        return self.health_bar

    #move king on the board
    def move(self,key):
        #change king position on board
        self.game.board[self.x][self.y] = CHAR_DEA
        # self.game.king_note = Fore.GREEN + '| K |' + Fore.RESET
        #move king up
        if(key == 'w'):
            self.curr_move = 'w'
            if(self.x > 0 and self.game.board[self.x-1][self.y] == CHAR_DEA):
                self.x -= 1
        #move king down
        elif(key == 's'):
            self.curr_move = 's'
            if(self.x < ROWS_V - 1 and self.game.board[self.x+1][self.y] == CHAR_DEA):
                self.x += 1
        #move king left
        elif(key == 'a'):
            self.curr_move = 'a'
            if(self.y > 0 and self.game.board[self.x][self.y-1] == CHAR_DEA):
                self.y -= 1
        #move king right
        elif(key == 'd'):
            self.curr_move = 'd'
            if(self.y < COLS_V - 1 and self.game.board[self.x][self.y+1] == CHAR_DEA):
                self.y += 1
        self.colour_change_king()
        # self.game.print_board()

    #function to attack a building
    def attack_building(self,key):
        if key == ' ':
            if(self.curr_move == 'w'):
                for building in self.game.buildings:
                    for build in building.coords:
                        if(build[0] == self.x-1 and build[1] == self.y):
                            building.bu_health -= self.attack
                            building.display()
                            #update values in game.buildings
                        #update values in game.walls
            elif(self.curr_move == 's'):
                for building in self.game.buildings:
                    for build in building.coords:
                        if(build[0] == self.x+1 and build[1] == self.y):
                            building.bu_health -= self.attack
                            building.display()
                            #update values in game.buildings
                        #update values in game.walls
            elif(self.curr_move == 'a'):
                for building in self.game.buildings:
                    for build in building.coords:
                        if(build[0] == self.x and build[1] == self.y-1):
                            building.bu_health -= self.attack
                            building.display()
                            #update values in game.buildings
                        #update values in game.walls
            elif(self.curr_move == 'd'):
                for building in self.game.buildings:
                    for build in building.coords:
                        if(build[0] == self.x and build[1] == self.y+1):
                            building.bu_health -= self.attack
                            building.display()
                            #update values in game.buildings
                        #update values in game.walls
        # return


    def attack_wall(self,key):
        if key == ' ':
            if(self.curr_move == 'w'):
                #give attack damage to wall at location
                for wall in self.game.walls:
                    if(wall.x == self.x-1 and wall.y == self.y):
                        wall.wall_health -= self.attack
                        wall.display()
                        #update values in game.walls
            elif(self.curr_move == 's'):
                #give attack damage to wall at location
                for wall in self.game.walls:
                    if(wall.x == self.x+1 and wall.y == self.y):
                        wall.wall_health -= self.attack
                        wall.display()
            elif(self.curr_move == 'a'):
                #give attack damage to wall at location
                for wall in self.game.walls:
                    if(wall.x == self.x and wall.y == self.y-1):
                        wall.wall_health -= self.attack
                        wall.display()
            elif(self.curr_move == 'd'):
                #give attack damage to wall at location
                for wall in self.game.walls:
                    if(wall.x == self.x and wall.y == self.y+1):
                        wall.wall_health -= self.attack
                        wall.display()
        # return 

    #function to check if king is dead
    def check_king(self):
        if(self.health <= 0):
            return True

        
        
    
    
        


