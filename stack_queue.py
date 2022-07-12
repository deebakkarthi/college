from stack import stack


class queue:
    def __init__(self):
        self.front = stack()
        self.back = stack()

    def enqueue(self, x):
        self.back.push(x)

    def dequeue(self):
        if self.front:
            return self.front.pop()
        else:
            while self.back:
                self.front.push(self.back.pop())
            return self.front.pop()

    def front(self):
        if self.front:
            return self.front.top()
        else:
            while self.back:
                self.front.push(self.back.pop())
            return self.front.top()

    def __bool__(self):
        return bool(self.front) or bool(self.back)

    def __len__(self):
        return len(self.front) + len(self.back)
