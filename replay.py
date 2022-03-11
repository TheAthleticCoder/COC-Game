#IMPORTING THE REQUIRED MODULES
import colorama
import sys
sys.path.insert(1, './src')
import time
from colorama import Fore, Back, Style
import json

# custom modules
from constants import *
from input import input_to
from gamecreate import *
from troops import Troop
#Initializing colorama
colorama.init()

#Initialising the game
game = Game()

#read replays.json file 
with open("./replays/replays.json", "r+") as file:
    data = json.load(file)

#choose replay number 
replay_num = int(input("Enter replay number: "))
replay_num -= 1
replay_dict = data[replay_num]

#note down game frames 
game.game_mov_frame_dict = replay_dict
game.game_start_time = time.time()

while True:
    
    #print board
    board = game.print_board()
    game.game_frames += 1
    #set key as empty string 
    key = ''

    temp_key = input_to()
    #smoother prinitng
    print("\033[H\033[J", end="")
    
    #loop to set key as a input char value based on frames
    for rep in replay_dict:
        if int(rep) == game.game_frames:
            key = replay_dict[rep]
        
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
    if(game.king != ''):
        game.king.move(key)
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

    #check for troops
    for tr in game.troops:
        if(time.time()-tr.troop_time > game.troop_move_time):
            tr.move()
            tr.troop_time = time.time()
        if tr.check_troop() == True:
            game.troops.remove(tr)
            #remove items in dictionaries whose keys are the tuple of coordinates
            tr_list = tr.coords.tolist()
            game.board[tr_list[0]][tr_list[1]] = CHAR_DEA
            
    #use spells
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
    

    
    #make it smooth
    if (key != None):
        time.sleep(T)

    #VERY IMPORTANT FOR MAKING REPLAY RUN SLOWER
    #EXTRA FEATURE REPLAY SPEED
    if temp_key == '1':
        time.sleep(0.2)
    elif temp_key == '2':
        time.sleep(0.1)
    elif temp_key == '3':
        time.sleep(0.05)

    #ending game code 
    if(len(game.buildings) == 0):
        os.system('aplay -q ./src/sounds/win.wav&')
        print(Fore.CYAN + game_win + Fore.RESET)
        break
    elif(len(game.troops) == 0 and game.king == ''):
        os.system('aplay -q ./src/sounds/lose.wav&')
        print(Fore.GREEN  + game_lose + Fore.RESET)
        break

    #exit code by pressing button 'q'
    if(key == 'q'):
        sys.exit()
    # print("\033[0;0H")


