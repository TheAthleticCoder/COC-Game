# We create game constants here

#Time
FPS = 90
T = 1/FPS

#Board dimensions
ROWS_V = 25
COLS_V = 25

#King position
X_KING = 1
Y_KING = 1
HP_KING = 10
KING_ATTACK = 2


#ATTACK TIMES
BU_AT_TIME = 1
TR_AT_TIME = 1


#Default char
CHAR_DEA = '| |'

#Wall class
ROWS_W = 1
COLS_W = 1
HP_WALL = 10
CHAR_WALL = '|W|'
WALLS = [[10,10,10],[10,11,10]]
NEW_WALLS = [[[5,4]],[[2,10]]]

#Town Hall
X_TH = 11
Y_TH = 11
HP_TH = 10
CHAR_TH = u'|T|'
TH_BLOCKS = [[X_TH,Y_TH],[X_TH,Y_TH+1],[X_TH,Y_TH+2],[X_TH,Y_TH+3],[X_TH+1,Y_TH],[X_TH+1,Y_TH+1],[X_TH+1,Y_TH+2],[X_TH+1,Y_TH+3],
[X_TH+2,Y_TH],[X_TH+2,Y_TH+1],[X_TH+2,Y_TH+2],[X_TH+2,Y_TH+3]]

#coordinates of all blocks around the TH_BLOCKS
TH_BLOCKS_AROUND = [[X_TH-2,Y_TH-2,HP_WALL],[X_TH-2,Y_TH-1,HP_WALL],[X_TH-2,Y_TH,HP_WALL],[X_TH-2,Y_TH+1,HP_WALL],[X_TH-2,Y_TH+2,HP_WALL],
[X_TH-2,Y_TH+3,HP_WALL],[X_TH-2,Y_TH+4,HP_WALL],[X_TH-2,Y_TH+5,HP_WALL],[X_TH+4,Y_TH-2,HP_WALL],[X_TH+4,Y_TH-1,HP_WALL],[X_TH+4,Y_TH,HP_WALL],
[X_TH+4,Y_TH+1,HP_WALL],[X_TH+4,Y_TH+2,HP_WALL],[X_TH+4,Y_TH+3,HP_WALL],[X_TH+4,Y_TH+4,HP_WALL],[X_TH+4,Y_TH+5,HP_WALL],
[X_TH-1,Y_TH-2,HP_WALL],[X_TH,Y_TH-2,HP_WALL],[X_TH+1,Y_TH-2,HP_WALL],[X_TH+2,Y_TH-2,HP_WALL],[X_TH+3,Y_TH-2,HP_WALL],
[X_TH-1,Y_TH+5,HP_WALL],[X_TH,Y_TH+5,HP_WALL],[X_TH+1,Y_TH+5,HP_WALL],[X_TH+2,Y_TH+5,HP_WALL],[X_TH+3,Y_TH+5,HP_WALL]]

#HUT 1
X_H1 = 5
Y_H1 = 3
HP_H1 = 10
CHAR_H1 = '|H|'
H1_BLOCKS = [[X_H1,Y_H1],[X_H1, Y_H1+1]]

#HUT 2
X_H2 = 5
Y_H2 = 11
HP_H2 = 10
CHAR_H2 = '|H|'
H2_BLOCKS = [[X_H2,Y_H2],[X_H2, Y_H2+1]]

#HUT 3
X_H3 = 13
Y_H3 = 3
HP_H3 = 10
CHAR_H3 = '|H|'
H3_BLOCKS = [[X_H3,Y_H3],[X_H3, Y_H3+1]]

#Spawn locations
X_SPAWN = [ROWS_V-2,1,ROWS_V-2]
Y_SPAWN = [2,COLS_V-2,COLS_V-2]
SPAWN_POINTS = [[ROWS_V-2,2],[1,COLS_V-2],[ROWS_V-2,COLS_V-2]]

#Defender class
CHAR_C1 = '|C|'
X_C1 = 17
Y_C1 = 17
HP_C1 = 10
C1_BLOCKS = [[X_C1,Y_C1]]
C1_ATTACK = 1
C1_HEALTH = 10

CHAR_C2 = '|C|'
X_C2 = 14
Y_C2 = 6
HP_C2 = 10
C2_BLOCKS = [[X_C2,Y_C2]]
C2_ATTACK = 1
C2_HEALTH = 10


#Barbs
BARB_HP = 10
BARB_CHAR = '|B|'
BARB_ATTACK = 1

game_win = r''' 
  ________                        ________                    ._.
 /  _____/_____    _____   ____   \_____  \___  __ ___________| |
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ |
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/\|
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   __
        \/     \/      \/     \/          \/          \/       \/
_____.___.               __      __.__              ___          
\__  |   | ____  __ __  /  \    /  \__| ____    /\  \  \         
 /   |   |/  _ \|  |  \ \   \/\/   /  |/    \   \/   \  \        
 \____   (  <_> )  |  /  \        /|  |   |  \  /\    )  )       
 / ______|\____/|____/    \__/\  / |__|___|  /  \/   /  /        
 \/                            \/          \/       /__/                                                                                                                                                                          
        '''

game_lose = r''' 
                                                                                                    
                                                                                                             
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   @@@  
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  @@!  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@   
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   @!@  
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    !!!  
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!        
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  :!:  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::   ::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : :  :::  
@@@ @@@   @@@@@@   @@@  @@@     @@@        @@@@@@    @@@@@@   @@@@@@@@             @@@      
@@@ @@@  @@@@@@@@  @@@  @@@     @@@       @@@@@@@@  @@@@@@@   @@@@@@@@            @@@       
@@! !@@  @@!  @@@  @@!  @@@     @@!       @@!  @@@  !@@       @@!                @@!        
!@! @!!  !@!  @!@  !@!  @!@     !@!       !@!  @!@  !@!       !@!          @!@  !@!         
 !@!@!   @!@  !@!  @!@  !@!     @!!       @!@  !@!  !!@@!!    @!!!:!       !@!  !!@         
  @!!!   !@!  !!!  !@!  !!!     !!!       !@!  !!!   !!@!!!   !!!!!:       !:!  !!!         
  !!:    !!:  !!!  !!:  !!!     !!:       !!:  !!!       !:!  !!:               !!:         
  :!:    :!:  !:!  :!:  !:!      :!:      :!:  !:!      !:!   :!:          :!:   :!:        
   ::    ::::: ::  ::::: ::      :: ::::  ::::: ::  :::: ::    :: ::::     :::     ::       
   :      : :  :    : :  :      : :: : :   : :  :   :: : :    : :: ::      :::       :      
                                                                                                                                                                                              
        '''

#clock
clock = 0
