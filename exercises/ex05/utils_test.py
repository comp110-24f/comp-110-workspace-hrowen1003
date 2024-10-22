"""Test functions from utils"""

__author__ = "730722910"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

# ========== UNIT TESTS for only_evens() ==========


def test_only_evens_return() -> None:
    """Tests if only_evens correct returns even nums for a normal use case"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]
    assert only_evens(test_list) == [2, 4, 6, 6]


def test_only_evens_mutation() -> None:
    """Checks if only_even mutates its input, which it should not do"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]
    only_evens(test_list)
    same: bool = (
        True  # temp var to test if each idx of test_list is still the same after
        # only_evens was called
    )
    if len(test_list) != len([1, 2, 3, 4, 5, 6, 6]):
        same = (
            False  # if len(test_list) changed, it was mutated and is no longer the same
        )
    idx: int = 0
    while idx < len(test_list):  # while loop to test if each elem is still the same
        if [1, 2, 3, 4, 5, 6, 6][idx] != test_list[idx]:
            same = False
        idx += 1
    assert same  # do not need "== True", because same is already a bool


def test_only_evens_edge() -> None:
    """Tests only_evens edge case in which an empty list is input"""
    test_list: list[int] = []
    assert (
        only_evens(test_list) == []
    )  # the desired functionality for this edge case would be for
    # an empty list to be returned


# ========== UNIT TESTS for sub() ==========


def test_sub_return() -> None:
    """Tests that sub returns correct subsection of input"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]
    assert sub(test_list, 1, 4) == [2, 3, 4]


def test_sub_mutation() -> None:
    """Tests that input was not mutated by sub"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]
    sub(test_list, 1, 4)
    same: bool = True  # bool var to check each idx is correct after fn call
    if len(test_list) != len([1, 2, 3, 4, 5, 6, 6]):
        same = (
            False  # if len(test_list) changed, it was mutated and is no longer the same
        )
    idx: int = 0
    while idx < len(test_list):  # while loop to test if each elem is still the same
        if [1, 2, 3, 4, 5, 6, 6][idx] != test_list[idx]:
            same = False
        idx += 1
    assert same  # do not need "== True", because same is already a bool


def test_sub_edge() -> None:
    """Tests if sub correctly returns empty list when bounds are invalid"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]  # len(test_list) = 7
    assert sub(test_list, 20, 19) == []


# ========== UNIT TESTS for add_at_index() ==========


def test_add_at_index_return() -> None:
    """Tests that add_at_index returns None"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]
    assert (
        add_at_index(input=test_list, num=7, idx=1) is None
    )  # VS Code wants by to use "is" but I don't know if we're allowed to use that yet


def test_add_at_index_mutation() -> None:
    """Tests that input is mutated to only add num at correct idx"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]
    add_at_index(input=test_list, num=7, idx=1)
    same: bool = True  # bool to check if each idx of input after mutation is correct
    if len(test_list) != len([1, 7, 2, 3, 4, 5, 6, 6]):
        same = (
            False  # if len(test_list) didn't increase by 1, it wasn't mutated correctly
        )
    idx: int = 0
    while idx < len(
        test_list
    ):  # while loop to test if each elem is same as intended output
        if [1, 7, 2, 3, 4, 5, 6, 6][idx] != test_list[idx]:
            same = False
        idx += 1
    assert same  # do not need "== True", because same is already a bool


def test_add_at_index_raises_indexerror_edge() -> None:
    """Tests add_at_index raises IndexError; edge_case where idx is out of bounds"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 6]
    with pytest.raises(IndexError):
        add_at_index(
            input=test_list, num=7, idx=15
        )  # checks if index error is being raised for edge case
