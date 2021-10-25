# Imports
import json
import random
import time

# Other files
with open("FizzBuzz/infos.json","r",encoding="utf-8") as playerInfos:
    player = json.load(playerInfos)
    playerName = player["playerName"]

with open("FizzBuzz/singes.json","r",encoding="utf-8") as singesFile:
    singes = json.load(singesFile)

# Start
fizz = "Fizz !"
buzz = "Buzz !"
fizzBuzz = "FizzBuzz !"

gameStart = True

while gameStart:
    
    listPlayers = []

    for singe in range(len(singes)):
        listPlayers.append(singes[singe]["name"])
    listPlayers.append(playerName)
    print("Dans la partie, il y a", ", ".join(listPlayers), "en tant que joueurs. \n")

    time.sleep(1.0)

    starter = random.randint(0,len(listPlayers)-1)
    print(f"Le premier joueur du jeu FizzBuzz est {listPlayers[starter]} . \n")

    gameRound = True
    countStart = 1

    time.sleep(1.0)
    print(f"Le joueur {listPlayers[starter]} commence en disant : {countStart} . \n")

    gameTurn = True
    while gameTurn:
        
        if starter >= len(listPlayers)-1:
            starter = 0
        else:
            starter += 1

        countStart += 1

        probabilityMonkey = random.randint(singes[singe]["chanceMin"],singes[singe]["chanceMax"])
        probabilityChef = random.randint(singes[0]["chanceMin"],singes[0]["chanceMax"])
        probabilityPlayer = random.randint(player["chanceMin"],player["chanceMax"])
        chance = random.randint(0,100)
        
        if len(listPlayers) > 1 :

            if listPlayers[starter] == singes[0]["name"]:
                if probabilityChef < chance:
                    print(f"Le joueur {listPlayers[starter]} a perdu ! Il n'est pas digne d'être un chef ! \n")
                    listPlayers.pop(starter)
                else:
                    if countStart%3 == 0 and countStart%5 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {fizzBuzz} \n")
                    elif countStart%3 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {fizz}\n")
                    elif countStart%5 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {buzz}\n")
                    else:
                        print(f"Le joueur {listPlayers[starter]} continue avec le nombre {countStart} . \n")

            elif listPlayers[starter] == playerName:
                if probabilityPlayer < chance:
                    print(f"Le joueur {listPlayers[starter]} a perdu ! Dommage pour toi ! Les singes se moquent de toi ! \n")
                    print(f"Tu as perdu le défi FizzBuzz ... Nous sommes navrés pour toi. ☹ \n")
                    listPlayers.pop(starter)

                    # Break when the player lose.
                    gameStart = False
                    gameTurn = False

                    print("Ce n'est pas grave, ce n'est qu'un échec aujourd'hui. Reviens demain pour savoir si les singes auront moins de chance.")

                    # New try
                    restart = input("Veux-tu retenter ta chance au FizzBuzz ? O -> Oui ; N -> Non : ").upper()
                    if restart == "O":
                        gameStart = True
                    else:
                        gameStart = False
                        print("Bonne chance à toi petite aventurier pour le reste de ton aventure !")

                else:
                    if countStart%3 == 0 and countStart%5 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {fizzBuzz} \n")
                    elif countStart%3 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {fizz} \n")
                    elif countStart%5 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {buzz} \n")
                    else:
                        print(f"Le joueur {listPlayers[starter]} continue avec le nombre {countStart} . \n")

            else:
                if probabilityMonkey < chance:
                    print(f"Le joueur {listPlayers[starter]} a perdu ! \nUn de moins, courage à toi aventurier ! 💪 \n")
                    listPlayers.pop(starter)
                else:
                    if countStart%3 == 0 and countStart%5 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {fizzBuzz} \n")
                    elif countStart%3 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {fizz} \n")
                    elif countStart%5 == 0:
                        print(f"Le joueur {listPlayers[starter]} continue avec {buzz} \n")
                    else:
                        print(f"Le joueur {listPlayers[starter]} continue avec le nombre {countStart} . \n")
                
            print("Actuellement, il reste :", ", ".join(listPlayers), "dans la partie ! Tiens le coup, tu vas y arriver ! 💪 \n")

        else:
            print("Le dernier de la partie est :", " ".join(listPlayers), "! \n")
            print(f"Le gagnant du défi FizzBuzz est donc {listPlayers[starter]} ! Félicitations à toi ! 🎉 \n")
            
            if gameStart == True:
                restart = input("Voulez-vous rejouez au FizzBuzz ? O -> Oui ; N -> Non : ").upper()
                if restart == "O":
                    gameStart = True
                else:
                    gameStart = False
                    print("Dans ce cas, je t'informe que tu as gagné le défi FizzBuzz et donc la clé d'or ! 🗝 \nLes singes s'enfuient tous en criant de désespoir dans la jungle. \nN'oublie pas de la mettre dans ton inventaire !")
                    print("Bonne chance à toi petit aventurier pour le reste de ton aventure !")
            
            # Break when the player win.
            gameStart = False
            gameTurn = False
        
        time.sleep(1.0)

