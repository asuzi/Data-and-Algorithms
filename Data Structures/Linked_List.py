import random

"""
NOTES:

"""



""" Creates nodes, can add functions for the node if needed """
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

""" Linked list """
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self): #prints list one by one
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value): #append to the end
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value): #append to the beginning
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):  # remove last item
        if self.length == 0:    #if linked list is empty do nothing
            return None
        
        temp = self.head        #this part does the actual popping
        pre = self.head
        while temp.next is not None: #while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:    #if we removed all from linkedlist we need to fix head and tail
            self.head = None
            self.tail = None
            
        return temp

    def popFirst(self):  # remove first item
        if self.length == 0:    #if linked list is empty do nothing
            return None
        
        temp = self.head        #this part does the actual popping
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:    #if we removed all from linkedlist we need to fix head and tail
            self.tail = None
            
        return temp

    def get(self, index):   #returns item based on its index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def setValue(self, index, value):   #change node value in index
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True                 #return True or False based on if value was succesfully changed
        return False                    #True = YES & False = NO

    def insert(self, index, value): #insert node into specific index MUST RETURN TRUE OR FALSE
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value) #has their own True or False
        if index == self.length:
            return self.append(value) #has their own True or False

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):        # remove item from index
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        # head moves one to right
        if index == self.length - 1:
            return self.pop()
        # tail moves one to left

        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):  #REVERSES the linked list ( IMPORTANT LOOP )
        temp = self.head
        self.head = self.tail
        self.tail = temp
        tempRight = temp.next
        tempLeft = None

        for _ in range(self.length):
            tempRight = temp.next
            temp.next = tempLeft
            tempLeft = temp
            temp = tempRight


l = LinkedList(1)   #Creates the LinkedList !MUST DO!
l.append(420)       #appends an item into the LinkedList
for i in range(3):
    l.append(i + random.randint(1,101))
l.append(2000)
l.pop()             #removes the last item from LinkedList
l.prepend(15)
l.popFirst()
l.print_list()      #prints out the LinkedList
print(l.get(1))
l.setValue(1,99999)
l.insert(5,590)
l.remove(1)
l.reverse()         #reverses linked list
l.print_list()      #prints out the LinkedList

# CHEAT SHEET
"""
    def setValue(self, index, value):   #change node value in index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return temp
"""