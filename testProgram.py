x = 10
y = 2

# this is a one line comment
'''this is a multi
line comment '''

print(x+y)

if x == 10:
    print 'x = 10'

name = "kristen rose"
print name[0] # print the character in the first index
print name.upper() # make all upper case
print name.capitalize() # capitalize first letter of the string
print name.title() # capitalizes the first letter of every word in the string
print name.swapcase() # swaps the case of every letter in the string
print name.strip() # removes all white space from within string

date = "12/10/2016"
date_manip = date.split('/') # go through string and split where '/' occurs
print date_manip
month = date_manip[0]
day = date_manip[1]
year = date_manip[2]
print 'month: ' + month
print 'day: ' + day
print 'year: ' + year

a = 5
print a == 5 # returns True
print a == 4 # returns False
print a < 7 # returns True
print a > 7 # returns False
print a != 3 # returns True
print a >= 5 # returns True
print a <= 5 # returns True
print a > 5 # returns False

# if statement example
'''if (condition 1):
        statements run if condition 1 is true
   elif (condition 2):
        statements run if condition 2 is true
   else:
        statements run if neither condition 1 nor condition 2 are true'''
if x == 10:
    print 'x = 10'
elif x == 9:
    print 'x = 9'
else:
    print 'x does not equal 9 or 10'

# while loop example (press ctl-C to stop infinite loops)
counter = 0
while counter < 5:
    print counter
    counter = counter + 1 # you could also use counter += counter to achieve the same thing

# for loop example
for counter in range(0,5):
    print counter

# making a list
nameOfList = ["item1", "item2", "item3", "item4"]
print "List item 1: " + nameOfList[0]

# changing a list
nameOfList[2] = "itemC"
nameOfList.append("item5")

# looping through lists
for listItem in nameOfList:
    print "Item Listing: "  + listItem

# looping through lists with numbers
originalNumberList = [1,2,3,4,5]
finalNumberList = []
for x in originalNumberList:
    finalNumberList.append(x**2)
print finalNumberList

# dictionaries
kfinsDictionary = {'age':26,'favorite color':'purple','favorite country':'New Zealand'}
print kfinsDictionary
print kfinsDictionary['age']
# to add to dictionary
kfinsDictionary['middle name']='Rose'
# delete from a dictionary
del kfinsDictionary['favorite country']

# functions
'''def funkyDuck(<input variables>): # structure
    <statements>
    return <output values>'''
# example
def letsAdd(x,y):
    addition = x+y
    return addition
print letsAdd(3,5)
# example 2
def letsDivide(x,y):
    divide = float(x)/float(y)
    return divide

# built-in functions
len('name') # returns length of arguement
str(57) # converts arguement into a string
float(38) # converts arguement to a decimal number
int(20.2) # converts arguement into an integer
round(20.2) # rounds the arguement to the nearest number

# modules (a module is a collection of functions that can be imported for use in a script)
import math
print math.sqrt(16)
# or...
from math import sqrt, exp # this allows the use of the sqrt and exp without having to import all the other functions included in the math module

# creating a module
'''save a new file called smallMathsModule.py with the following code
from random import randint
def multiplyBy5(x):
    return 5 * x
def add5(x):
    return 5 + x
def randomAdd(x):
    y = randint(0,10)
    return x + y
now create a new script located in the same folder as the smallMathsModule.y
import smallMathsModule
print smallMathsModule.multiplyBy5(3) # applies the muliplyBy5 from within the smallMathsModule
print smallMathsModule.add5(9) # applies the add5 from within the smallMathsModule
print smallMathsModule.randomAdd(6) # applies the randomAdd from within the smallMathsModule'''

# creating a program
coaches = {'ian wilson':['Dhahran Wellness','Dhahran, Saudi Arabia','middle school'],'derick perry':['The Thacher School','Ojai, CA','high school'],'steve keith':['Vanderbilt University','Nashville, TN','collegiate'],'steve sisson':['Rogue Athletic Club','Austin, TX','post-collegiate'],'mike hickey':['Athletics Northwest','Portland, OR','post-collegiate'],'jonathan marcus':['High Performance West','Portland, OR','post-collegiate']}
def KFinsCoaches(coachsName):
    try:
        coachsInfo = coaches[coachsName]
        print 'Team: ' + coachsInfo[0]
        print 'Location: ' + coachsInfo[1]
        print 'Level: ' + coachsInfo[2]
    except:
        print 'No info found for that Coach.'
continueLoop = True
while continueLoop == True:
    coachsName = raw_input('Please enter a name: ').lower()
    KFinsCoaches(coachsName)
    continueLoop = False
    searchAgain = raw_input('Search again? (y/n)')
    if searchAgain == 'y':
        continueLoop = True
    elif searchAgain == 'n':
        continueLoop = False
    else:
        print 'That was not an option.'
        continueLoop = False
