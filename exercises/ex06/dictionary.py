"""Implementation of dictionary utils for EX06"""

__author__ = "730722910"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and vals of input dictionary"""
    output: dict[str, str] = {}

    # Checks every value in input to see if it matches any other vals, (raise KeyError)
    # Otherwise, when inverting, some vals would be overwritten (no dup keys!)
    for key in input:
        val: str = input[key]
        val_count: int = 0
        for comparison_key in input:
            if input[comparison_key] == val:
                val_count += 1
        if val_count > 1:
            raise KeyError

    # Inverts keys and inputs
    for key in input:
        new_val = key  # this and next line are unnecessary but make it more legible
        new_key = input[key]
        output[new_key] = new_val
    return output


def favorite_color(input: dict[str, str]) -> str:
    """Returns the most popular favorite color from a dictionary of names and colors"""
    top_color: str = ""
    top_count: int = 0

    for current_name in input:
        current_color: str = input[current_name]  # these vars make func more legible
        current_count: int = 0

        for other_name in input:
            other_color: str = input[other_name]
            if (
                other_color == current_color
            ):  # other_color and current_color will always be same at least once
                current_count += 1
        if (
            current_count > top_count
        ):  # top_color only changes if a later color has GREATER count
            top_color = current_color
    return top_color


def count(input: list[str]) -> dict[str, int]:
    """Returns dictionary that displays count for each unique str"""
    count_output: dict[str, int] = {}
    for string in input:
        if string not in count_output:
            count_output[string] = (
                1  # establishes key if it doesn't already exist in the dict
            )
        else:
            count_output[
                string
            ] += 1  # increments count when same string is found again
    return count_output


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Divides words list into a dictionary of lists sorted by first ltr"""
    output: dict[str, list[str]] = {}
    for word in words:
        first_ltr: str = word[
            0
        ].lower()  # lower method returns lower-case version of str
        if first_ltr not in output:
            output[first_ltr] = [word]
        else:
            output[first_ltr].append(word)
    return output


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Update attendance_log to add the student who attended a certain day"""
    if day not in attendance_log:
        attendance_log[day] = [student]  # creates new day key if it doesn't exist yet
    else:
        attendance_log[day].append(student)  # appends student to list
