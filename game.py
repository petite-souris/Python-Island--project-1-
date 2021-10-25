# code utf-8

# imports
from Map import mapmain
import time

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