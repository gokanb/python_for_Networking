"""Print information about the script's command-line arguments.

Usage:
    python argv_info.py one two three
"""

import sys

from termcolor import colored


def main():
    print(colored(f"Script name: {sys.argv[0]}", "blue"))
    print(colored(f"Argument count: {len(sys.argv) - 1}", "red"))
    print(colored(f"All arguments: {sys.argv}", "cyan"))

    # Print each extra argument safely, without assuming how many were given.
    for index, argument in enumerate(sys.argv[1:], start=1):
        print(colored(f"  Argument {index}: {argument}", "green"))

    print(colored(f"Platform: {sys.platform}", "yellow"))
    print(colored(f"Python version: {sys.version}", "yellow"))


if __name__ == "__main__":
    main()
