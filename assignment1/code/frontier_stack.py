from stack import Stack

class FrontierStack:
    def __init__(self):
        self.stack = Stack()
        self.total_item_pushed = 0

    def push(self, item):
        self.total_item_pushed += 1
        self.stack.push(item)

    def is_empty(self):
        return self.stack.is_empty()

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def top(self):
        return self.stack.top()

    def size(self):
        return self.stack.size()