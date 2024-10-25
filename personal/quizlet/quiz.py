"""File to quiz the user on whatever term set they choose"""

import time
import os
from personal.quizlet.shuffle import shuffle_dict


def clear_screen() -> None:
    os.system("clear")


def writing_mode_quiz(term_set: dict[str, str]) -> None:
    """quizes users on correct spellings of definitions"""
    shuffled_terms: dict[str, str] = shuffle_dict(term_set)
    next_round_terms: dict[str, str] = {}
    playing: bool = True
    while playing:
        score: int = 0
        current_round_terms: dict[str, str] = {}
        if len(next_round_terms) != 0:
            current_round_terms = next_round_terms
        else:
            current_round_terms = shuffled_terms
        next_round_terms: dict[str, str] = {}  # reset next_round_terms to be blank
        clear_screen()
        for wrd in current_round_terms:
            print("<----========---->")
            if input(f"{wrd}: ") == current_round_terms[wrd]:
                score += 1
                print("\U0001F389 Correct! \U0001F389")
            else:
                print("Incorrect.")
                print(f"The correct definition was: '{current_round_terms[wrd]}'")
                next_round_terms[wrd] = current_round_terms[wrd]
        print("<----========---->")
        print(f"You got {score} out of {len(current_round_terms)} term(s) correct")
        print(f"That's about {round((score/len(current_round_terms)) * 100)}% correct")
        if score < len(current_round_terms) and len(current_round_terms) != 0:
            cont_choice: "str" = input(
                "Would you like to continue with the terms you got wrong? (y/n) "
            )
            if cont_choice == "n":
                playing = False
        elif score == len(current_round_terms):
            playing = False


def flash_mode_quiz(term_set: dict[str, str]) -> None:
    """conducts flashcard-mode quizing"""
    shuffled_terms: dict[str, str] = shuffle_dict(term_set)
    next_round_terms: dict[str, str] = {}
    playing: bool = True
    while playing:
        score: int = 0
        current_round_terms: dict[str, str] = {}
        if len(next_round_terms) != 0:
            current_round_terms = next_round_terms
        else:
            current_round_terms = shuffled_terms
        next_round_terms: dict[str, str] = {}  # reset next_round_terms to be blank
        clear_screen()
        for wrd in current_round_terms:
            print(f"<----========---->\nTerm: {wrd}")
            input("Hit enter to flip card")
            print(f"Definition: '{current_round_terms[wrd]}'")
            if input("Type 'y' if you got it right: ") == "y":
                score += 1
                print("\U0001F389 Congrats! \U0001F389")
            else:
                print("Better luck next round")
                next_round_terms[wrd] = current_round_terms[wrd]
        print("<----========---->")
        print(f"You got {score} out of {len(current_round_terms)} term(s) correct")
        print(f"That's about {round((score/len(current_round_terms)) * 100)}% correct")
        if score < len(current_round_terms) and len(current_round_terms) != 0:
            cont_choice: "str" = input(
                "Would you like to continue with the terms you got wrong? (y/n) "
            )
            if cont_choice == "n":
                playing = False
        elif score == len(current_round_terms):
            playing = False


def quiz(term_set: dict[str, str]) -> None:
    """main function for running quiz of terms"""
    time.sleep(0.5)
    clear_screen()
    print("Beginning quiz!")
    print("The terms will be shuffled")
    print("You will be retested on any you get wrong in future rounds\n")
    mode: str = input("Flashcard Mode or Writing Mode? (flash/writing): ")
    mode_valid: bool = True
    if mode != "flash" and mode != "writing":
        mode_valid = False
    while not mode_valid:  # FIX BUG I HAVE HERE HERE
        if mode != "flash" and mode != "writing":
            mode = input("I don't understand. Please type 'flash' or 'writing': ")
        else:
            mode_valid = True
    if mode == "flash":
        flash_mode_quiz(term_set)
    if mode == "writing":
        writing_mode_quiz(term_set)
