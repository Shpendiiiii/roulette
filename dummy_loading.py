# import time
# import random
# import rich
# from rich.console import Console
#
#
# def loading_animation(duration=0.5, interval=0.1, random_start=0, random_end=36):
#     console = Console()
#     symbols = ["-", "\\", "|", "/"]
#     start_time = time.time()
#
#     while time.time() - start_time < duration:
#         for symbol in symbols:
#             rand_int = random.randint(random_start, random_end)
#             print(f"Loading... {symbol} {rand_int}", end="\r")
#             # print("", end="\r")
#             time.sleep(interval)


import time
import random
from rich.console import Console


def loading_animation(duration=0.5, interval=0.1, random_start=0, random_end=36):
    console = Console()
    symbols = ["-", "\\", "|", "/"]
    start_time = time.time()

    while time.time() - start_time < duration:
        for symbol in symbols:
            if time.time() - start_time >= duration:
                break  # Break the inner loop if the duration time has been reached
            rand_int = random.randint(random_start, random_end)
            print(f"Loading... {symbol} {rand_int}", end="\r")
            time.sleep(interval)

    # Clear the line here
    print(" " * 50, end="\r")


# loading_animation()
