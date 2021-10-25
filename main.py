# code UTF-8

# Imports
import time

# Lecture of other files
with open("Textes/bienvenue.txt", "r", encoding="utf-8") as bienvenue:
    ligneB = bienvenue.readlines()
with open("Textes/regles.txt", "r", encoding="utf-8") as regles:
    ligneR = regles.readlines()
with open("Textes/scenario.txt", "r", encoding="utf-8") as scenario:
    ligneS = scenario.readlines()

# starting
def main():

    # text of starting
    for ligne in ligneB:
        print(ligne)
        time.sleep(1.0)

    # rules of the game
    print("Avant de commencer le jeu, veux-tu d'abord lire les règles ?")
    reply = "o"
    # ask a reply
    reply = input()
    if reply == "o":
        for ligne in ligneR:
            print(ligne)
            time.sleep(1.0)
        print("\nMaintenant que les règles ont été énumérées, voici le début de l'histoire !\n")
        for ligne in ligneS:
            print(ligne)
            time.sleep(1.0)
    else:
        # scenario
        for ligne in ligneS:
            print(ligne)
            time.sleep(1.0)
    
    # start game
    print("\nEs-tu prêt pour l'aventure petit aventurier ?\n")
    reply = "o"
    #ask to user a reply
    reply = input()
    if reply == "o":
        # start game
        pass
    else:
        # really sure ? Save ? Bye
        pass

if __name__ == "__main__":
    main()