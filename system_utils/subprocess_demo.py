"""Show two ways to run a shell command from Python: os.system and subprocess."""

import os
from subprocess import call


def main():
    print("Current path:", os.getcwd())
    print("PATH:", os.getenv("PATH"))

    print("\nListing files with os.system:")
    os.system("ls -la")

    print("\nListing files with subprocess.call:")
    call(["ls", "-la"])


if __name__ == "__main__":
    main()
