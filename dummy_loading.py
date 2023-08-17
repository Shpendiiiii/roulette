import time
import random
import rich
from rich.console import Console


def loading_animation(duration=0.5, interval=0.1):
    console = Console()
    symbols = ["-", "\\", "|", "/"]
    start_time = time.time()

    while time.time() - start_time < duration:
        for symbol in symbols:
            rand_int = random.randint(0, 37)
            print(f"Loading... {symbol} {rand_int}", end="\r")
            time.sleep(interval)
