"""Gives Wordle-like information about a five letter word, given an input letter"""

__author__ = "730722910"  # For my PID, can us "#" or str(#). They are equal


def main() -> None:  # Assigns values to parameters for contains_char
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    word: str = input(
        "Enter a 5-character word: "
    )  # Don't forget to leave space after ":"
    if len(word) != 5:  # Don't need an if statement for if (word==5) here
        print("Error: Word must contain 5 characters.")
        exit()  # terminates running of entire program
    return word  # returns word to become an argument in contains_char call


def input_letter() -> str:
    letter: str = input(
        "Enter a single character: "
    )  # Remember including the end space
    if len(letter) != 1:
        print("Error: Character must be a single character")
        exit()
    return letter  # returns word to become an arguement in contains_char call


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if letter == word[0]:
        print(letter + " found at index 0")  # Indexes start with 0
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(
            letter + " found at index 4"
        )  # This kind of process will be easier with loops in the future
        count = count + 1
    if (
        count == 0
    ):  # The following if/elif/else statements output instances of letter found in word
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(
            str(count) + " instance of " + letter + " found in " + word
        )  # Don't forget to remove pluralization when there's one of something, duh!
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # No return statement needed (return value is None)


if __name__ == "__main__":  # runs main() function
    main()
