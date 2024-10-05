"""List Syntax Guide"""

my_numbers: list[float] = [3.5, 2.5]  # constructor
your_numbers: list[float] = []  # literal
game_points: list[int] = [102, 86, 94]


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""
    idx: int = 0
    while idx < len(int_list):
        print(list[idx])
        idx += 1


# display(game_points)


# def lessen(my_list: list[str]):
# idx: int = 0
# while idx < len(my_list):
#    my_list[idx] = my_list[idx] - 1
#   idx += 1


# msg: list[str] = [4, 5, 6]
# lessen(msg)
# print(msg)

# String analogy:
# fruit: str = ""
# fruit: str = str()


# Method: a function that belongs to the list class
# It's like calling append(grocery_list, "bananas"), but correct syntax is:
# <list name>.append()
