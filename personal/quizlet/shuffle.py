"""Playing with dictionaries 10/21"""

import random

terms: dict[str, str] = {
    "femur": "bone",
    "bicep": "muscle",
    "stomach": "digestive organ",
}


def shuffle_dict(terms: dict[str, str]) -> dict[str, str]:
    items: list[tuple] = list(terms.items())
    random.shuffle(items)
    shuffled_terms: dict[str, str] = dict(items)
    return shuffled_terms


def playing_around() -> None:
    """ignore this functino, it was just to help with understanding concepts"""
    shuffle_dict(terms)

    # Below is partly imported from internet to test how to randomize dictionaries

    my_dict = {"a": 1, "b": 2, "c": 3}

    # Convert dictionary to list of key-value pairs
    items = list(my_dict.items())

    print(f"items is {items}")
    print(f"index 1 of items is {items[1]}")

    # Shuffle the list
    random.shuffle(items)

    print(f"items is now {items}")

    # Create a new dictionary from the shuffled list
    shuffled_dict = dict(items)

    print(f"shuffled_dict is {shuffled_dict}")


if __name__ == "__main__":
    print(shuffle_dict(terms))
