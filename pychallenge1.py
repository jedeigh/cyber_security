# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
# Jedeigh
# Soul Food
# Creator
# assign 5 different data types to 5 different variables. At least one datatype must be a string.
a = 3.5
bool = True
c = "cat"
d = 9
e = a

# print the length of your string.
print (len(c))
print (e)

# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"
savvy = "Learning Python is Awesome"


# Replace "Awesome" with "great" in the string
newsav = savvy.replace ("Awesome", "great")
print (newsav)


# Create and assign 3 more variables called name, age and length using the multi-variable naming method.
name, age, tall = "J", 38, 5.9



# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."
miniBio = f"Hi my name is {name}, I am {tall} and {age} old today"
print (miniBio)

# Create a list of at least 5 elements of mixed data types
l1 = ["hi", 8, .5, "time", name]
print (l1)

# replace a part of it with something else
l1[0] = "bye"
print (l1)
# append or insert several more items to the list
l1.append(age)
# find and print the length of the list
print (len(l1))
# slice a sub-section of the 1st list, and save it to a different 2nd list
l2 = l1[0:2]
# print the 2nd list
print (l2)
# extend your original list with the 2nd list sliced above
l1.append(l2)
print (l1)
# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.
simlist = [1,0,9,4,5]
# sort "simList", and print the list
simlist.sort()
print (simlist)
# copy the "simList" list to another 3rd list
l3 = simlist.copy()
print (l3)
# add the 2nd and 3rd lists together into a 4th list
l4 = simlist + l3
print (l4)