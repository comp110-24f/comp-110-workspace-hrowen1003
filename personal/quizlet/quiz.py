"""File to quiz the user on whatever term set they choose"""

import time
import os
from personal.quizlet.shuffle import shuffle_dict


def quiz(term_set: dict[str, str]) -> None:
    time.sleep(0.5)
    os.system("clear")
    print("Beginning quiz!")
    print("The terms will be shuffled")
    print("You will be retested on any you get wrong in future rounds")
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
        for wrd in shuffled_terms:
            print("<----========---->")
            if input(f"{wrd}: ") == shuffled_terms[wrd]:
                score += 1
                print("Correct!")
            else:
                print("Incorrect.")
                next_round_terms[wrd] = current_round_terms[wrd]
        print("<----========---->")
        print(f"You got {score} out of {len(shuffled_terms)} terms correct")
        print(f"That's about {round((score/len(shuffled_terms)) * 100)}% correct")
        if score < len(shuffled_terms) and len(shuffled_terms) != 0:
            cont_choice: "str" = input(
                "Would you like to continue with the terms you got wrong? (y/n) "
            )
            if cont_choice == "n":
                playing = False
