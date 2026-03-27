#!/usr/bin/env python3


class CountedIterator:
    """Iterator that keeps track of how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to zero."""
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """
        Return the next item from the iterator.
        Increment the counter each time an item is successfully retrieved.
        """
        item = next(self._iterator) 
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self._count
