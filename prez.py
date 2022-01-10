from time import sleep
from options.joueur import *



def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('Handle option \'Jouer\'')
     

def option2():
     print('Handle option \'Charger une partie\'')

def option3():
     print('Handle option \'Regle\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('entrez un nombre de 1 à 4')
        #Check what choice was entered and act accordingly
        if option == 1:
          exec(open("defis/main.py",encoding="utf-8").read())
        elif option == 2:
            option2()
        elif option == 3:
            exec(open("divers/regle.py",encoding="utf-8").read())
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

