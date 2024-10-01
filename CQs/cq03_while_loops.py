"""Challenge Question #3: While Loops"""

__author__ = "730722910"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts the number of times search_char appears in a phrase"""
    match_count = 0
    index = 0  # create local variable index to cycle through the characters of phrase
    while index < len(phrase):
        if (
            search_char == phrase[index]  # use two "=" b/c it's a conditional
        ):  # use subscription syntax to check if individual letters match
            match_count += 1  # simpler way of saying increasing match_count by 1
        index += 1  # don't forget to increase index or code will never stop running
    return match_count
