import random 
import time 

# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:


game_ops = ['rock', 'paper', 'sza']
cpu_choice = random.choice(game_ops)
player_choice = ''

print("Let's play Rock, Paper, SZA")
time.sleep(1)
game_q = input("Do you want to play, y/n?")

if game_q == 'yes' or game_q == 'y':  
    print("Great Let's Begin...")
    time.sleep(1)
    print("Best 2 out of 3!")
    print('Rock')
    time.sleep(1)
    print('Paper')
    time.sleep(1)
    print('SZA... GO!!!')
    time.sleep(1)
    for i in game_ops:
        player_choice = input()
        if player_choice == 'rock' and cpu_choice == 'paper':
            print("You lose, smh!")
        if player_choice == 'rock' and cpu_choice == 'sza':
            print("You win, haha!")
        if player_choice == 'paper' and cpu_choice == 'rock':
            print("You win, smh!")
        if player_choice == 'paper' and cpu_choice == 'sza':
            print("I win, haha!")
        if player_choice == 'sza' and cpu_choice == 'paper':
            print("You win, smh!")
        if player_choice == 'sza' and cpu_choice == 'rock':
            print("I win, haha!")
        if player_choice == cpu_choice:
            print("we're tied!")
else: 
    print("Darn it, You were about to get that work...")
    time.sleep(1)
    print("Bye scary cat!")

    
        
        

        