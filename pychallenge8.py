# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:

counter = 1

for i in range(1,6):
    print(f"{counter} mississippi!")
    counter += 1
    
print("Ready or not, Here I come, You can't hide!")
