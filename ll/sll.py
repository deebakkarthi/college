# Singly linked list ADT

from dataclasses import dataclass

class list_node:
    def __init__(self, val, n=None):
        self.val = val
        self.next = n

    # __eq__ enables the == operation
    # can use node1 ==  node2 instead of node1.val == node2.val
    def __eq__(self, other):
        return self.val == other.val
    
    def __str__(self):
        return str(self.val)

class sll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, new):
        if self:
            new.next = self.head
        # If empty list init tail
        else:
            self.tail = new
        self.head = new
        self.size += 1

    def remove_head(self):
        tmp = self.head
        self.head = tmp.next
        self.size -= 1
        return tmp
    
    def insert_tail(self,new):
        if self:
            self.tail.next = new
        # If empty list init head
        else:
            self.head = new
        self.tail = new
        self.size += 1

    def insert_after(self,node,new):
        new.next = node.next
        node.next = new
        self.size += 1

    def remove_after(self,node):
        tmp = node.next
        # tmp maybe None
        if tmp:
            node.next = tmp.next
            self.size -= 1
        return tmp

    # pythonic way of checking empty list
    def __bool__(self):
        return self.size != 0

    # returns generator
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    # enables len(list)
    def __len__(self):
        return self.size
