import colorama
import time
from colorama import Fore, Back, Style

from constants import *

class Spells:
    def __init__(self, game):
        self.game = game
        self.spell_duration_time = 10
        self.spell_start_time = 0
        self.rage_activ = False

    #Assignment Requirement: Heal Spell
    def heal_spell(self):
        #increase health of all troops by 150%
        for troop in self.game.troops:
            troop.troop_health += int(troop.troop_health * 0.5)
            if troop.troop_health > troop.tot_health:
                troop.troop_health = troop.tot_health
            troop.display()
        #increase kings health
        self.game.king.health += int(self.game.king.health * 0.5)
        if self.game.king.health > HP_KING:
            self.game.king.health = HP_KING
        self.game.king.colour_change_king()

    #Assignment Requirement: Rage Spell
    def rage_spell(self):
        #increase movement speed
        self.game.troop_move_time = 0.5*TR_AT_TIME

        #increase troops attack power
        for troop in self.game.troops:
            troop.attack_given = 2*BARB_ATTACK
            troop.display()
        #increase kings attack
        self.game.king.attack = 2*KING_ATTACK
        self.game.king.colour_change_king()

    
