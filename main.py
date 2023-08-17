from generate_the_matrix import *
from rich.style import Style
from rich.prompt import Prompt
from rich.prompt import Confirm
import rich
import random
from dummy_loading import loading_animation

console = Console(color_system="truecolor")


def welcome_screen():
    is_US = Confirm.ask("Do you want a US styled roulette? Default is European")
    if is_US:
        matrix = generate_matrix_style(generate_pure_matrix(), "US")
        colored_dict = generate_colors(matrix)
    else:
        matrix = generate_matrix_style(generate_pure_matrix())
        colored_dict = generate_colors(matrix)
    pretty_print_matrix(colored_dict)
    return matrix, colored_dict, is_US


def color_bet(colored_dict):
    the_color_chooser = random.randint(0, 1)
    color = Prompt.ask("\nBet on red or black?")
    if the_color_chooser == 0 and color == "red":
        print("you won")
        for key, value in colored_dict.items():
            if value == "[red]":
                print(key, end=", ")
    elif the_color_chooser == 1 and color == "black":
        print("you won")
    else:
        print("lost")


def straight_up(is_us):
    if is_us:
        number_chooser = random.randint(0, 37)
    else:
        number_chooser = random.randint(0, 36)

    number = Prompt.ask("[green] \n\n Choose your number")
    loading_animation(random_end=37)
    if number_chooser != 37:
        console.print(f"[green] Roulette says: {number_chooser}")
    if str(number_chooser) == str(number):
        console.print("[bold red] You won\n")
    else:
        if str(number_chooser) == "37" and str(number) == "00":
            console.print("[green] roulette says 00")
            console.print("[red] Wow, won!\n")
        console.print("[bold pink] Better luck next time\n")


def column_bet(is_us):
    number_chooser = random.randint(0, 36)
    print("\n")
    choose_column = Prompt.ask("[green] \nBet on row")

    loading_animation()
    column = None
    console.print(f" Roulette says: {number_chooser}")
    if number_chooser % 3 == 1:
        column = 1
    elif number_chooser % 3 == 2:
        column = 2
    else:
        column = 3

    if choose_column == str(column):
        console.print("[blue] You won!")
    else:
        console.print("[red] Better luck next time!")
        console.print(f"[bold blue] {number_chooser} is in column {column}")


matrix, colored_dict, is_us = welcome_screen()
# print(colored_dict)
# while True:
# color_bet(colored_dict)
while True:
    # straight_up(is_us)
    column_bet(is_us)
