from dll import dll, list_node


class queue:
    def __init__(self):
        self.list = dll()

    def enqueue(self, x):
        self.list.insert_tail(list_node(x))

    def dequeue(self):
        if self:
            return self.list.remove_head().val
        else:
            return None

    def front(self):
        if self:
            return self.list.head.val
        else:
            return None

    def __bool__(self):
        return bool(self.list)

    def __len__(self):
        return len(self.list)
