"""
QUEUE TIME!!
Also can be done as a list but has bad Big O (O(1) + O(n))
Can be done as a LinkedList for better Big O (O(1) + O(1))
LinkedList DO NOT remove from end(last)

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def printQueue(self): #prints queue(first to last) one by one
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def Enqueue(self, value): #ADD ITEM TO THE END
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def Dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


Q = Queue(0)
Q.Enqueue(1)
Q.Enqueue(2)
Q.Enqueue(3)
Q.Dequeue()

Q.printQueue()