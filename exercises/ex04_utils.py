"""Reconstructing idioms and functions of python from scratch"""

__author__ = "730722910"


def all(int_list: list[int], num: int) -> bool:
    """Checks if all of the elements in int_list equal num"""
    idx: int = 0
    while idx < len(int_list):
        if (
            int_list[idx] != num
        ):  # This cuts the program short the moment num doesn't equal some idx
            return False
        idx += 1
    return True


def max(int_list: list[int]) -> int:
    """Finds the max value in an int_list"""
    if len(int_list) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # stops function and provides user error info
    idx: int = 0
    max: int = int_list[0]  # just like the card-max algorithm from class
    while idx < len(int_list):
        if int_list[idx] > max:
            max = int_list[idx]
        idx += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if each element in each list is the same"""
    idx: int = 0
    if len(list_1) != len(
        list_2
    ):  # lists can't be equal if they aren't the same length
        return False
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appends each element of list_2 on to the end of list_1"""
    idx: int = 0
    while idx < len(list_2):
        list_1.append(list_2[idx])  # .append is a method, as compared to a function
        idx += 1
