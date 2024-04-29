import sys
import os
from pathlib import Path
from colorama import Fore

def dir_structure(path, indent=""):

    # if the path is not a dir print an error message and exit the function
    if not os.path.isdir(path):
        print(f"{Fore.RED}{path} is not a directory!{Fore.RESET}")
        return

    # getting the list of items in the directory
    items = Path(path).iterdir()

    # iterate items in the directory
    for item in items:
        # if an item is a file, print it in green
        if item.is_file():
            print(f"{indent}{Fore.GREEN}{item.name}{Fore.RESET}")
        # if an item is a dir print it in blue
        elif item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/{Fore.RESET}")
            # check the dirs content
            dir_structure(item, indent + "  ")

# checking the entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}To run the script type {Fore.RESET}python 3.py /path/to/dir{Fore.RED} in terminal{Fore.RESET}.")
        sys.exit(1)

path = sys.argv[1]
dir_structure(path)