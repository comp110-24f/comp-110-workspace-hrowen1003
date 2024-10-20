"""Define functions to be tested by utils_test"""

__author__ = "730722910"


def only_evens(input: list[int]) -> list[int]:
    """returns onyl the even elements of a list of ints"""
    evens: list[int] = []
    for num in input:
        if num % 2 == 0:  # checks if num is even
            evens.append(num)  # can't use += for lists, instead append method
    return evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """return the subsection of input list from start to end-1 indexes"""
    output: list[int] = []
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    if len(input) == 0 or start >= len(input) or end <= 0:  # if end <= 0, NOT end >= 0
        return output  # if any of above conds met, no need to use for loop
    for idx in range(start, end):
        output.append(input[idx])
    return output


def add_at_index(input: list[int], num: int, idx: int) -> None:
    """adds num at a specific index in input"""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    stor: list[int] = []  # store elems of input after and including desired index
    for temp_idx in range(idx, len(input)):
        stor.append(input[temp_idx])  # storing each elem in stor
    while idx < len(input):
        input.pop(idx)  # remove these elems temporarily so num can be appended to input
    input.append(num)  # insert num by appending to now shortened input
    for elem in stor:
        input.append(elem)  # add original elems of input back in
