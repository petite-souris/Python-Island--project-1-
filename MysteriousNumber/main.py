# imports
import time

# open other files
with open("MysteriousNumber/script.txt", "r", encoding="utf-8") as script:
    lignes = script.readlines()

def main():
    # start
    for ligne in lignes:
        print(ligne)
        time.sleep(0.8)

    # ask if the user want to play
    reply = "o"
    reply = input()
    while reply == "o":
        # start the game
        from game import gameStart
        print(gameStart)
    else:
        print("D'accord, je comprends que tu n'as assez de temps pour moi. \n")
        print("Je te souhaite donc une bonne aventure moussaillon et à très vite !")

if __name__ == '__main__':
    main()