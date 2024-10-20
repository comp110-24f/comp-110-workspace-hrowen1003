"""Test the functionality of find_max.py"""

__author__ = "730722910"

from CQs.cq07.find_max import find_and_remove_max


def test_max_return() -> None:
    """tests if find_and_remove max returns correct max"""
    test_input: list[int] = [5, 2, 3, 5, 5, 3, 5]
    assert find_and_remove_max(test_input) == 5  # max should be 5


def test_max_mutate() -> None:
    """tests if find_and_remove_max correctly mutates input list"""
    test_input: list[int] = [
        5,
        2,
        3,
        5,
        5,
        3,
        5,
    ]  # two fives in a row check that previous idx-jumping problem is fixed
    find_and_remove_max(test_input)
    assert test_input == [2, 3, 3]


def test_max_edge_case() -> None:
    """tests if find_and_remove_max correctly returns empty list if all nums are same"""
    same_input: list[int] = [1, 1, 1, 1, 1, 1]
    find_and_remove_max(same_input)  # max = 1
    assert same_input == []
