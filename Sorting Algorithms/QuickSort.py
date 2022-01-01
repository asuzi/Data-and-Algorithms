"""
Compare everything to the pivot point and seperate items (less than goes left) orthers go right
(Pivot point initially is the first item) (when we start seperating MessyList in peaces we use first item as the pivot)
next we move pivot point behind all less thans (it is now sorted)
then we run quick sort on the items on left and on items on right (PIVOT IS AT THE MIDDLE AND SORTED)
"""
import random
MessyList = []
for i in range(10):
    MessyList.append(random.randint(0,50))

# Swap is a helper function for pivot
def swap(myList, index1, index2):
    temp = myList[index1]
    myList[index1] = myList[index2]
    myList[index2] = temp

#Pivot is only a helper function for QuickSort
def pivot(myList, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        if myList[i] < myList[pivotIndex]:
            swapIndex += 1
            swap(myList, swapIndex, i)
    swap(myList, pivotIndex, swapIndex)
    return swapIndex #Returns the index NOT the value

def quickSort_helper(myList, left, right): #actual quick sortin happens here
    if left < right:
        pivotIndex = pivot(myList, left, right)
        quickSort_helper(myList, left, pivotIndex-1)
        quickSort_helper(myList, pivotIndex+1, right)
    return myList

def quickSort(myList): # this is just so its easier to call your function
    return quickSort_helper(myList, 0, len(myList)-1)

print(MessyList)
print(quickSort(MessyList)) 



