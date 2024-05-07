# Today we are going to create a random password generator using for loops and arrays in python
# Make sure to print you password to the screen
#Can you randomize your password generated

import random
import string 

letters = string.ascii_letters
digits = string.digits
specials = string.punctuation

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
    random_index = random.randint(0, len(specials) - 1)
    password.append(specials[random_index])

# Generating random numbers
for _ in range(nr_numbers):
    random_index = random.randint(0, len(digits) - 1)
    password.append(digits[random_index])

# Shuffling the password to randomize it
random.shuffle(password)

# Joining the characters to form the password string
password = ''.join(password)

print(f"Your random password is: {password}")