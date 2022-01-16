""" Creates nodes, can add functions for the node if needed """
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("LENGTH NORMAL: ", self.length)

    def reverse_print_list(self):
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev
        print("LENGTH REVERSE: ", self.length)

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index >= self.length or index < 0:
            return None

        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def setValue(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True                 #return True or False based on if value was succesfully changed
        return False  

    def delete(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def insert(self, index, value):
        if index >= self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node
        self.length += 1
        return True


D = DoublyLinkedList(0)
D.append(1)
D.append(2)
D.append(3)
D.pop()
D.prepend(420)
D.popFirst()
D.setValue(0,6969)
D.insert(1,121)
D.delete(1)
D.delete(0)


D.print_list()
print("--------------")
D.reverse_print_list()
