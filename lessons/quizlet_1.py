"""A Quizlet for Myself"""

__author__ = "730722910"


words: list = ["ankle", "shoulder"]
defins: list = ["just above foot", "next to arm"]


# super_list: list = [words, defins]

# print(super_list)
# print(super_list[0])
# print(super_list[0][0])
# print(super_list[0][0][0])


def main() -> None:
    add_term(
        word=input("What word would you like to add?"),
        defin=input("What is the definition of that term?"),
    )
    print(words)
    print(defins)
    print("You got " + str(round(quiz_user() * 100)) + " percent of the words right.")


def add_term(word: str, defin: str) -> None:
    words.append(word)
    defins.append(defin)


def quiz_user() -> float:
    idx: int = 0
    score: int = 0
    print("I will provide you with the definition of each term, ")
    print("and you should provide the corresponding term.")
    while idx < len(words):
        print("Definition " + str(idx + 1) + ": " + defins[idx])
        if words[idx] == input("Word: "):
            print("Correct!")
            score += 1
        else:
            print("WRONG! The real word was " + words[idx])
        idx += 1
    return score / len(words)


if __name__ == "__main__":
    ask: str = input("Would you like to play? (Y/N)")
    if "Y" == ask:
        main()
    elif "N" == ask:
        print("ok")
    else:
        ask = input("Please either type 'Y' or 'N'")
