import rich
from rich.prompt import Prompt
import numpy as np
import random

def find_element(matrix, target):
    matrix = np.array(matrix)
    indices = np.where(matrix == target)
    if indices[0].size > 0:
        return indices[0][0], indices[1][0]
    else:
        return None


def double(matrix):
    choose_doubles = Prompt.ask(
        "[green] Choose two vertically or horizontally adjoined numbers"
    ).split()
    print(choose_doubles)
    get_val = []

    for i in range(2):
        get_val.append(find_element(matrix, int(choose_doubles[i])))

    print(get_val)
    
    if get_val[0][0] == get_val[1][0] and get_val[0][1] + 1 == get_val[1][1]:
        print(choose_doubles, " are neighbors horizontally")
        return True, choose_doubles
    elif get_val[0][1] == get_val[1][1] and get_val[0][0] + 1 == get_val[1][0]:
        print(choose_doubles, " are neighbors vertically")
        return True, choose_doubles
    else:
        print("Not neighbors, try again") 
        #add a while loop here that will force the user to chose the two correct neighbors
 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27],
    [28, 29, 30],
    [31, 32, 33],
    [34, 35, 36],
]
while True:
           
    is_neighbors, chosen_neighbors = double(matrix) 

    if is_neighbors:
        rand_int = str(random.randint(0, 36))
        print("Roulette says", rand_int)
        print("Choosen neighbors", chosen_neighbors)
        if rand_int in chosen_neighbors:
            print("[green] YOU WON")
        else: 
            print("You did not win")
    


