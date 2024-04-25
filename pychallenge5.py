# Write a program that works out whether if a given number is an 
# odd or even number
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
try:
    num = int(input("Please Enter a number: "))
    if num % 2 == 0:
        print("Your number is even!")
    else:
       print("Your number is odd!")
except ValueError:
    print("Invaild input, you did not enter a number!")


# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:


# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x = ((90 * 365) - (age * 365))
y = ((90 * 53)  - (age * 52))
z = ((90 * 12)  - (age * 12))
print(f"You have {x} days, {y} weeks & {z} months left until you turn 90")