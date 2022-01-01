"""
Selection Sort:

Keep track of index with smallest value (minIndex)
Then compare next index value to the minIndex
"""
import random

messyList = []
for i in range(10):
    messyList.append(random.randint(1,50))

def SelectionSort(myList):
    for i in range(len(myList)-1):
        minIndex = i
        for j in range(i+1, len(myList)):
            if myList[j] < myList[minIndex]:
                minIndex = j
        if i != minIndex:
            temp = myList[i]
            myList[i] = myList[minIndex]
            myList[minIndex] = temp
    return myList

print(messyList)
print(SelectionSort(messyList))