from stack import Stack

class Frontier:
    def __init__(self, initial):
        self.stack = Stack()
        self.depth = 1
        self.init = initial
        self.cutoff = False
        self.items_pushed = 0
        self.max_items_pushed = 0

        # push te init-state into the stack
        self.stack.push(self.init)

    def is_empty(self):
        return self.stack.is_empty() and not self.cutoff # stack is empty and try next level is false

    def insert(self, x):
        if x.path_len() <= self.depth: # check if x is not too deep
            self.items_pushed += 1
            self.max_items_pushed = max(self.stack.size(), self.max_items_pushed)
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

    def get_items_pushed(self):
        return self.items_pushed

    def get_max_items_pushed(self):
        return self.max_items_pushed