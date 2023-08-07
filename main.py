from generate_the_matrix import *
from rich.style import Style
import rich

us_v1_v1 = generate_matrix_style("EU")

pretty_print_matrix(us_v1_v1)

def welcome_screen():
    style = Style()
    style.fg = "#87CEFA"
    return style

rich.print("Welcome, choose your table stylem, US or European", style=welcome_screen())
