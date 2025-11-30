"""
Implements a priority queue using a minimum heap.

- The heap is represented by a list self.queue
- The parent of index i is (i-1)//2  (equivalently (i+1)//2 - 1)
- The left child of index i is 2*i+1
- The right child of index i is 2*i+2

This is a direct class conversion of the original procedural implementation.
"""
import state
from typing import Any, Callable, List


class Frontier:
    """
    Priority queue backed by a min-heap.

    Parameters:
    - s: initial element to add to the queue
    - function: a callable f(x) that returns the priority (lower is higher priority)
    """

    def __init__(self, s: Any, function: Callable[[Any], float]):
        self.queue: List[Any] = [s]
        self.function = function
        self.total: int = 1   # total insertions (keeps old behaviour)
        self.max: int = 1     # maximum observed size (keeps old behaviour)

    # ----- helper index utilities -----
    def _parent(self, i: int) -> int:
        return (i + 1) // 2 - 1

    def _left(self, i: int) -> int:
        return (i + 1) * 2 - 1

    def _right(self, i: int) -> int:
        return (i + 1) * 2

    def _swap(self, x: int, y: int) -> None:
        self.queue[x], self.queue[y] = self.queue[y], self.queue[x]

    # ----- public API -----
    def is_empty(self) -> bool:
        """Return True iff the queue is empty."""
        return len(self.queue) == 0

    def insert(self, s: Any) -> None:
        """
        Insert state s into the priority queue.
        Moves the new element up to preserve the min-heap property.
        """
        self.queue.append(s)
        i = len(self.queue) - 1
        self.total += 1

        # update max size seen
        if len(self.queue) > self.max:
            self.max = len(self.queue)

        # bubble up while parent's priority is larger
        while i > 0 and self.function(self.queue[i]) < self.function(self.queue[self._parent(i)]):
            p = self._parent(i)
            self._swap(i, p)
            i = p

    def remove(self) -> Any:
        """
        Remove and return the root (minimum element). Returns 0 on underflow
        to match the original implementation.
        """
        if self.is_empty():
            return 0  # underflow like original code

        # keep parity with original code which updated max in remove()
        if len(self.queue) > self.max:
            self.max = len(self.queue)

        root = self.queue[0]
        # move last element to root and pop the last
        self.queue[0] = self.queue[-1]
        self.queue.pop()

        if not self.is_empty():
            self._heapify(0)

        return root

    # ----- internal heap maintenance -----
    def _heapify(self, i: int) -> None:
        """
        Fix the heap by rolling down from index i.
        If node i is larger than any child, swap with the smallest child and recurse.
        """
        min_son = i
        l = len(self.queue)
        if self._left(i) < l and self.function(self.queue[self._left(i)]) < self.function(self.queue[min_son]):
            min_son = self._left(i)
        if self._right(i) < l and self.function(self.queue[self._right(i)]) < self.function(self.queue[min_son]):
            min_son = self._right(i)
        if min_son != i:
            self._swap(i, min_son)
            self._heapify(min_son)

    # convenience
    def peek(self) -> Any:
        """Return the root without removing it; return None if empty."""
        return None if self.is_empty() else self.queue[0]

    def __len__(self) -> int:
        return len(self.queue)


# Example usage (keep commented or remove when integrating):
# def priority_fn(x): return x  # for numeric priorities
# pq = Fortier(5, priority_fn)
# pq.insert(3)
# pq.insert(7)
# print(pq.remove())  # -> 3
# print(pq.remove())  # -> 5