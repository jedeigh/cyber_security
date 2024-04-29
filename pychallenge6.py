import random 
# Scenario
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number.
#  He wants everyone who runs his program to play the Guess the secret number game,
#  and guess what number he has picked for them.
#  Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
num_vault = [0,1,2,3,4,5,6,7,8,9]
secret_num = random.choice(num_vault)
# Your task is to help the magician complete the code in the editor in such a way so that the code:
# will ask the user to enter an integer number;
user = int(input('Please Enter a number 0-9: '))
# will use a while loop;
while user != secret_num:
    print("Ha ha! You're stuck in my loop!")
    user = int(input('Try again, pick another number: '))
    if user == secret_num:
        print("Well done, muggle! You are free now.")

# will check whether the number entered by the user is the same as the number picked by the magician.
# If the number chosen by the user is different than the magician's secret number, the user should see
# the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again.
# If the number entered by the user matches the number picked by the magician, the number should be printed to the screen,
# and the magician should say the following words: "Well done, muggle! You are free now."
# The magician is counting on you! Don't disappoint him