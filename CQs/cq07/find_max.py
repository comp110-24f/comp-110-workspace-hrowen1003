"""Define function to locate and remind max value of a list"""

__author__ = "730722910"


def find_and_remove_max(input: list[int]) -> int:
    """identifies max and remove all instances it from input list"""
    if len(input) == 0:
        return -1  # edge case
    max: int = 0
    for num in input:
        if num > max:
            max = num
    idx: int = 0
    while idx < len(input):  # could also work as while loop using range()
        if input[idx] == max:
            input.pop(idx)
        else:  # if elem is popped, then all following elems get idx shifted down one,
            # so you only need to increase idx when elem /= max
            idx += 1
    return max
