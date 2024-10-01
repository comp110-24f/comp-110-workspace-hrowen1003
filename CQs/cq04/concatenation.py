"""CQ4 Concatenation Programs"""

__author__ = "730722910"

word1: str = "happy"
word2: str = "tuesday"


def main() -> None:  # I didn't NEED a main() function, but it's probably a good habit?
    print(concat(word1, word2))


def concat(str_1: str, str_2: str) -> str:
    """Function to return the combination of two strings"""
    return (
        str_1 + str_2
    )  # if these parameters weren't explicitly str's, I'd have to use str() to concat


if (
    __name__ == "__main__"
):  # This ensures the whole file isn't automatically run when imported
    main()
