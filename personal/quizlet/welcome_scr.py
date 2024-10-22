import time
import os

Q: list[str] = ["/^^^\\", "|   |", "| \\ |", "\\__\\/"]
U: list[str] = ["|   |", "|   |", "|   |", "\\___/"]
I: list[str] = ["^^T^^", "  |  ", "  |  ", "__|__"]
Z: list[str] = ["^^^/^", "  /  ", " /   ", "/____"]
L: list[str] = ["|    ", "|    ", "|    ", "|____"]
E: list[str] = ["|^^^^", "|____", "|    ", "|____"]
T: list[str] = ["^^T^^", "  |  ", "  |  ", "  |  "]
front_emph: list[str] = [" -=**", "<====", "<====", " -=**"]
back_emph: list[str] = ["**=-", "====>", "====>", "**=-"]
blank: list[str] = ["     ", "     ", "     ", "     "]
sml_blank: list[str] = ["  ", "  ", "  ", "  "]
total_ltrs: list[list] = [Q, U, I, Z, L, E, T, front_emph, back_emph]
# /^^^\ |   | ^^T^^ ^^^/^ |     |^^^^ ^^T^^
# |   | |   |   |     /   |     |____   |
# | \ | |   |   |    /    |     |       |
# \__\/ \___/ __|__ /____ |____ |____   |

# -=**
# =====
# =====
# -=**

# **=-
# =====
# =====
# **=-

# |^^\
# |   \
# |   /
# |__/
D = ["|^^\\ ", "|   \\", "|   /", "|__/ "]
# |   |
# \   /
# | |
#  V
V = ["|   |", "\\   /", " | | ", "  V  "]
# |   |
# |\  |
# | \ |
# |  \|
N = ["|   |", "|\\  |", "| \\ |", "|  \\|"]
#  |
#  |
#  |
#  o
excl = ["  |  ", "  |  ", "  |  ", "  o  "]

idx: int = 0
current_line: str = ""
while idx < len(Q):
    current_line += (Q[idx]) + " "
    idx += 1
# print(current_line)

ltrs: list[str] = Q


def make_line(ltrs: list[list], line_num: int) -> str:
    line: str = str()
    for char in ltrs:
        line += char[line_num]
        line += " "
    return line


def print_word(ltrs: list[list]) -> None:
    for line_num in range(
        0, len(ltrs[0])
    ):  # replace ltrs[0] sometime with a function that find the ltr with the max lines
        print(make_line(ltrs, line_num))


def listify(ltrs: str) -> list:
    list_ltrs: list = []
    for char in ltrs:
        idx = 0
        while idx < len(total_ltrs):
            if char == str(total_ltrs[idx]):
                char = total_ltrs[idx]
            idx += 1
        list_ltrs += char
    return list_ltrs


def titleify() -> None:
    os.system("clear")
    for sec in range(0, 9):
        dots: str = "." * (sec % 3 + 1)
        print(dots)
        time.sleep(0.2)
        os.system("clear")
    # print("Your list of available chars is: " + str(total_ltrs))  # FIX THIS AH
    # ltrs: str = input("What would you like to print ~fancily~?")
    # add function to check validity of characters input
    # print(listify(ltrs))
    print_word([front_emph, sml_blank, Q, U, I, Z, L, E, T, excl, sml_blank, back_emph])
    time.sleep(1)


if __name__ == "__main__":
    titleify()
