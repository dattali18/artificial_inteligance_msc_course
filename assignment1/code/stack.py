"""
empty stack [0]

[] stack that contains 3,2,1

3 is the top of the stack
"""


# creates a stack with x

class Stack:
    def __init__(self, n=0):
        if n < 0:
            self.items = []
        else:
            self.items = [n]

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





