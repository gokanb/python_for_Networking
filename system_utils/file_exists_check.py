"""Check whether a file given on the command line exists and is readable.

Usage:
    python file_exists_check.py <path>
"""

import os
import sys

from termcolor import colored


def main():
    if len(sys.argv) != 2:
        print("Usage: python file_exists_check.py <path>")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.isfile(path):
        print(colored(f"[-] The file '{path}' does not exist.", "red"))
        sys.exit(1)

    print(colored(f"[+] The file '{path}' exists.", "green"))

    # os.R_OK is the correct flag for "is this readable?"
    if os.access(path, os.R_OK):
        print(colored("[+] The file is readable.", "green"))
    else:
        print(colored("[-] Access to the file is denied.", "red"))


if __name__ == "__main__":
    main()
