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

if __name__ == "__main__":
    main()