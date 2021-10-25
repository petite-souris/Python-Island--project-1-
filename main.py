# code UTF-8

# Imports
import time

# Lecture of other files
with open("Textes/bienvenue.txt", "r", encoding="utf-8") as bienvenue:
    ligneB = bienvenue.readlines()

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
    else:
        pass

if __name__ == "__main__":
    main()