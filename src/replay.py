import colorama
import sys
import time
from colorama import Fore, Back, Style
import json

# custom modules
from constants import *
from input import input_to
from king import King
from gamecreate import *
from walls import Wall
from buildings import Building
from troops import Troop
from spells import Spells
colorama.init()

#initialise gaming constraints
game = Game()

#read json file
with open("replays.json", "r+") as file:
    data = json.load(file)

#choose replay
replay_num = int(input("Enter replay number: "))
replay_num -= 1
replay_dict = data[replay_num]
#note down game start time
game.game_mov_frame_dict = replay_dict
game.game_start_time = time.time()
# king = King(game)

while True:
    #keep it running smoothly
    # os.system('cls' if os.name == 'nt' else 'clear')
    #print board and take input key from input file
    board = game.print_board()
    game.game_frames += 1
    key = ''

    
    print("\033[H\033[J", end="")
    #allow king to make move every 1 second


    # key = input_to()
    for rep in replay_dict:
        if int(rep) == game.game_frames:
            key = replay_dict[rep]
        
    # if key != None:
    #     game.game_mov_tim_dict[time.time() - game.game_start_time] = key

    #deploy troops based on spawn points
    start_time = time.time()
    game.start_time = start_time
    if (key == 'c'):
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[0]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        # game.troop_list.append([SPAWN_POINTS[0][0],SPAWN_POINTS[0][1],Troop(game,np.array(SPAWN_POINTS[0]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])
    elif (key == 'v'):
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[1]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        # game.troop_list.append([SPAWN_POINTS[1][0],SPAWN_POINTS[1][1],Troop(game,np.array(SPAWN_POINTS[1]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])
    elif (key == 'b'):
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[2]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        # game.troop_list.append([SPAWN_POINTS[2][0],SPAWN_POINTS[2][1],Troop(game,np.array(SPAWN_POINTS[2]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])

    #move king
    #if king exists, dp:
    if(game.king != ''):
        game.king.move(key)
        #allow king to attack wall multiple times
        # game.king.attack_wall(key)
        game.king.King_attack(key)
        if(game.king.check_king() == True):
            game.board[game.king.x][game.king.y] = CHAR_DEA
            game.king = ''

    #check if wall is hit
    for wa in game.walls:
        if(wa.check_wall() == True):
            game.walls.remove(wa)
            game.board[wa.x][wa.y] = CHAR_DEA
            del game.wall_dict[(wa.x,wa.y)]
    #check if building is hit
    for bu in game.buildings:
        if(bu.check_bu() == True):
            game.buildings.remove(bu)
            #remove items in dictionaries whose keys are the tuple of coordinates
            for bu_co in bu.coords:
                game.board[bu_co[0]][bu_co[1]] = CHAR_DEA
                del game.build_dict[tuple(bu_co)]
        if(time.time()-bu.building_time > game.build_att_time):
            bu.bu_attack()
            bu.building_time = time.time()

    for tr in game.troops:
        if(time.time()-tr.troop_time > game.troop_move_time):
            tr.move()
            tr.troop_time = time.time()
        if tr.check_troop() == True:
            game.troops.remove(tr)
            #remove items in dictionaries whose keys are the tuple of coordinates
            tr_list = tr.coords.tolist()
            game.board[tr_list[0]][tr_list[1]] = CHAR_DEA
                # del game.troops[tuple(tr_co)]
        #check if troop is hit

    if (key == 'h'):
        #call heal spell
        game.spell.heal_spell()
    elif (key == 'r'):
        game.spell.spell_start_time = time.time()
        game.spell.rage_active = True
        #make rage spell last for 10 seconds
    
    if (game.spell.spell_start_time != 0) and game.spell.rage_active == True:
        if (time.time()-game.spell.spell_start_time < game.spell.spell_duration_time):
            game.spell.rage_spell()
        else:
            game.spell.rage_active = False
            game.spell.spell_start_time = 0
            game.troop_move_time = TR_AT_TIME
            for troop in game.troops:
                troop.attack_given = BARB_ATTACK
                troop.display()
        #increase kings attack
            game.king.attack = KING_ATTACK
            game.king.colour_change_king()
    

    #if king exists, print its health

    if (key != None):
        time.sleep(T)

    time.sleep(0.1)
    #if building list is empty, end game
    if(len(game.buildings) == 0):
        #append dictionary to json file
        print(Fore.CYAN + game_win + Fore.RESET)
        break
    elif(len(game.troops) == 0 and game.king == ''):
        print(Fore.GREEN  + game_lose + Fore.RESET)
        break

    #exit code by pressing button 'q'
    if(key == 'q'):
        sys.exit()
    # print("\033[0;0H")


