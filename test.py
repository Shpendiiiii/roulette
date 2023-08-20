from rich import print
from rich.text import Text
import threading
import time
import msvcrt

exit_flag = False

def monitor_exit_condition():
    global exit_flag
    while not exit_flag:
        if msvcrt.kbhit():  # Check if a key was pressed
            key = msvcrt.getch().decode('utf-8')  # Get the pressed key
            if key.lower() == "exit":
                exit_flag = True
                print("Exiting the program.")

def print_in_bright_baby_blue():
    """Prints the given text in bright baby blue."""
    styled_text = Text.assemble(
        "This text is in bright baby blue:", style="rgb(175, 0, 255)"
    )
    print(styled_text)
    ask_user = input("What is your fav color of the alphabet: ")
    styled_text_2 = Text.assemble(ask_user, style="blink magenta")
    print(styled_text_2)

def main():
    while not exit_flag:
        print_in_bright_baby_blue()
        time.sleep(1)  # Simulating some work

if __name__ == "__main__":
    exit_thread = threading.Thread(target=monitor_exit_condition)
    main_thread = threading.Thread(target=main)

    exit_thread.start()
    main_thread.start()

    exit_thread.join()
    main_thread.join()

    print("Program has been gracefully exited.")
