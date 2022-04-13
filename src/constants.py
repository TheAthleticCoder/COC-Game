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

#Queen position
X_QUEEN = 1
Y_QUEEN = 1
HP_QUEEN = 10
QUEEN_ATTACK = 1

#ATTACK TIMES
TR_AT_TIME = 0.5
BU_AT_TIME = 1
TR_AT_TIME_BARB = 1
TR_AT_TIME_ARCH = 0.5
TR_AT_TIME_BALLOON = 0.5


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
X_H1 = 6
Y_H1 = 6
HP_H1 = 10
CHAR_H1 = '|H|'
H1_BLOCKS = [[X_H1,Y_H1],[X_H1, Y_H1+1],[X_H1+1,Y_H1],[X_H1+1,Y_H1+1]]

#HUT 2
X_H2 = 6
Y_H2 = 18
HP_H2 = 10
CHAR_H2 = '|H|'
H2_BLOCKS = [[X_H2,Y_H2],[X_H2, Y_H2+1],[X_H2+1,Y_H2],[X_H2+1,Y_H2+1]]

#HUT 3
X_H3 = 12
Y_H3 = 6
HP_H3 = 10
CHAR_H3 = '|H|'
H3_BLOCKS = [[X_H3,Y_H3],[X_H3, Y_H3+1],[X_H3+1,Y_H3],[X_H3+1,Y_H3+1]]

#HUT 4
X_H4 = 18
Y_H4 = 12
HP_H4 = 10
CHAR_H4 = '|H|'
H4_BLOCKS = [[X_H4,Y_H4],[X_H4, Y_H4+1],[X_H4+1, Y_H4],[X_H4+1, Y_H4+1]]

#HUT 5
X_H5 = 12
Y_H5 = 18
HP_H5 = 10
CHAR_H5 = '|H|'
H5_BLOCKS = [[X_H5,Y_H5],[X_H5, Y_H5+1],[X_H5+1,Y_H5],[X_H5+1,Y_H5+1]]

#Spawn locations
X_SPAWN = [ROWS_V-2,1,ROWS_V-2]
Y_SPAWN = [2,COLS_V-2,COLS_V-2]
SPAWN_POINTS = [[ROWS_V-2,2],[1,COLS_V-2],[ROWS_V-2,COLS_V-2]]

#Defender class
CHAR_C1 = '|C|'
X_C1 = 16
Y_C1 = 17
HP_C1 = 10
C1_BLOCKS = [[X_C1,Y_C1]]
C1_ATTACK = 1
C1_HEALTH = 10

CHAR_C2 = '|C|'
X_C2 = 16
Y_C2 = 8
HP_C2 = 10
C2_BLOCKS = [[X_C2,Y_C2]]
C2_ATTACK = 1
C2_HEALTH = 10

CHAR_C3 = '|C|'
X_C3 = 8
Y_C3 = 17
HP_C3 = 10
C3_BLOCKS = [[X_C3,Y_C3]]
C3_ATTACK = 1
C3_HEALTH = 10

CHAR_C4 = '|C|'
X_C4 = 8
Y_C4 = 8
HP_C4 = 10
C4_BLOCKS = [[X_C4,Y_C4]]
C4_ATTACK = 1
C4_HEALTH = 10

#Wizard class
CHAR_W1 = '|Z|'
X_W1 = 17
Y_W1 = 18
HP_W1 = 10
W1_BLOCKS = [[X_W1,Y_W1]]
W1_ATTACK = 1
W1_HEALTH = 10

#Wizard class
CHAR_W2 = '|Z|'
X_W2 = 17
Y_W2 = 7
HP_W2 = 10
W2_BLOCKS = [[X_W2,Y_W2]]
W2_ATTACK = 1
W2_HEALTH = 10


#Wizard class
CHAR_W3 = '|Z|'
X_W3 = 8
Y_W3 = 16
HP_W3 = 10
W3_BLOCKS = [[X_W3,Y_W3]]
W3_ATTACK = 1
W3_HEALTH = 10

#Wizard class
CHAR_W4 = '|Z|'
X_W4 = 8
Y_W4 = 7
HP_W4 = 10
W4_BLOCKS = [[X_W4,Y_W4]]
W4_ATTACK = 1
W4_HEALTH = 10

#Barbs
BARB_HP = 10
BARB_CHAR = '|B|'
BARB_ATTACK = 2
MAX_BARB_COUNT = 6

#Archers
ARCH_HP = 5
ARCH_CHAR = '|A|'
ARCH_ATTACK = 1
MAX_ARCH_COUNT = 6

#Balloons
BALLOON_HP = 10
BALLOON_CHAR = '|O|'
BALLOON_ATTACK = 4
MAX_BALLOON_COUNT = 3

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
