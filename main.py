# code UTF-8

# Imports
import time

# Lecture of other files
with open("Textes/bienvenue.txt", "r", encoding="utf-8") as bienvenue:
    ligneB = bienvenue.readlines()
with open("Textes/regles.txt", "r", encoding="utf-8") as regles:
    ligneR = regles.readlines()

# starting
def main():

    # text of starting
    for ligne in ligneB:
        print(ligne)
        time.sleep(1.0)

    # new player
    print("Es-tu un nouveau joueur ? \n")
    reply = input()
    if reply != 'o' or reply != 'oui' or reply != 'O' or reply != 'OUI':
        input("Quel est ton nom cher aventurier ? \n")

        # rules of the game
        print("Avant de commencer le jeu, veux-tu d'abord lire les règles ?")
        reply = "o"
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

    else:
        # load a save
        pass

if __name__ == "__main__":
    main()