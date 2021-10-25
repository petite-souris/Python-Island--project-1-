import time

# Open files in other files
with open("FizzBuzz/script.txt", "r", encoding="utf-8") as script:
    for ligne in script:
        print(ligne)
        time.sleep(1.0)

# Question about the quest
print("\nVeux-tu tenter ce défi pour obtenir la clé d'or nécessaire à l'ouverture de la porte finale ?")
    
reply = input()
while reply == False:
    print("Je comprends. Je te souhaite alors une bonne aventure à toi petit aventurier ! A très vite !")
else:
    time.sleep(1.5)
    from game import gameStart
    print(gameStart)
    
# Retour au menu principal.