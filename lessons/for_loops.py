"""Testing out for loops"""

greet: list[str] = ["Hi", "Johnny", "Buddy"]
w: str = "abc123"

# for x in greet:
#   for y in x:
#  print(y)


# new_greet: list[str] = list()

# for x in greet:
# new_greet.append(x)

# print(new_greet)

pets: list[str] = ["Louie", "Bo", "Bear"]


def good_boy(pets: list[str]) -> None:
    for name in pets:
        print(f"Good boy, {name}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(idx)
    print(names[idx])
