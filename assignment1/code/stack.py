
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)





