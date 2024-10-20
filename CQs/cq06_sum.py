"""Summing the elements of a list using different loops"""

__author__ = "730722910"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0  # because vals is a list of floats, sum should be a float
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for num in vals:
        sum += num  # for a for loop, num represents the elem not the idx
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[
            idx
        ]  # this is more similar to a while loop, but without the need to define or
        # progress idx
    return sum
