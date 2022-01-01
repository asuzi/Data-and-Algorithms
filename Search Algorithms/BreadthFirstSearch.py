"""
BFS - Search Method
Go through a tree layer by layer.
"""
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

####### Start of BFS
    def BFS(self):
        currentNode = self.root
        queue = [] #list is not an ideal queue! use queue I have created earlier
        visited = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            visited.append(currentNode.value)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

        return visited

TestTree = BinarySearchTree()

for _ in range(10):
    TestTree.insert(random.randint(0,1000))

print(TestTree.BFS())