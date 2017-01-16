# Author: Kristen Findley
# Date: 16 January 2017
# Description: Drill 48 of 68 - write a sorting algorithm

l1a = [67,45,2,13,1,998]
l1b = []
l2a = [89,23,33,45,10,12,45,45,45]
l2b = []


while len(l1a) > 0:
    l1b.append(min(l1a))
    l1a.pop(l1a.index(min(l1a)))
while len(l2a) > 0:
    l2b.append(min(l2a))
    l2a.pop(l2a.index(min(l2a)))

print(l1b)
print(l2b)

           
