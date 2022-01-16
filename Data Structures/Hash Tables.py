"""
Useful for quickly storing (semi- randomly) and accessing data

Common interview question; 
You have two lists and we want to determine does these two lists have an item in common

Bad solution (but works)
1: we can create nested for loop to compare every item in list 1 to list 2 ( if i == j)

Best solution
2: loop first list and make it an dictionary (item is KEY and value is TRUE) (item : True)
Now make a for loop that goes through the second list and look up stuff with getItem method.

def item in common(list2, list1):
    dict = {}
    for i in list1:
        dict[i] = True
    for j in list2:
        if j in dict:
            return True
    return False

"""

class HashTable:
    def __init__(self,size = 7):
        self.dataMap = [None] * size

    def __hash(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 23) % len(self.dataMap)
        return myHash

    def printTable(self):
        for i, val in enumerate(self.dataMap):
            print(i, ":", val)

    def setItem(self, key, value):
        index = self.__hash(key)
        if self.dataMap[index] == None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])

    def getItem(self, key):
        index = self.__hash(key)
        if self.dataMap[index] is not None:
            for i in range(len(self.dataMap[index])):
                if self.dataMap[index][i][0] == key:
                    return self.dataMap[index][i][1]
        return None

    def getKeys(self):
        allkeys = []
        for i in range(len(self.dataMap)):
            if self.dataMap[i] is not None:
                for j in range(len(self.dataMap[i])):
                    allkeys.append(self.dataMap[i][j][0])
        return allkeys
H = HashTable()

H.setItem('bolts', 1400)
H.setItem('washer', 50)
H.setItem('rehsaw', 420)
H.setItem('lumber', 70)
H.printTable()


print(H.getItem('washer'))
print(H.getItem('rehsaw'))
print(H.getKeys())