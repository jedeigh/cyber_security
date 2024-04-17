# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions met or and else when no condition is met.
a = int(input("Enter your first number! "))
b = int(input("Enter your second number! "))

if a == b:
    print("is balanced")
elif a != b:
        if a < b:
            print("b is greater")
        else:
            print("a is greater")

# elif a < b:
#     print("b is greater")
# elif a <= b:
#     print("b could be greater or equal")
# elif a > b:
#     print("a is greater")
# else:
#     print("a could be greater or equal")

# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.

# Create an if statement with two conditions by using or between conditions.

# Create a nested if statement.

# Hint:  a = int(input("Enter a number "))