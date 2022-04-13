from colorama import Fore, Back, Style
import time
from constants import *

class Queen:
    def __init__(self,game):
        self.game = game
        self.x = X_QUEEN
        self.y = Y_QUEEN
        self.kill = False
        self.health = HP_QUEEN
        self.attack = 2
        self.curr_move = ''
        self.char = '|Q|'
        self.actual_char = '|Q|'
        self.health_bar = ''
        self.q_time = 0
        self.colour_change_queen()
    
    def colour_change_queen(self):
        self.char = self.actual_char
        if self.health >= HP_QUEEN*0.5:
            self.colour = Fore.GREEN
        elif self.health >= HP_QUEEN*0.2 and self.health < HP_QUEEN*0.5:
            self.colour = Fore.YELLOW
        elif self.health < HP_QUEEN*0.2:
            self.colour = Fore.RED
        self.char = self.colour + self.char + Fore.RESET 
        self.game.board[self.x][self.y] = self.char

    def move(self,key):
        self.game.board[self.x][self.y] = CHAR_DEA
        if(key == 'w'):
            self.curr_move = 'w'
            if(self.x > 0 and self.game.board[self.x-1][self.y] == CHAR_DEA):
                self.x -= 1
        elif(key == 's'):
            self.curr_move = 's'
            if(self.x < ROWS_V - 1 and self.game.board[self.x+1][self.y] == CHAR_DEA):
                self.x += 1
        elif(key == 'a'):
            self.curr_move = 'a'
            if(self.y > 0 and self.game.board[self.x][self.y-1] == CHAR_DEA):
                self.y -= 1
        elif(key == 'd'):
            self.curr_move = 'd'
            if(self.y < COLS_V - 1 and self.game.board[self.x][self.y+1] == CHAR_DEA):
                self.y += 1
        self.colour_change_queen()
    
    def Queen_attack(self,key):
        if key == ' ':
            if self.curr_move == 'w':
                for building in self.game.buildings:
                    for build in building.coords:
                        if (build[0] >= self.x-6 and build[0] <=self.x-10) and (build[1] >= self.y-2 and build[1] <=self.y+2):
                            building.bu_health -= self.attack
                            building.display()
                            break
                for wall in self.game.walls:
                    if(wall.x >= self.x-6 and wall.x <=self.x-10) and (wall.y >= self.y-2 and wall.y <=self.y+2):
                        wall.wall_health -= self.attack
                        wall.display()
                        
            elif self.curr_move == 's': 
                for building in self.game.buildings:
                    for build in building.coords:
                        if (build[0] >= self.x+6 and build[0] <=self.x+10) and (build[1] >= self.y-2 and build[1] <=self.y+2):
                            building.bu_health -= self.attack
                            building.display()
                            break
                for wall in self.game.walls:
                    if(wall.x >= self.x+6 and wall.x <=self.x+10) and (wall.y >= self.y-2 and wall.y <=self.y+2):
                        wall.wall_health -= self.attack
                        wall.display()
            elif self.curr_move == 'a':
                for building in self.game.buildings:
                    for build in building.coords:
                        if (build[0] >= self.x-2 and build[0] <=self.x+2) and (build[1] >= self.y-6 and build[1] <=self.y-10):
                            building.bu_health -= self.attack
                            building.display()
                            break
                for wall in self.game.walls:
                    if(wall.x >= self.x-2 and wall.x <=self.x+2) and (wall.y >= self.y-6 and wall.y <=self.y-10):
                        wall.wall_health -= self.attack
                        wall.display()

            elif self.curr_move == 'd':
                for building in self.game.buildings:
                    for build in building.coords:
                        if (build[0] >= self.x-2 and build[0] <=self.x+2) and (build[1] >= self.y+6 and build[1] <=self.y+10):
                            building.bu_health -= self.attack
                            building.display()
                            break
                for wall in self.game.walls:
                    if(wall.x >= self.x-2 and wall.x <=self.x+2) and (wall.y >= self.y+6 and wall.y <=self.y+10):
                        wall.wall_health -= self.attack
                        wall.display()
        if key == 'x':
            self.game.queen_state = True
            self.q_time = time.time()


    def spec_queen_ult(self):
        if self.curr_move == 'w':
            for building in self.game.buildings:
                for build in building.coords:
                    if (build[0] >= self.x-12 and build[0] <=self.x-20) and (build[1] >= self.y-4 and build[1] <=self.y+4):
                        building.bu_health -= self.attack
                        building.display()
                        break
            for wall in self.game.walls:
                if(wall.x >= self.x-12 and wall.x <=self.x-20) and (wall.y >= self.y-4 and wall.y <=self.y+4):
                    wall.wall_health -= self.attack
                    wall.display()
                    
        elif self.curr_move == 's': 
            for building in self.game.buildings:
                for build in building.coords:
                    if (build[0] >= self.x+12 and build[0] <=self.x+20) and (build[1] >= self.y-4 and build[1] <=self.y+4):
                        building.bu_health -= self.attack
                        building.display()
                        break
            for wall in self.game.walls:
                if(wall.x >= self.x+12 and wall.x <=self.x+20) and (wall.y >= self.y-4 and wall.y <=self.y+4):
                    wall.wall_health -= self.attack
                    wall.display()
        elif self.curr_move == 'a':
            for building in self.game.buildings:
                for build in building.coords:
                    if (build[0] >= self.x-4 and build[0] <=self.x+4) and (build[1] >= self.y-12 and build[1] <=self.y-20):
                        building.bu_health -= self.attack
                        building.display()
                        break
            for wall in self.game.walls:
                if(wall.x >= self.x-4 and wall.x <=self.x+4) and (wall.y >= self.y-12 and wall.y <=self.y-20):
                    wall.wall_health -= self.attack
                    wall.display()

        elif self.curr_move == 'd':
            for building in self.game.buildings:
                for build in building.coords:
                    if (build[0] >= self.x-4 and build[0] <=self.x+4) and (build[1] >= self.y+12 and build[1] <=self.y+20):
                        building.bu_health -= self.attack
                        building.display()
                        break
            for wall in self.game.walls:
                if(wall.x >= self.x-4 and wall.x <=self.x+4) and (wall.y >= self.y+12 and wall.y <=self.y+20):
                    wall.wall_health -= self.attack
                    wall.display()

    def health_bar_calc(self):
        self.health_bar = ''
        temp = int(self.health/2)
        self.health_bar = '|'
        for i in range(temp):
            self.health_bar += '██'
        for i in range(int(HP_QUEEN/2) - temp):
            self.health_bar += '░░'
        self.health_bar += '|'
        self.health_bar = self.colour + self.health_bar  + Fore.RESET
        return self.health_bar

    def check_queen(self):
        if(self.health <= 0):
            return True
        #move queen up-left
        