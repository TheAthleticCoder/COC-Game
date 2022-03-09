import colorama
import time
from colorama import Fore, Back, Style

from constants import *

class Spells:
    def __innit__(self, game):
        self.game = game
        self.spell_duration_time = 10
        self.spell_start_time = 0