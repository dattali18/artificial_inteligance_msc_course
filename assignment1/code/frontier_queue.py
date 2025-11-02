from queue import Queue

class FrontierQueue:
    def __init__(self):
        self.queue = Queue()
        self.total_item_pushed = 0

    def enqueue(self, item):
        self.total_item_pushed += 1
        self.queue.enqueue(item)

    def dequeue(self):
        return self.queue.dequeue()

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()

    def peek(self):
        return self.queue.peek()
