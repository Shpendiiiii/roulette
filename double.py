import rich
from rich.prompt import Prompt
import numpy as np


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
    elif get_val[0][1] == get_val[1][1] and get_val[0][0] + 1 == get_val[1][0]:
        print(choose_doubles, " are neighbors vertically")
    else:
        print("Not neighbors, try again") 


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
    double(matrix)
