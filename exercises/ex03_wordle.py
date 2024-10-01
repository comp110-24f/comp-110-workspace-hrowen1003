"""Next Step in Making (*almost) Wordle"""

__author__ = "730722910"


WHITE_BOX: str = "\U00002B1C"  # not in snake_case b/c it's a global constant?
GREEN_BOX: str = "\U0001F7E9"  # not in snake_case in exercise outline
YELLOW_BOX: str = "\U0001F7E8"


def main(secret_word: str) -> None:
    """Beginning of program and main game controller"""
    turn: int = 1
    win_state: bool = False  # win_state helps stop loop if user wins early
    while turn <= 6 and not win_state:  # b/c turn starts at 1, not 0, this should be <=
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(
            secret_len=len(secret_word)
        )  # this and the following line could be written as one...
        print(
            emojified(guess=guess, secret_word=secret_word)
        )  # but it would be long and confusing, so this helps abstract/simplify
        if guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            win_state = True  # stops game early if user succeeds
        turn += 1
    if (
        turn > 6 and not win_state
    ):  # "and not win_state" is needed in case user wins on 6th turn
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_len: int) -> str:
    """Verifies that input word length is equal to secret word length"""
    word: str = input(
        f"Enter a {secret_len} character word: "
    )  # using f-string to simplify concatenation
    while len(word) != secret_len:
        word = input(f"That wasn't {secret_len} chars! Try again: ")
    return word


def contains_char(secret_word: str, guess_char: str) -> bool:
    """Checks if given char of input_word matches any char in secret_word"""
    assert (
        len(guess_char) == 1
    )  # assert would print error message if not 1 char, helps with debugging
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == guess_char:
            return True
        idx += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Return string of emojis characterizing accuracy of guess"""
    assert len(guess) == len(secret_word)  # assert checkpoint
    idx: int = 0
    results: str = ""  # create str var to store emoji boxes
    while idx < len(secret_word):
        if guess[idx] == secret_word[idx]:
            results += GREEN_BOX  # using above defined global constants
        elif contains_char(
            secret_word=secret_word, guess_char=guess[idx]
        ):  # contains_char abstracts this:)
            results += YELLOW_BOX
        else:
            results += WHITE_BOX
        idx += 1
    return results


if __name__ == "__main__":  # using this python idiom
    main(secret_word="codes")
