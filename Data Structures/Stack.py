"""
Stack can be implemented in many different ways,
it can be implemented as a list (remove last index + add last index)
or as a linked list (remove first index + add first index)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        #self.bot = new_node 'this will be useful for queue and priority queue NOT for stack'
        self.length = 1

    def printStack(self): #prints stack one by one
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp


S = Stack(0)
S.push(1)
S.push(2)
S.push(3)
S.pop()
S.printStack()



