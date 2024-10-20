"""Tests fns from list_fns"""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """get_first should return first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"  # RV shoudl be husky


def test_remove_first_return_value() -> None:
    """remove_first should have an RV of None"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) is None


def test_remove_first_behavior() -> None:
    """remove_first should remove the first element from the input list"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


def test_get_first_edge_case() -> None:
    """get_first called on an empty list should return ""."""
    assert get_first([]) == ""


def test_get_and_remove_first() -> None:
    # I don't feel like adding functionality to this test rn
    pointless: str = get_and_remove_first(["husky", "golden", "poodle", "lab"])
    pointless = pointless * 2
    return None
