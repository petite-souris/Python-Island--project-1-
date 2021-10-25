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

# text of starting
    for line in lineB:
        print(line)
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
            for line in lineR:
                print(line)
                time.sleep(2.0)
            print("\nMaintenant que les règles ont été énumérées, voici le début de l'histoire !\n")
            for line in lineS:
                print(line)
                time.sleep(1.0)
        else:
            # scenario
            for line in lineS:
                print(line)
                time.sleep(1.0)

        # start game
        print("\nEs-tu prêt pour l'aventure petit aventurier ?\n")
        reply = "o"
        reply = input()
        if reply == "o":
            # start game
            print(game)
        else:
            # really sure ? Save ? Bye
            pass

    else:
        # load a save and play
        pas