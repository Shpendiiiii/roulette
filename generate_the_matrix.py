import time

from rich.color import ColorParseError
from rich.console import Console


def generate_pure_matrix():
    main = []
    ii = 1
    for i in range(0, 12):
        seed = []
        for j in range(3):
            seed.append(ii)
            ii += 1
        main.append(seed)
    return main


def generate_matrix_style(pure_matrix, style="EU"):
    pure_matrix.insert(0, [0])
    if style == "US":
        pure_matrix.insert(1, ["00"])
    return pure_matrix


def generate_colors(matrix):
    """
       Generate the reds and blacks for the matrix

    Args:
        matrix: the generated matrix (not the one with the 0)
    """
    red = "[red]"
    black = "[black]"
    is_red = True
    color_dict = {}
    for row in matrix:
        for item in row:
            color = black if is_red else red
            if item == 0 or item == "00":
                color_dict.update({f"{str(item)}": "[green]"})
            else:
                color_dict.update({f"{str(item)}": f"{color}"})
            is_red = not is_red
    return color_dict


def pretty_print_matrix(dictionary):
    """
    Print a matrix in a pretty format.

    Args: 
        matrix: The matrix to print.
    """
    console = Console()
    i = 0
    for key, value in dictionary.items():
        if i != 0 and i % 3 == 0:
            print("\n")
        if key == "0" or key == "00":
            if "00" not in dictionary:
                console.print(f"[green]{' ' * 6}{key}")
                # print("\n")
            else:
                console.print(f"[green]{' ' * 3}{key}", end="")
            i -= 1
        if len(key) < 2 and key != "0" and key != "00":
            if i == 0 and "00" in dictionary:
                print("\n")
            console.print(f"{value}  {key}", end=" ")
        elif key != "0" and key != "00":
            console.print(f"{value} {key}", end=" ")
        i += 1


# pure_matrix = generate_pure_matrix()
# dict_with_colors = generate_colors(pure_matrix)
# final = pretty_print_matrix(dict_with_colors)
pretty_print_matrix(generate_colors(generate_matrix_style(generate_pure_matrix())))
print("\n")
pretty_print_matrix(generate_colors(generate_matrix_style(generate_pure_matrix(), "US")))





# print((generate_matrix_style(generate_pure_matrix())))
