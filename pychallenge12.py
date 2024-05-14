# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments
import time 
import random 


yes_no = ["yes", "no"]
directions = ["north", "south", "east", "west"]
 
# Introduction
print("Welcome to the Path of the Brave!")
time.sleep(2)
name = input("What is your name, adventurer?\n")
time.sleep(1)
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself at a portal of possiblites which fate will you chose?")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into this portal?\nyes/no\n")
    if response == "yes":
        print("You walk through the portal to travel to a distant land. Where you go who knows.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while True:
    print("Please choose the direction you choose to walk on this path...")
    time.sleep(2)
    response = input("north, south, east, west")
    if response == "north":
        print("Scandinavia (Denmark, Norway, Sweden, Finland, Iceland): \n Known for their high quality of life, social welfare systems, and stunning natural landscapes.")
        challengeN = input("You are approached by a Viking, do you run or stand your ground")
        if challengeN == 'stand':
            print("He just wants you to guess how many push ups he can do...")
            #more code here
        else: print("You've lost heart, game over!")
        quit()
    elif response == "south":
        print("This path leads to the land down under Australia: \n Known for its vast landscapes, unique wildlife, and vibrant cities like Sydney and Melbourne.")
        challengeS = input("Watch an angry kangroo is on the run and charging at you, run or stand your ground?")
        if challengeS == 'stand':
            print("The wild beast attacks!")
            #more code here
        else: print("Running was actually the smart move, live to see another day")
        #more code here
    elif response == "east":
        print("Welcome to Egypt: Famous for its ancient civilization, \n including the pyramids and Sphinx, as well as its rich cultural heritage.")
        challengeE = input("You are inside the pyramid next to the tomb of the Great Pharaoh, will you open it yes or no? ")
        if challengeE == 'yes':
            print("The mummy rises from the dead and curses you, game over!")
            quit()
        else: print("Would you like to explore the pyramid more instead?")
        #more code
    else:print("Hola Mexico: Renowned for its rich history, vibrant culture, and delicious cuisine, including tacos and tequila.")
    challengeW = input("You arrived just in time for the Day of the DEAD, there's a ceromony at a local cemetery, shall you go?")
    if challengeW == 'yes':
        #more code
    else: print("ok")
