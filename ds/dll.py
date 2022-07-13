# Doubly linked list ADT
class list_node:
    def __init__(self, val, p=None, n=None):
        self.val = val
        self.prev = p
        self.next = n

    # __eq__ enables the == operation
    # can use node1 ==  node2 instead of node1.val == node2.val
    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class dll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, new):
        if self:
            new.next = self.head
            self.head.prev = new
        # if empty list init tail
        else:
            self.tail = new
        self.head = new
        self.size += 1

    def insert_tail(self, new):
        if self:
            new.prev = self.tail
            self.tail.next = new
        # if empty list init head
        else:
            self.head = new
        self.tail = new
        self.size += 1

    def insert_before(self, node, new):
        if node is self.head:
            self.insert_head(new)
        else:
            self.insert_between(node.prev, new, node)
            self.size += 1

    def insert_after(self, node, new):
        if node is self.tail:
            self.insert_tail(new)
        else:
            self.insert_between(node, new, node.next)
            self.size += 1

    def insert_between(self, prev, new, next):
        prev.next = new
        new.prev = prev
        new.next = next
        next.prev = new

    def connect(self, prev, next):
        prev.next = next
        next.prev = prev

    def remove_head(self):
        tmp = self.head
        # Not an empty list
        if tmp:
            self.head = tmp.next
            # Not an empty list
            if self.head:
                self.head.prev = None
        self.size -= 1
        return tmp

    def remove_tail(self):
        tmp = self.tail
        # Not an empty list
        if tmp:
            self.tail = tmp.prev
            # Not an empty list
            if self.tail:
                self.tail.next = None
        self.size -= 1
        return tmp

    def remove_after(self, node):
        ret = node.next
        # If there is a node
        if ret:
            # The logic to check .next.next is too messy
            # so just calling remove_tail if node is tail
            if ret is self.tail:
                return self.remove_tail()
            else:
                self.connect(node, ret.next)
        self.size -= 1
        return ret

    def remove_before(self, node):
        ret = node.prev
        if ret:
            # Same reason a remove_after()
            if ret is self.head:
                return self.remove_head()
            else:
                self.connect(ret.prev, node)
        self.size -= 1
        return ret

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
