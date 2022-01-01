"""
Insertion Sort:

Always start from second item and compare it to item before it.
If its less than the one it was compared to they switch places.
"""
import random

messyList = []
for i in range(10):
    messyList.append(random.randint(1,50))

def InsertionSort(myList):
    for i in range(1, len(myList)):
        temp = myList[i]
        j = i-1
        while temp < myList[j] and j > -1:
            myList[j+1] = myList[j]
            myList[j] = temp
            j -= 1
    return myList

print(messyList)
print(InsertionSort(messyList))