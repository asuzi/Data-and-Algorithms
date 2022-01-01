"""
DFS: PreOrder:
Why? : Starts from the root and keeps going left when reach bottom backtrack and get subnodes on right side
Always checks node to the left first

DFS: PostOrder:
Why? : Starts from bottom left node working its way towards the root adn then on the right side
always check right and left if no nodes append to visited the node. 
if visited both left and right append to visited the node node

DFS: InOrder:
Why? :  Starts from bottom left node and if there is nothing left append value to visited, then check right 
if none go back and append parent value and check again if nodes on right side
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

################# start of DFS
    def DFS_PreOrder(self):
        visited = []

        def traverse(currentNode):
            visited.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)

        traverse(self.root)
        return visited

    def DFS_PostOrder(self):
        visited = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            visited.append(currentNode.value)

        traverse(self.root)
        return visited

    def DFS_InOrder(self):
        visited = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            visited.append(currentNode.value)
            if currentNode.right is not None:
                traverse(currentNode.right)

        traverse(self.root)
        return visited

TestTree = BinarySearchTree()

for _ in range(10):
    TestTree.insert(random.randint(0,100))

print(TestTree.DFS_PreOrder())
print(TestTree.DFS_PostOrder())
print(TestTree.DFS_InOrder())