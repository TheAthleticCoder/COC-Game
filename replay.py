#IMPORTING THE REQUIRED MODULES
import colorama
import sys
sys.path.insert(1, './src')
import time
from colorama import Fore, Back, Style
import json

# custom modules
from src.constants import *
from src.input import input_to
from src.gamecreate import *
from src.troops import Troop
#Initializing colorama
colorama.init()

#Initialising the game
level = 1
# val = input("Enter 'k' for a King and 'q' for a Queen: ")
with open("./replays/r_hero.json", "r+") as file:
    h_data = json.load(file)

#read replays.json file 
with open("./replays/replays.json", "r+") as file:
    data = json.load(file)

#choose replay number 
replay_num = int(input("Enter replay number: "))
replay_num -= 1
val = h_data[replay_num]
game = Game(val,level)
replay_dict = data[replay_num]

#note down game frames 
game.game_mov_frame_dict = replay_dict
game.game_start_time = time.time()
replay_speed = 0.2

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
    if (key == 'c') and game.barb_count < MAX_BARB_COUNT:
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[0]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        game.barb_count += 1
        # game.troop_list.append([SPAWN_POINTS[0][0],SPAWN_POINTS[0][1],Troop(game,np.array(SPAWN_POINTS[0]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])
    elif (key == 'v') and game.barb_count < MAX_BARB_COUNT:
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[1]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        game.barb_count += 1
        # game.troop_list.append([SPAWN_POINTS[1][0],SPAWN_POINTS[1][1],Troop(game,np.array(SPAWN_POINTS[1]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])
    elif (key == 'b') and game.barb_count < MAX_BARB_COUNT:
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[2]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        game.barb_count += 1
        # game.troop_list.append([SPAWN_POINTS[2][0],SPAWN_POINTS[2][1],Troop(game,np.array(SPAWN_POINTS[2]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])
    elif (key == 'g') and game.arch_count < MAX_ARCH_COUNT:
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[0]),ARCH_HP,ARCH_CHAR ,ARCH_ATTACK,ARCH_HP,start_time))
        game.arch_count += 1
    elif(key == 'j') and game.arch_count < MAX_ARCH_COUNT:
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[1]),ARCH_HP,ARCH_CHAR ,ARCH_ATTACK,ARCH_HP,start_time))
        game.arch_count += 1
    elif(key == 'k') and game.arch_count < MAX_ARCH_COUNT:
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[2]),ARCH_HP,ARCH_CHAR ,ARCH_ATTACK,ARCH_HP,start_time))
        game.arch_count += 1
    elif(key == 'y') and game.ball_count < MAX_BALLOON_COUNT:
        game.aerial_troops.append(Troop(game,np.array(SPAWN_POINTS[0]),BALLOON_HP,BALLOON_CHAR ,BALLOON_ATTACK,BALLOON_HP,start_time))
        game.ball_count += 1
    elif(key == 'u') and game.ball_count < MAX_BALLOON_COUNT:
        game.aerial_troops.append(Troop(game,np.array(SPAWN_POINTS[1]),BALLOON_HP,BALLOON_CHAR ,BALLOON_ATTACK,BALLOON_HP,start_time))
        game.ball_count += 1
    elif(key == 'i') and game.ball_count < MAX_BALLOON_COUNT:
        game.aerial_troops.append(Troop(game,np.array(SPAWN_POINTS[2]),BALLOON_HP,BALLOON_CHAR ,BALLOON_ATTACK,BALLOON_HP,start_time))
        game.ball_count += 1

    #move king
    if(game.king != ''):
        game.king.move(key)
        #allow king to attack wall multiple times
        # game.king.attack_wall(key)
        game.king.King_attack(key)
        if(game.king.check_king() == True):
            game.board[game.king.x][game.king.y] = CHAR_DEA
            game.king = ''

    if(game.queen != ''):
        game.queen.move(key)
        # # game.queen.attack_wall(key)
        game.queen.Queen_attack(key)

        if(game.queen_state == True):
            if(time.time()-game.queen.q_time >= 1):
                game.queen.spec_queen_ult()
                game.queen_state = False

        # if (key == 'x'):
        #     if(time.time()-game.queen.q_time >= 5):
        #         game.queen.spec_queen_attack()
        #         game.queen.q_time = time.time()

        if(game.queen.check_queen() == True):
            game.board[game.queen.x][game.queen.y] = CHAR_DEA
            game.queen = ''

    #check if wall is hit
    for wa in game.walls:
        if(wa.check_wall() == True):
            game.walls.remove(wa)
            game.board[wa.x][wa.y] = CHAR_DEA
            game.algo_arr[wa.x][wa.y] = 0
            del game.wall_dict[(wa.x,wa.y)]
    #check if building is hit
    for bu in game.buildings:
        if(bu.check_bu() == True):
            game.buildings.remove(bu)
            bu.display()
            if bu.attack_mode == True:
                for bu_co in bu.coords:
                    del game.new_build_dict[tuple(bu_co)]
            #remove items in dictionaries whose keys are the tuple of coordinates
            for bu_co in bu.coords:
                game.algo_arr[bu_co[0]][bu_co[1]] = 0
                game.board[bu_co[0]][bu_co[1]] = CHAR_DEA
                del game.build_dict[tuple(bu_co)]
        else:
            bu.display()
        #code to make the building attack periodically
        if(time.time()-bu.building_time > game.build_att_time):
            if bu.actual_char == '|C|':
                bu.bu_attack()
            elif bu.actual_char == '|Z|':
                bu.bu_aerial_attack()
            bu.building_time = time.time()

    #check for troops
    for tr in (game.troops+game.aerial_troops):
        #move troop and attack buldings or walls in a time bound fashion
        if tr.actual_char == '|O|':
            game.troop_att_time = TR_AT_TIME_BALLOON
            if(time.time()-tr.troop_time > game.troop_att_time):
                tr.balloon_move()
                tr.troop_time = time.time()
        if tr.actual_char == '|A|':
            game.troop_att_time = TR_AT_TIME_ARCH
            if(time.time()-tr.troop_time > game.troop_att_time):
                tr.archer_move()
                tr.troop_time = time.time()
        if tr.actual_char == '|B|':
            game.troop_att_time = TR_AT_TIME_BARB
            if(time.time()-tr.troop_time > game.troop_att_time):
                tr.barb_move()
                tr.troop_time = time.time()

        if tr.check_troop() == True:
            if tr.actual_char == '|O|':
                game.aerial_troops.remove(tr)
            else:
                game.troops.remove(tr)
            #remove items in dictionaries whose keys are the tuple of coordinates
            tr_list = tr.coords.tolist()
            game.board[tr_list[0]][tr_list[1]] = CHAR_DEA
            
    #use spells
    if (key == 'h'):
        #call heal spell
        os.system('aplay -q ./src/sounds/heal.wav&')
        game.spell.heal_spell()
    elif (key == 'r'):
        os.system('aplay -q ./src/sounds/rage.wav&')
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
            # game.king.attack = KING_ATTACK
            # game.king.colour_change_king()

    #extra code to make game smooth
    if (key != None):
        time.sleep(T)

    #VERY IMPORTANT FOR MAKING REPLAY RUN SLOWER
    #EXTRA FEATURE REPLAY SPEED
    if temp_key == '1':
        replay_speed = 0.2
    elif temp_key == '2':
        replay_speed = 0.1
    elif temp_key == '3':
        replay_speed = 0.05

    time.sleep(replay_speed)
    #ending game code 
    # if(len(game.buildings) == 0):
    #     os.system('aplay -q ./src/sounds/win.wav&')
    #     print(Fore.CYAN + game_win + Fore.RESET)
    #     break
    # elif(len(game.troops) == 0 and game.king == ''):
    #     os.system('aplay -q ./src/sounds/lose.wav&')
    #     print(Fore.GREEN  + game_lose + Fore.RESET)
    #     break

    # #exit code by pressing button 'q'
    # if(key == 'q'):
    #     sys.exit()
    # # print("\033[0;0H")


    if(len(game.buildings) == 0):
        if level == 3:
            os.system('aplay -q ./src/sounds/win.wav&')
            print(Fore.CYAN + game_win + Fore.RESET)
            break
        else: 
            level += 1
            game = Game(val,level)
        #append dictionary to json file
        #save moves into replays json folder
        # with open('./replays/replays.json', 'r') as fp:
        #     data = json.load(fp)
        # data.append(game.game_mov_frame_dict)
        # with open('./replays/replays.json', 'w') as fp:
        #     json.dump(data, fp)
        # os.system('aplay -q ./src/sounds/win.wav&')
        # print(Fore.CYAN + game_win + Fore.RESET)
        # break
    #if troops and king are dead, end game, you lose
    elif(len(game.troops) == 0 and game.king == '' and game.queen == ''):
        #append dictionary to json file
        #save moves into replays json folder
        os.system('aplay -q ./src/sounds/lose.wav&')
        print(Fore.GREEN  + game_lose + Fore.RESET)
        break

    #exit code by pressing button 'q'
    if(key == 'q'):
        sys.exit()


