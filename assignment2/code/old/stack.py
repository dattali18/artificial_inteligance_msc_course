"""
Stack class conversion of the original procedural implementation.

Original behavior preserved:
- create(x) -> stack containing x (constructor accepts an optional initial element)
- is_empty(s) -> True iff stack is empty
- insert(s,x) -> push x onto the top of the stack (index 0)
- remove(s) -> pop and return top element; returns 0 on underflow (matches original)

Note: the implementation uses list.insert(0, x) / pop(0) to preserve the original semantics
(which are O(n)). If you want O(1) push/pop, switch to append()/pop() and treat the list end as top.
"""
from typing import Any, List, Optional


class Stack:
    def __init__(self, x: Optional[Any] = None):
        """Create a stack. If x is provided, the stack starts with [x]."""
        self._stack: List[Any] = []
        if x is not None:
            self._stack.append(x)

    def is_empty(self) -> bool:
        """Return True iff the stack is empty."""
        return self._stack == []

    # keep original names for compatibility
    def insert(self, x: Any) -> None:
        """Push x onto the top of the stack (top is index 0 to match original)."""
        self._stack.insert(0, x)

    def remove(self) -> Any:
        """
        Pop and return the top element.
        Returns 0 on underflow to match the original procedural implementation.
        """
        if self.is_empty():
            return 0  # underflow like original code
        x = self._stack[0]
        self._stack.pop(0)
        return x

    # convenience / Pythonic aliases
    def push(self, x: Any) -> None:
        self.insert(x)

    def pop(self) -> Any:
        return self.remove()

    def peek(self) -> Optional[Any]:
        """Return the top element without removing it, or None if empty."""
        return None if self.is_empty() else self._stack[0]

    def __len__(self) -> int:
        return len(self._stack)

    def as_list(self) -> List[Any]:
        """Return a shallow copy of the internal list (top at index 0)."""
        return list(self._stack)