"""
Trees:
Parent node -> child node
child nodes can also be parents
Node with no children nodes is called leaf

Binary Search Tree = if number is greater than ROOT it goes to right side, otherwise it goes to the left side.
The same pattern repeats until it reaches the bottom. (next node -> if bigger go right side else: go left side)

n = number of layers (only full layers ) in Binary Search Tree (BST)
calculate size (2 ** n - 1)
BIG O FOR BST = (log n)


"""
import random

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.depth = 0
        self.size = 0

    def sizeAndDepth(self):
        if self.root is not None:
            self.depth += 1
        temp = self.root
        while temp is not None:
            temp = temp.right
            self.depth += 1
        print("This many nodes: ", self.size , " This deep: ", self.depth, "(!! DEPTH IS NOT ACCURATE BUT GIVES SOME IDEA THAT AT LEAST THE BST IS WORKING !!") 

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.size += 1
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    self.size += 1
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    self.size += 1
                    return True
                temp = temp.right

    def contain(self,value):
        steps = 0
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
                steps += 1
            elif value > temp.value:
                temp = temp.right
                steps += 1
            else:
                print("Found it! It took me ",steps, " steps.")
                return True
        return False

    def minValue(self, start):
        if self.root is None:
            return None
        while start.left is not None:
            start = start.left
        return start

    def maxValue(self, start):
        if self.root is None:
            return None
        while start.right is not None:
            start = start.right
        return start


BST = BinarySearchTree()

BST.insert((50)) # MAKE n ROOT
for _ in range(10): # 50 RANDOM NUMBERS
    BST.insert(random.randint(0,100))

BST.sizeAndDepth() #The amount of nodes might differ since duplicate values are not allowed.

print(BST.contain(49)) # RETURNS TRUE IF GIVEN VALUE IS IN THE BINARY SEARCH TREE

# YOU CAN CHOOSE DIFFERENT SUBTREES SO YOU DONT HAVE TO START FROM THE ROOT.
print(BST.minValue(BST.root.right))
print(BST.maxValue(BST.root.left))


