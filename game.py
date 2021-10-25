# code utf-8

# imports
from Map.mapmain import mapmain
from MysteriousNumber.game import *
from FizzBuzz.game import *
from CaesarCode.main import *
from Player.player import *
from inventory import *
# from Menu import *
# from FinalDoor.main import *

import time
import os
import json

# other files
with open("Texts/starting.txt", "r", encoding="utf-8") as starting:
    lineS = starting.readlines()

# functions
def game():
    for line in lineS:
        print(line)
        time.sleep(1.0)
        
    print(mapmain)



if __name__ == '__main__':
    game()