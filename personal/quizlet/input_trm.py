"""Program for user to input and store their terms and definitions"""

import time
import os

wrds: list[str] = []
defs: list[str] = []


def input_pair(num: int) -> None:
    time.sleep(1)
    os.system("clear")
    idx: int = 0
    while idx < num:
        print(f"<====Term: {idx+1}====>")
        wrds.append(input("Word --> "))
        defs.append(input("Definition --> "))
        idx += 1
    print("=" * len(f"<====Term: {idx+1}====>"))


def initiate_input() -> None:
    input_pair(int(input("How many terms and definitions would you like to add? ")))


if __name__ == "__main__":
    initiate_input()
