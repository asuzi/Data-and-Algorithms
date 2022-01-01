"""
Merge Sort:

If you have two already sorted lists it is very easy to merge them
'Merge sort breaks the list down until it has many lists with only one item in it. (List with only one item is already sorted)
then make sorted lists with 2 items
then make soted lists with 3 items 
When only two lists remain we loop through both of them and append the lower value to new list merged and sorted list.
"""
import random

messyList = []
for _ in range(10):
    messyList.append(random.randint(1,50))

def merge(list1, list2): # Helper function, only use if you have 2 already sorted lists
    """
    List1 and 2 need to be already sorted
    """
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def mergeSort(myList):
    if len(myList) == 1:
        return myList
    mid = int(len(myList)/2)
    left = myList[:mid]
    right = myList[mid:]
    return merge(mergeSort(left), mergeSort(right))

print(messyList)
print(mergeSort(messyList))