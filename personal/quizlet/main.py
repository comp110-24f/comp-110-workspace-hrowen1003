"""Second Attempt at creating quizlet"""

__author__ = "730722910"

from personal.quizlet.welcome_scr import titleify
from personal.quizlet.input_trm import initiate_input, new_terms
from personal.quizlet.preload_terms import (
    set_name_catalog,
    org_terms,
    astr_terms,
)
from personal.quizlet.quiz import quiz

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
    explain_set_choice()
    pick_term_set()
    return None


def explain_set_choice() -> None:
    print("Welcome, user!\nCurrently you have the following term sets pre-loaded:")
    print("=====================================")
    for set_name in set_name_catalog:
        print(set_name)
    print("=====================================")
    print(
        "If you would like to test yourself on one of these term sets, type it's name."
    )
    print("Otherwise, simply type 'input' if you would like to create your own set")


def find_preload_set(set_choice: str) -> dict[str, str]:
    """If user choses a preload set, this finds the dictionary for that set"""
    # I know this would be better as a loop somehow, but I can't figure out how to turn
    # the user input str into calling a variable (in this case a dictionary)
    if set_choice == "org_terms":
        return org_terms
    if set_choice == "astr_terms":
        return astr_terms
    else:
        return (
            dict()
        )  # pick_term_set already checked that input was valid, but this line exists
        # to avoid VS Code yelling at me
    # if you add more preload terms sets, add if statements here!!!


def pick_term_set() -> None:
    choice_made: bool = False
    while not choice_made:
        set_choice = input("What would you like to do? ")
        for term_set in set_name_catalog:
            if set_choice == term_set:
                choice_made = True
                print(f"You chose {set_choice}")
                quiz(find_preload_set(set_choice))
        if not choice_made and set_choice == "input":
            choice_made = True
            initiate_input()
            while input("Would you like to add any more terms? (y/n) ") == "y":
                initiate_input()
            quiz(new_terms)
        elif not choice_made:
            print(
                "I do not understand. Please type either 'input' or the name of a set"
            )


if __name__ == "__main__":
    main()
