"""Test functions from utils"""

__author__ = "730722910"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

# === UNIT TESTS for only_evens() ===


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


# === UNIT TESTS for sub() ===


# === UNIT TESTS for add_at_index() ===


def test_add_at_index_raises_indexerror() -> None:
    """Tests that add_at_index correctly raises IndexError for edge_case where idx is out of bounds of input"""
