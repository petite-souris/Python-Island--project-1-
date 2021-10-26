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
def starting():                     # text of starting
    for line in lineB:
        print(line)
        time.sleep(1.0)

def print_menu():                   # menu
    for line in lineM:
        print(line)
        
def print_play():                   # option play
    print("Handle option \'Jouer\'")

def print_load():                   # option load
    print("Handle option \'Charger une partie\'")

def print_rules():                  # option rules
    for line in lineR:
        print(line)
        time.sleep(2.0)

if __name__ == '__main__':
    while True:
        starting()

        print("Voici le menu du jeu.\n")
        time.sleep(1.0)
        print_menu()

        option = ''
        option = int(input("Entre ton choix : "))                  # reply of player

        if option == 1:
            # new player
            print("Es-tu un nouveau joueur ? \n")
            reply = input()

            if reply != 'o' or reply != 'oui' or reply != 'O' or reply != 'OUI':
                new_player = input("Quel est ton nom cher aventurier ? \n")
                print(f"Bienvenue à toi {new_player} ! \n")

                # rules for new player
                print("Veux-tu les règles du jeu avant de commencer ? \n")
                reply = "o"
                reply = input()

                if reply == "o":
                    # scenario
                    for line in lineS:
                        print(line)
                        time.sleep(1.0)
                else:
                    pass
                    
            else:
                # scenario
                for line in lineS:
                    print(line)
                    time.sleep(1.0)

                # game

        elif option == 2:
            pass

        elif option == 3:
            print_rules()

            # game
            print("Maintenant que les règles ont été développées, veux-tu commencer le jeu ?")
            reply = "o"
            reply = input()

            if reply == "o":
                # scenario
                for line in lineS:
                    print(line)
                    time.sleep(1.0)

                # game
            else:
                # return menu
                print("Voici le menu du jeu : ")
                print_menu()

        else:
            exit()
