# Version: Python 3.5.2
# Author: Kristen Findley
# Date: 06 January, 2017
# Purpose: Python Drill 41 of 68 (Total days/minutes/seconds you have been alive)

print("Let's see how long you have lived in days, minutes, and seconds.")
name = input("Name: ")
print("Now enter your age.")
age = int(input("Age: ")) 
days = age*365
minutes = days*24*60
seconds = minutes*60
print(name, ", you have been alive for ", days, " days or ", minutes, " minutes or ", seconds, " seconds!")
