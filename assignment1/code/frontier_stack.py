from stack import Stack

class FrontierStack:
    def __init__(self):
        self.stack = Stack()
        self.items_pushed = 0
        self.max_item_pushed = 0

    def push(self, item):
        self.items_pushed += 1
        self.max_item_pushed = max(self.max_item_pushed, self.size())
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

    def get_items_pushed(self):
        return self.items_pushed

    def get_max_item_pushed(self):
        return self.max_item_pushed
