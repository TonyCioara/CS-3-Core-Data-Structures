#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

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

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? Always a constant number of steps,
        independent of input"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list.get_at_index(0)

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? Always a constant number of steps,
        independent of input"""
        # TODO: Remove and return front item, if any
        item = self.list.get_at_index(0)
        self.list.delete(item)
        return item


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.list_size = 0
        self.first_item = 0
        self.max_size = 4
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list_size == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list_size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? It's always a constant number of steps,
        independent of input"""
        # TODO: Insert given item
        if self.first_item >= self.max_size:
            self.list[self.first_item - self.max_size] = item
        else:
            self.list.append(item)
            self.list_size += 1
        if self.list_size >= self.max_size:
            self.resize()
        if self.first_item >= self.max_size:
            self.first_item -= self.max_size

    def resize(self):
        new_list = self.list
        self.list = []
        for index in range(0, self.max_size - 1):
            current_index = index + self.first_item
            if current_index >= self.max_size:
                current_index -= self.max_size
            self.list.append(new_list[index])
        self.max_size = self.max_size * 2

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.list_size > 0:
            return self.list[self.first_item]
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – Why? The whole array has to be moved over,
        or a new array has to be created"""
        # TODO: Remove and return front item, if any
        if self.list_size > 0:
            item = self.list[self.first_item]
            self.first_item += 1
            self.list_size -= 1
            return item
        raise ValueError('List is empty')


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
