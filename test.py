import rich


def print_in_bright_baby_blue(text):
    """Prints the given text in bright baby blue."""
    rich.print(
        f"This text is in bright baby blue: {text}", style=rich.color.rgb(87, 192, 250)
    )


if __name__ == "__main__":
    print_in_bright_baby_blue("Hello, shpend!")
