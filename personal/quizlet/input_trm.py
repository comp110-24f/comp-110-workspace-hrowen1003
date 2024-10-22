"""Program for user to input and store their terms and definitions"""

import time
import os

new_terms: dict[str, str] = dict()


def input_pair(add_count: int) -> None:
    time.sleep(0.5)
    os.system("clear")
    idx: int = len(new_terms)
    add_count += len(new_terms)
    while idx < add_count:
        print(f"<====Term: {idx+1}====>")
        new_terms[input("Word --> ")] = input("Definition --> ")
        idx += 1
    print("=" * len(f"<====Term: {idx+1}====>"))


def initiate_input() -> dict[str, str]:
    input_pair(int(input("How many terms and definitions would you like to add? ")))
    return new_terms


if __name__ == "__main__":
    initiate_input()
