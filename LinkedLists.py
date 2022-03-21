from email import header
from unittest.mock import NonCallableMock


class node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        n = self.head
        if self.head is None:
            print("Linked list is empty")
        else:
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        n = self.head
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add(self,data,index):
        new_node = node(data)
        cur = self.head
        for i in range(index-1):
            prev = cur
            next = cur.ref
            cur = cur.ref
        prev.ref = new_node
        new_node.ref = next

LL1 = LinkedList()
LL1.add_end(4)
LL1.add_end(6)
LL1.add_end(8)
LL1.add_end(2)
LL1.printLL()
print(" ")
LL1.add(10,3)
LL1.printLL()