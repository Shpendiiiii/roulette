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
    style = "red"
    print(s)
    for row in matrix:
            for item in row:
                if style == "black":
                    style = "red"
                else:
                    style = "red"
            console.print(" ".join([format(item, "2d") if type(item) == int else item for item in row]), style)


eu_v1 = generate_matrix_style("EU")
us_v1 = generate_matrix_style("US")


pretty_print_matrix(us_v1)



