"""A program that does math to help prepare for a tea party"""

__author__: str = (
    "730722910"  # Remember in the future that author has 2 "_" on each side, not 3!!
)


def main_planner(guests: int) -> None:
    """Bring all subfunctions together to collect and input and output party info"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # Make sure local variable is being carried over into tea_bags
    print("Treats: " + str(treats(people=guests)))  # Same as above
    print(
        "Cost: $"
        + str(  # Must convert into a string for concatenation
            cost(
                tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
            )  # have to call these functions again, because cost() is not based on...
            # ...guests directly, but the number of tea bags and treats
        )
    )


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on guest size"""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on number of tea bags used"""
    return int(
        tea_bags(people=people) * 1.5
    )  # Must restate people=people, because people is a local variable that wouldn't...
    # ...otherwise be carried into tea_bag function


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total price of the party, tea bags and treats combined"""
    return (tea_count * 0.5) + (
        treat_count * 0.75
    )  # Do not need to call other functions here, as those functions with be called...
    # ...in main_planner when assigning parameters values


if __name__ == "__main__":
    """Initiates the main function to plan tea party"""
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # Important to call program at end, after functions have been defined
