# code utf-8

# other files
from Player.player import *    

# matrice of the map
map_mattrix = [
    [1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,0,1,1,8,1,1,1,1,4,4,4,4,4,1,1,1,1,1,1,1,1],
    [4,4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1],
    [4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1],
    [4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,1,1,1,1],
    [4,4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1],
    [4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1],
    [4,4,4,4,4,4,4,4,0,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1],
    [4,4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1],
    [4,4,4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2,0,0,0,2,2,2,2,2,2,2,3,3,3,3,3,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,3,3,3,3,3,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,3,3,3,3,3,0,0,0,0,0],
    [2,2,2,2,2,7,2,2,2,2,0,0,2,2,2,2,2,2,2,2,1,3,3,3,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,2,1,1,3,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,6,2,2,1,1,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
]

# functions to play the map

print(player)
for y in range(len(map_mattrix)):
    row = ""
    for x in range(len(map_mattrix[y])):
        element = map_mattrix[y][x]
        if x == player["x"] and y == player['y']:
            row+= "😁"
        elif element == 8:
            row+="⚫"
        elif element == 7:
            row+="📜"
        elif element == 6:
            row+="🔱"
        elif element == 5:
            row+="🗿"  
        elif element == 4:
            row+="🌿"
        elif element == 3:
            row+="🟧"
        elif element == 2:
            row+="🌴"
        elif element == 0:
            row+="🟦"
        elif element == 1:
            row+="⛰ "
    print(row)
        

