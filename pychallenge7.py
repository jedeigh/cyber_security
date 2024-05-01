import random 
# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
counter = 3
bobs_num = random.randrange(1,20)
print(f"Let's play a number guess game, you have {counter} tries \n to pick the correct number ranges (1-20) \n Good Luck!")

# Rule 2: Program must run until the correct number is guessed
guessed = False 
for wrong_guess in range(1, counter + 1):
    counter -=1 
    play_num = int(input('Guess my number friend '))
    if play_num > bobs_num:
        print("You're number is too high, try again!")
        continue
    if play_num < bobs_num:
        print("You're number is too low, try again!")
        continue
    else:
        play_num == bobs_num 
        guessed = True
        print(f"You got it, my number was {bobs_num} and it only took you {3 - counter} tries!")
        break 
else:
    print(f"You reached your maximum limit of guesses with {counter}, the correct number was {bobs_num} game over!")
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?