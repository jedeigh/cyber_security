import math
# Here is a short story:

# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. 
#They were all very happy and lived for a long time. End of story.

# Your task is to:

# create the variables: john, mary, and adam;
john = 3
mary = 5
adam = 6
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
print(john, mary, adam)
# now create a new variable named total_apples equal to the addition of the three previous variables.
total_apples = john + mary + adam
print("Total apples are: ",total_apples)
# print the value stored in total_apples to the console;
# experiment with your code: create new variables, assign different values to them, and perform 
#various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an 
less_apples = adam - mary - john 
print("subtracting all the apples will leave you with", less_apples,"apples") 
apple_pi = adam * mary * john * math.pi  
print("multipling all apples times pi will give you", apple_pi,"apples") 
#integer together on one line, e.g., "Total number of apples:" and total_apples.