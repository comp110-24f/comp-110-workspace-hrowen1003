"""Second Attempt at creating quizlet"""

__author__ = "730722910"

from personal.quizlet.welcome_scr import titleify
from personal.quizlet.input_trm import initiate_input

# =====Notes on intended purposes & possible abstractions:====
# 1. Feature to quiz user
# 2.store the answers they got wrong for future rounds
# 3. Ideally feature to story input values in an external file
# 4.function to turn a long input seperated by commas into a list of defs/words
# 5. function to grade user
# 6. function to edit existing lists of defs/words after being created
# 7. make it look pretty :)


def main() -> None:
    titleify()
    initiate_input()
    while input("Would you like to add any more terms? (y/n) ") == "y":
        initiate_input()
    # URGENT: I need to have stuff in input_trm.py have a return value of some sort,
    # that way i can save those list in main too
    # Ask for Input
    # Ask to Quiz
    return None


if __name__ == "__main__":
    main()
