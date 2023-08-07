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


def generate_matrix_style(input="EU"):
    pure_matrix = generate_pure_matrix()
    if input == 'EU':
        pure_matrix.insert(0, [0])
        return pure_matrix
    else:
        pure_matrix.insert(0, [0, "00"])
        return pure_matrix


def pretty_print_matrix(matrix):
    """
    Print a matrix in a pretty format.

    Args:
        matrix: The matrix to print.
    """
    console = Console()

    red = "[red]"
    black = "[black]"
    is_red = True

    for row in matrix:
        formatted_row = []
        for item in row:
            color = red if is_red else black
            item_str = str(item)
            if isinstance(item, int) and len(item_str) < 2:
                item_str = " " + item_str
            formatted_item = f"{color} {item_str}"
            formatted_row.append(formatted_item)
            is_red = not is_red

        console.print(" ".join(formatted_row))


eu_v1 = generate_matrix_style("EU")
us_v1 = generate_matrix_style("US")

pretty_print_matrix(us_v1)
