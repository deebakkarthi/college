from dll import dll, list_node


class deque:
    def __init__(self):
        self.list = dll()

    def insert_first(self, x):
        self.list.insert_head(list_node(x))

    def insert_last(self, x):
        self.list.insert_tail(list_node(x))

    def remove_first(self):
        if self:
            return self.list.remove_head().val
        else:
            return None

    def remove_last(self):
        if self:
            return self.list.remove_tail().val
        else:
            return None

    def last(self):
        if self:
            return self.list.head.val
        else:
            return None

    def first(self):
        if self:
            return self.list.tail.val
        else:
            return None

    def __bool__(self):
        return bool(self.list)

    def __len__(self):
        return len(self.list)
