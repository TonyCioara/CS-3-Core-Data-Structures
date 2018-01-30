#!python

from linkedlist import LinkedList
import time
import sys


class Set(object):

    def __init__(self, elements=None):
        """Initialize this hash table with the given initial size."""
        init_size = 4
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of element entries

    def _bucket_index(self, value):
        """Return the bucket index where the given value would be stored."""
        return hash(value) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # TODO: Calculate load factor
        # return ...
        load_factor = self.size / len(self.buckets)
        return load_factor

    def items(self):
        """Return a list of all entries values in this set.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all pairs of value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of value entries by traversing its buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Count number of value-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets:
            item_count += bucket.length()
        return item_count
        # Equivalent to this list comprehension:
        return sum(bucket.length() for bucket in self.buckets)

    def contains(self, value):
        """Return True if this set contains the given value, or False.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given value belongs in
        index = self._bucket_index(value)
        bucket = self.buckets[index]
        # Check if an entry with the given value exists in that bucket
        entry = bucket.find(lambda data: data == value)
        return entry is not None  # True or False

    def add(self, value):
        """Insert or update the given value with its associated value.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given value belongs in
        index = self._bucket_index(value)
        bucket = self.buckets[index]
        # Find the entry with the given value in that bucket, if one exists
        # Check if an entry with the given value exists in that bucket
        entry = bucket.find(lambda data: data == value)
        if entry is not None:  # Found
            # In this case, the given value's value is being updated
            # Remove the old value-value entry from the bucket first
            return
        else:
            self.size += 1
        # Insert the new value-value entry into the bucket in either case
        bucket.append(value)
        # TODO: Check if the load factor exceeds a threshold such as 0.75
        # ...
        # TODO: If so, automatically resize to reduce the load factor
        # ...
        load_factor = self.load_factor()
        if load_factor > 0.75:
            self.resize()

    def delete(self, value):
        """Delete the given value and its associated value, or raise valueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given value belongs in
        index = self._bucket_index(value)
        bucket = self.buckets[index]
        # Find the entry with the given value in that bucket, if one exists
        entry = bucket.find(lambda data: data == value)
        if entry is not None:  # Found
            # Remove the value-value entry from the bucket
            self.size -= 1
            bucket.delete(entry)
        else:  # Not found
            raise ValueError('element not found: {}'.format(value))

    def resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new value).
        Best and worst case running time: ??? under what conditions? [TODO]
        Best and worst case space usage: ??? what uses this memory? [TODO]"""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # TODO: Get a list to temporarily hold all current value-value entries
        # ...
        temporary_buckets = self.items()
        # TODO: Create a new list of new_size total empty linked list buckets
        # ...
        self.buckets = [LinkedList() for i in range(new_size)]
        # TODO: Insert each value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        # ...
        self.size = 0
        for value in temporary_buckets:
            self.add(value)

    def union(self, other_set):
        new_set = Set()
        for element in self.items():
            new_set.add(element)
        for element in other_set.items():
            new_set.add(element)
        return new_set

    def intersection(self, other_set):
        new_set = Set()
        if self.size < other_set.size:
            for element in self.items():
                if other_set.contains(element):
                    new_set.add(element)
        else:
            for element in other_set.items():
                if self.contains(element):
                    new_set.add(element)
        return new_set

    def difference(self, other_set):
        new_set = Set()
        for element in self.items():
            if not other_set.contains(element):
                new_set.add(element)
        return new_set

    def is_subset(self, other_set):
        for element in self.items():
            if not other_set.contains(element):
                return False
        return True


def test_set():
    s = Set()
    s.add("willie")
    s.add("tony")
    s.add("uchena")
    s.add("phyllis")
    s.add("phyllis")
    s.add("en")
    s.add("egon")
    s.add("egoasdn")
    s.add("egoasdan")
    s.add("egasdasdaon")
    s.add("egosdasn")
    print(s.contains("egon"))
    print(s.contains("andrew"))
    s.delete("egon")
    print(s.contains("egon"))
    s.union(s)


if __name__ == '__main__':
    test_set()
