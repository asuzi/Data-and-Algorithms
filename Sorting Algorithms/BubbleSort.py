"""
Bubble Sort:

Starts with the first item on the list and going to
Compare it to the next item.
If first item is bigger than the next one we're going to
move it left and keep going
"""
import random

messyList = []
for i in range(10):
    messyList.append(random.randint(1,50))

def BubbleSort(myList):
    for i in range(len(myList)-1,0,-1):
        for j in range(i):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
    return myList

print(messyList)
print(BubbleSort(messyList))