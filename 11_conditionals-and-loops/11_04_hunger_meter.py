# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.


hunger = 2

if isinstance(hunger, str):
    print("great your hunger is a string")
else:
    print("Please declare your hunger level with a string")
