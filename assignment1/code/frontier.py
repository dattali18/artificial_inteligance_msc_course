"""
# יוצר מחסנית ״משוכללת״
[stack, max. depth, init. state, try next level?]
stack - a simple stack as defined at stack.py
max.depth - the current search depth of ID
init.state - the initial state of the problem
try next level - is there a reason to search deeper
"""
from stack import Stack
from state import *

class Frontier:
    def __init__(self, initial):
        self.stack = Stack()
        self.depth = 1
        self.init = initial
        self.cutoff = False
        self.total_item_pushed = 0

        # push te init-state into the stack
        self.stack.push(self.init)

    def is_empty(self):
        return self.stack.is_empty() and not self.cutoff # stack is empty and try next level is false

    def insert(self, x):
        if x.path_len() <= self.depth: # check if x is not too deep
            self.total_item_pushed += 1
            self.stack.push(x)    # insert x to stack
        else:
            self.cutoff = True               # there is a reason to search deeper if needed

    def remove(self):
        if self.stack.is_empty():    # check is there are no states in the stack
            if self.cutoff:                # check if there is a reason to search deeper
                self.depth += 1             # increase search depth
                self.cutoff = False          # meanwhile there is no evidence to  a need to search deeper
                return self.init         # return the initial state
            else:
                return 0

        return self.stack.pop()   # if there are items in the stack ...
