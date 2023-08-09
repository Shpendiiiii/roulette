from generate_the_matrix import *
from rich.style import Style
import rich

console = Console(color_system="truecolor")

us_v1_v1 = generate_matrix_style("US")

test = pretty_print_matrix(us_v1_v1)

print(test)


def welcome_screen():
    style = Style()
    style.fg = "#87CEFA"
    return style
