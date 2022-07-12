from sll import sll, list_node

class stack:
    def __init__(self):
        self.list = sll()

    def push(self, x):
        self.list.insert_head(list_node(x))

    def pop(self):
        if self:
            return self.list.remove_head().val
        else:
            return None

    def top(self):
        if self:
            return self.list.head.val
        else:
            return None

    def __len__(self):
        return len(self.list)

    def __bool__(self):
        return bool(self.list)
