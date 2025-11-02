from queue import Queue

class FrontierQueue:
    def __init__(self):
        self.queue = Queue()
        self.items_pushed = 0
        self.max_item_pushed = 0

    def enqueue(self, item):
        self.items_pushed += 1
        self.max_item_pushed = max(self.max_item_pushed, self.size())
        self.queue.enqueue(item)

    def dequeue(self):
        return self.queue.dequeue()

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()

    def peek(self):
        return self.queue.peek()

    def get_items_pushed(self):
        return self.items_pushed

    def get_max_item_pushed(self):
        return self.max_item_pushed
