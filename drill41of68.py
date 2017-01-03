# Python 2.7.12
# 
# Author: Kristen Findley
# 
# Purpose: Create a program to see how many days, minutes, and seconds
#          a person has lived print("Lets see how long you have lived in days, minutes, and seconds.")



name = input('name: ')
print('Now enter your age')
age = input("age: ")
print("Now enter what time you were born")
days = age * 365
minutes = age * 365 * 24 * 60
seconds = age * 365 * 24 * 60 * 60
print(name, ", you have been alive for ", day, " days, ", minutes, " minutes, and ", seconds, " seconds!")
