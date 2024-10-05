"""Mutating functions."""

__author__ = "730722910"


def manual_append(
    old_list: list[int], new_int: int
) -> None:  # Use colons for parameters, not =!!!
    """Appends new_int onto end of old_list"""
    old_list.append(new_int)


def double(old_list: list[int]) -> None:
    """Should multiply each element in old_list by 2"""
    idx: int = 0
    while idx < len(old_list):
        old_list[idx] = old_list[idx] * 2
        idx += 1  # if you forget to include this, the code will run forever......


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
