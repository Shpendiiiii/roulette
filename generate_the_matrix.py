from rich.color import ColorParseError
from rich.console import Console


def generate_pure_matrix():
    main = []
    ii = 0
    for i in range(0, 12):
        seed = []
        for j in range(4):
            seed.append(ii)
            ii += 1
        main.append(seed)
    return main


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
            color_dict.update({f"{item}": f"{color}"})
            is_red = not is_red
    return color_dict


matrix = generate_pure_matrix()
print("the var matrix", matrix)


def generate_matrix_style():
    pure_matrix = generate_colors(matrix)

    pure_matrix.update({"00": "[green]"})
    return pure_matrix


styled_matrix = generate_matrix_style()
gen = generate_colors(styled_matrix)


def pretty_print_matrix(dictionary):
    """
    Print a matrix in a pretty format.

    Args:
        matrix: The matrix to print.
    """
    console = Console()

    i = 0

    for key, value in dictionary.items():
        if i % 3 == 0:
            print("\n")
        space = "\n"

        if len(key) < 2:
            console.print(f"{value}  {key}", end=" ")
        else:
            console.print(f"{value} {key}", end=" ")
        i += 1


pretty_print_matrix(gen)
