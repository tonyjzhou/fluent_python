from collections import deque


class Queue:
    """
    >>> q = Queue()
    >>> len(q)
    0

    >>> q.add(1)
    >>> len(q)
    1

    >>> q.add(2)
    >>> len(q)
    2

    >>> q.peek()
    1

    >>> len(q)
    2

    >>> q.poll()
    1
    >>> len(q)
    1
    >>> q.peek()
    2
    """

    def __init__(self):
        self._deque = deque()

    def __len__(self):
        return len(self._deque)

    def add(self, item):
        self._deque.append(item)

    def peek(self):
        return self._deque[0] if len(self) > 0 else None

    def poll(self):
        return self._deque.popleft() if len(self) > 0 else None
