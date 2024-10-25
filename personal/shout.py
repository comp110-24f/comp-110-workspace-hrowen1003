"""Program to turn anything into a shout"""

lower_alpha: str = "abcdefghijklmnopqrstuvwxyz"
upper_alpha: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shout(input_text: str) -> str:
    i: int = 0
    new_text: str = str()
    while i < len(input_text):
        input_char: str = input_text[i]
        char_i: int = 0
        ltr_found: bool = False
        while char_i < len(upper_alpha):
            if input_char == upper_alpha[char_i] or input_char == lower_alpha[char_i]:
                new_text += upper_alpha[char_i]
                ltr_found = True
            char_i += 1
        if not ltr_found:
            new_text += input_char
        i += 1
    return new_text


print(shout(input("What would you like me to scream? ")))

lst = [1, 2, 3]  # Global object (mutable)
