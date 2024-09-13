"""Practice with Conditionals"""


def less_than_ten(num: int) -> None:
    """tell me if num <10"""
    if num < 10:
        print("Small Number!")
    else:
        print("Big Number!")
    print("Have a nice day")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:  # conditional/boolean expression
        print("Eat some food, stupid")  # 'then' block
    else:
        print("No food right now, bud")  # "else" block
    print(
        "Why did you need a program to help you figure that out???"
    )  # reevaulate how you should spend your coding time


def check_first_letter(word: str, letter: str) -> str:
    """Checks if the first letter of word matches the input letter"""
    if word[0] == letter:  # conditional/boolean expression
        return "match!"  # 'then' block
    else:
        return "no match!"  # 'else" block


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))

age = 18
print(age)
