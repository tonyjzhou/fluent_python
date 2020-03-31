from collections import deque


class Stack:
    """
    >>> s = Stack()
    >>> len(s)
    0

    >>> s.push(1)
    >>> len(s)
    1

    >>> s.push(2)
    >>> len(s)
    2

    >>> s.pop()
    >>> s.pop()
    >>> len(s)
    0

    >>> s.top()

    >>> s.push(2)
    >>> s.top()
    2
    """

    def __init__(self):
        self._deque = deque()

    def push(self, item):
        self._deque.append(item)

    def pop(self):
        self._deque.pop()

    def top(self):
        return self._deque[-1] if len(self) > 0 else None

    def __len__(self):
        return len(self._deque)
