# Author: Kristen Findley
# Date: 16 January 2017
# Description: Drill 48 of 68 - write a sorting algorithm

lraw = input('Please enter a list of numbers separated by commas: ')
l1a =  list(map(int,lraw.split(',')))
l1b = []

while len(l1a) > 0:
    l1b.append(min(l1a))
    l1a.pop(l1a.index(min(l1a)))
    
print(l1b)
           
