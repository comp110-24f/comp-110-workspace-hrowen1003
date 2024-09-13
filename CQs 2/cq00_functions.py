"""This is my first Challenge Question"""

__author__ = "730722910"


def mimic(message: str) -> str:
    """returns the input"""
    return message


def main() -> None:
    """main function; runs mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
