# code utf-8

# imports
from Player.player import *   
from Map.mapmatrice import * 

# lecture of the map
for y in range(len(matrice)):
    row = ""
    for x in range(len(matrice[y])):
        element = matrice[y][x]
        if x == player["x"] and y == player['y']:
            row+= "👽"
        elif element == 8:
            row+="⛩"
        elif element == 7:
            row+="🌏"
        elif element == 6:
            row+="🏰"
        elif element == 5:
            row+="🏯"  
        elif element == 4:
            row+="🌲"
        elif element == 3:
            row+="🌴"
        elif element == 2:
            row+="🌳"
        elif element == 0:
            row+="🟦"
        elif element == 1:
            row+="🗻"
    print(row)
        
print(player)
