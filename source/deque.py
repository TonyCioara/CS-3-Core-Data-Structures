from linkedlist import LinkedList


class LinkedDeque(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list.size == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.size

    def push_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? Always a constant number of steps,
        independent of input"""
        # TODO: Insert given item
        self.list.append(item)

    def push_front(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? Always a constant number of steps,
        independent of input"""
        # TODO: Insert given item
        self.list.prepend(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list.get_at_index(0)

    def pop_front(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? Always a constant number of steps,
        independent of input"""
        # TODO: Remove and return front item, if any
        item = self.list.get_at_index(0)
        self.list.delete(item)
        return item

    def pop_back(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? Always a constant number of steps,
        independent of input"""
        # TODO: Remove and return front item, if any
        item = self.list.get_at_index(self.list.size - 1)
        self.list.delete(item)
        return item


Deque = LinkedDeque
