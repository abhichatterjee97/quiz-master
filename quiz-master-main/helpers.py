from os import system, name
from time import sleep
from datetime import datetime

now = datetime.now()
current_hour = int(now.strftime("%H"))


def ask_yes_no(question):
    """
    Asks the user for input for a Yes/No Question
    and returns a boolean

    Args:
    question: The question to ask
    """
    yes = ["yes", "y"]
    no = ["no", "n"]

    print(f"\n{question} \n\ny/n\n")
    while True:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("[Y]es or [N]o")
            continue


def is_quit(response):
    """
    Checks if the user's response
    was to quit the game, if so ask to confirm.
    Returns True if user wants to quit,
    otherwise returns False.
    """
    if response.lower() in ["q", "quit"]:
        if ask_yes_no("Would you like to return to the Main Menu?"):
            return True
        else:
            return False
    else:
        return False


def ask_any_key():
    """
    Ask the user to press any key to return to main menu
    """
    input("Press any key to return to Main Menu.")
    return


def clear():
    """
    Clears the Terminal Window
    """
    # for Windows
    if name == "nt":
        _ = system("cls")

    # for macOS/Linux
    else:
        _ = system("clear")
