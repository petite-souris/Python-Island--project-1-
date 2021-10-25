# code utf-8 

# imports
import random
import time

gameStart = True

while gameStart:
    # initializing no. of guess to 0
    guess_count = 0

    # repetition of the development three times
    for loop in range(1):

        # generating random number
        random_number = random.randint(1, 100)

        # running loop until user guess the random number
        while True:
            # getting user input

            user_guessed_number = int(input("Choisis un nombre entre 0 et 100 : \n"))

            # checking for the equality
            if user_guessed_number == random_number:
                print(f"Félicitations ! Tu as trouvé le numéro mystère en {guess_count} essais. \n")
                # breaking the loop
                break
            elif user_guessed_number < random_number:
                print("Le nombre que j'ai en tête est plus grand. \n")
            elif user_guessed_number > random_number:
                print("Le nombre que j'ai en tête est plus petit. \n")

            # incrementing the guess count
            guess_count += 1
        
        # time to make clear
        time.sleep(1.0)

    # felicitations when the user find the three mysterious number
    if guess_count <= 20:
        print("Félicitations, tu as trouvé tous les nombres mystères !")
        print(f"Tu as trouvé tous les nombres avec un total de {guess_count} essais !")
        print("Pour te remercier d'avoir pris le temps de jouer avec moi, je t'offre cette clé de bronze. ")

        # try again ?
        if gameStart == False:
            reply = input("Veux-tu rejouer avec moi ? O -> Oui ; N -> Non : ").upper()
            if reply == "o":
                gameStart = True
            else:
                gameStart = False
                print("Dans ce cas, je t'informe que tu as gagné le défi Nombre Mystère et donc la clé de bronze ! 🗝 \nN'oublie pas de la mettre dans ton inventaire !")
                print("Bonne chance à toi petit aventurier pour le reste de ton aventure !")
    else:
        print("Félicitations, tu as trouvé tous les nombres mystères !\n")
        print("Malheureusement, tu as dépassé les 20 essais que tu avais. \n")
        print("De ce fait, tu as perdu ce défi. Je suis désolé pour toi. \n")

        # try again ?
        if gameStart == False:
            reply = input("Veux-tu rejouer avec moi ? O -> Oui ; N -> Non : ").upper()
            if reply == "o":
                gameStart = True
            else:
                gameStart = False
                print("Dans ce cas, je t'informe que tu as gagné le défi Nombre Mystère et donc la clé de bronze ! 🗝 \nN'oublie pas de la mettre dans ton inventaire !")
                print("Bonne chance à toi petit aventurier pour le reste de ton aventure !")