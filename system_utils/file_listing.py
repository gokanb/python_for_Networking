"""List the files in the current working directory, in green."""

import os

from termcolor import colored


def list_current_directory():
    for entry in os.listdir(os.getcwd()):
        print(colored(f"[+] {entry}", "green"))


if __name__ == "__main__":
    list_current_directory()
