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


display(game_points)

# String analogy:
# fruit: str = ""
# fruit: str = str()


# Method: a function that belongs to the list class
# It's like calling append(grocery_list, "bananas"), but correct syntax is:
# <list name>.append()
