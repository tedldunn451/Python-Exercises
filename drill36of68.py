# Python 2.7.12
# 
# Author: Kristen Findley
# 
# Purpose: Python course drill 36 of 68

# 1) Assign an integer to a variable
integer = 5

# 2) Assign a string to a variable
string = 'Big Bear Lake'

# 3) Assign a float to a variable
floatNumber = 7.82

# 4) Use the print function and .format() notation
print('{0} is at an elevation of {1} ft'.format('Big Bear Lake', 7000))

# 5) Use the following operators +, -, *, /, +=, =, %
additionEx = 8 + 2
print(additionEx)
subtractionEx = 8 - 2
print(subtractionEx)
multEx = 8 * 2
print(multEx)
divisionEx = 8 / 2
print(divisionEx)

addOne = 1
print(addOne) # equals 1
addOne += addOne
print(addOne) # equals 1 + 1

remainder = 7 % 3
print(remainder)

# 6) Use logical operators and, or, and not
x = raw_input("Enter your age: ")
y = raw_input("Are you belay-certified? y/n: ")
if x >= 18 and y == 'y':
    print ("You may climb in the expert area.")
elif x >= 18 or y == 'y':
    print ("You may climb in the intermediate area.")
else:
    print ("You may climb only in the beginner area.")

name = raw_input("What is your name?: ")
if name != "Kristen":
    print ("You do not have the same name as me.")
else:
    print ("You have the same name as me!")

# 7) Use if, elif, and else - see example 6)

# 8) Use a while loop
distance = 3000
while distance > 400:
    print ("You have {} m to go".format(distance))
    distance = distance - 400

# 9-10) Create a list and use a for loop to iterate through the list and print specific information
events = [200,400,800,1600,5000,10000]
for race in events:
    if race >= 800 and race < 10000:
        print('Kristen races the {} m run'.format(race)) 

# 11) create a tuple and iterate through it to print each item
places_lived = ('Boise','Dhahran','Ojai','Nashville','Austin','Portland')
for city in places_lived:
    print (city)

# 12-13) define a function that returns a string variable
'''Type the following into the command prompt:

    >>>def ex12():
    flavor = raw_input("What is the best flavor of ice cream?: ")
    return flavor
    >>>ex12()

'''
