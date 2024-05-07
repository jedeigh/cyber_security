# Today we are going to create a random password generator using for loops and arrays in python
# Make sure to print you password to the screen
#Can you randomize your password generated

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# What is line 15 doing?
password = []
# Below is the guide how to write the for loop you need to write for symbols and numbers
# Generating random letters
for _ in range(nr_letters):
    random_index = random.randint(0, len(letters) - 1)
    password.append(letters[random_index])

# Generating random symbols
for _ in range(nr_symbols):
    random_index = random.randint(0, len(symbols) - 1)
    password.append(symbols[random_index])

# Generating random numbers
for _ in range(nr_numbers):
    random_index = random.randint(0, len(numbers) - 1)
    password.append(numbers[random_index])

# Shuffling the password to randomize it
random.shuffle(password)

# Joining the characters to form the password string
password = ''.join(password)

print(f"Your random password is: {password}")