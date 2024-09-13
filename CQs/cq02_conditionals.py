"""Challenge Question 2: Comparing a guess to secret number"""

__author__ = str(730722910)


def guess_a_number() -> None:
    """Create a secret number and compare it to user's guess"""
    secret: int = 7  # Define local variable "secret" and set initial value
    guess: int = int(
        input("Guess a number: ")
    )  # User input is a str, but must be converted to int for comparison
    print("Your guess was " + str(guess))  # Convert back to str for concatenation
    if secret == guess:
        print("You got it!")
    elif secret > guess:
        print("Your guess was too low! The secret number is " + str(secret))
    elif (
        secret < guess
    ):  # Given above if/elif statements, this line could also function with "else"
        print("Your guess was too high! The secret number is " + str(secret))
    return None  # This line is not necessary, but also doesn't harm functionality


if __name__ == "__main__":
    guess_a_number()  # Calling guess_a_number
