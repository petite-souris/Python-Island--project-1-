# code utf-8

# imports
import time

# lecture of other files
with open("Texts/welcome.txt", "r", encoding="utf-8") as welcome:
    lineB = welcome.readlines()
with open("Texts/rules.txt", "r", encoding="utf-8") as rules:
    lineR = rules.readlines()
with open("Texts/scenario.txt", "r", encoding="utf-8") as scenario:
    lineS = scenario.readlines()
with open("Menu/optionsmenu.py", "r", encoding="utf-8") as menu:
    lineM = menu.readlines()

# functions
# text of starting
def starting():
    for line in lineB:
        print(line)
        time.sleep(1.0)

# menu
def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])

def print_play():
    print("Handle option \'Jouer\'")

def print_load():
    print("Handle option \'Charger une partie\'")

def print_rules():
    print("Handle option \'Règles\'")

if __name__ == '__main__':
    while True:
        print("Voici le menu du jeu.")
        print_menu()
        option = ''
        # reply of player
        option = int(input("Entre ton choix : "))

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        else:
            exit()
