import random
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#Import the random module
#Split string method 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# :rotating_light: Don't change the code above :point_up_2:

#Write your code below this line :point_down:
for n in names_string:
    print("Time to pay the bill, \nlet's see who pays by spinning the butter knife on the table!")
    response = input("Do y'all want to play? y/n? ")
    if response == 'yes' or response == 'y':
        print(f"The person paying the bill today will be {random.choice(names)}.")
        break 
    else: print("ok fine let's just do split checks!")
    break 

        