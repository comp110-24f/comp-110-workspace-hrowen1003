"""Try to creat movement in 5/5 grid controlled by user"""

import os

# /|\/|\/|\/|\
#  |  |  |  |
#
#
#


# =====
# =====
# =====
# =====
# =====

background: dict[int, list[str]] = {
    5: [
        "=",
        "=",
        "=",
        "=",
        "=",
    ],
    4: [
        "=",
        "=",
        "=",
        "=",
        "=",
    ],
    3: [
        "=",
        "=",
        "=",
        "=",
        "=",
    ],
    2: [
        "=",
        "=",
        "=",
        "=",
        "=",
    ],
    1: [
        "=",
        "=",
        "=",
        "=",
        "=",
    ],
}

# player: str = "\U0001F920"
player: str = "O"


def main() -> None:
    x: int = 3
    y: int = 3
    playing: bool = True
    while playing:
        display(x, y)
        last_inpt = input("")
        playing = check_playing(last_inpt)
        y = change_y(y, last_inpt)
        x = change_x(x, last_inpt)


def display(x: int, y: int) -> None:
    os.system("clear")
    for line in background:
        line_sum: str = ""
        for object in background[line]:
            if y == line and x - 1 == len(line_sum):
                line_sum += player
            else:
                line_sum += object
        print(line_sum)


def check_playing(last_inpt: str) -> bool:
    if last_inpt == "quit":
        return False
    else:
        return True


def change_x(x: int, last_inpt: str) -> int:
    if last_inpt == "a" and x != 1:
        x -= 1
    if last_inpt == "d" and x != 5:
        x += 1
    return x


def change_y(y: int, last_inpt: str) -> int:
    if last_inpt == "s" and y != 1:
        y -= 1
    if last_inpt == "w" and y != 5:
        y += 1
    return y


if __name__ == "__main__":
    main()
